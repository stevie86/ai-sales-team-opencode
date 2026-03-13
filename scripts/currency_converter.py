#!/usr/bin/env python3
"""
Currency Converter — Fetches live rates and converts between currencies.
Usage:
    python3 currency_converter.py --fetch          # Fetch latest rates
    python3 currency_converter.py --convert 100 USD EUR  # Convert 100 USD to EUR
    python3 currency_converter.py --convert 500 CHF --to USD  # Convert 500 CHF to USD
"""

import json
import sys
import os
import argparse
from datetime import datetime, timedelta
from urllib.request import urlopen
from urllib.error import URLError

API_URL = "https://open.er-api.com/v6/latest/{base}"
CACHE_FILE = ".currency_rates.json"
CACHE_DURATION_HOURS = 24

DEFAULT_RATES = {
    "CHF": {"USD": 0.88, "EUR": 0.95, "GBP": 1.15},
    "USD": {"CHF": 1.14, "EUR": 1.08, "GBP": 1.31},
    "EUR": {"CHF": 1.05, "USD": 0.93, "GBP": 1.21},
    "GBP": {"CHF": 0.87, "USD": 0.76, "EUR": 0.83},
}


def load_cached_rates():
    """Load rates from cache file if valid."""
    if not os.path.exists(CACHE_FILE):
        return None

    try:
        with open(CACHE_FILE, "r") as f:
            data = json.load(f)

        fetched = datetime.fromisoformat(data.get("fetched", "2000-01-01"))
        expires = fetched + timedelta(hours=CACHE_DURATION_HOURS)

        if datetime.now() < expires:
            return data
    except (json.JSONDecodeError, KeyError, ValueError):
        pass

    return None


def save_cached_rates(data):
    """Save rates to cache file."""
    data["fetched"] = datetime.now().isoformat()
    with open(CACHE_FILE, "w") as f:
        json.dump(data, f, indent=2)


def fetch_live_rates(base_currency="USD"):
    """Fetch live rates from API."""
    print(f"Fetching live rates from open.er-api.com (base: {base_currency})...")

    try:
        url = API_URL.format(base=base_currency)
        with urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode())

        if data.get("result") != "success":
            raise Exception("API returned unsuccessful result")

        rates = {
            "base": base_currency,
            "rates": data.get("rates", {}),
            "timestamp": data.get("time_last_update_utc", ""),
        }

        print(f"✓ Fetched {len(rates['rates'])} currency rates")
        return rates

    except URLError as e:
        print(f"✗ Network error: {e}")
        return None
    except Exception as e:
        print(f"✗ Error: {e}")
        return None


def convert(amount, from_currency, to_currency, rates):
    """Convert amount from one currency to another."""
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    # If base matches
    if rates["base"] == from_currency:
        rate = rates["rates"].get(to_currency, 1.0)
    # If base matches target
    elif rates["base"] == to_currency:
        rate = 1.0 / rates["rates"].get(from_currency, 1.0)
    # Cross rate through base
    else:
        # Convert to base first, then to target
        to_base = 1.0 / rates["rates"].get(from_currency, 1.0)
        rate = to_base * rates["rates"].get(to_currency, 1.0)

    return amount * rate


def main():
    parser = argparse.ArgumentParser(description="Currency converter with live rates")
    parser.add_argument(
        "--fetch", action="store_true", help="Fetch latest rates from API"
    )
    parser.add_argument("--convert", type=float, help="Amount to convert")
    parser.add_argument(
        "--from", dest="from_currency", default="USD", help="Source currency"
    )
    parser.add_argument(
        "--to", dest="to_currency", default="EUR", help="Target currency"
    )
    parser.add_argument("--base", default="USD", help="Base currency for fetching")
    parser.add_argument(
        "--rates", action="store_true", help="Show current cached rates"
    )

    args = parser.parse_args()

    # Fetch rates
    if args.fetch:
        rates = fetch_live_rates(args.base)
        if rates:
            save_cached_rates(rates)
            print("\nRates cached successfully!")
            print(f"Valid for {CACHE_DURATION_HOURS} hours")
        sys.exit(0)

    # Show rates
    if args.rates:
        rates = load_cached_rates()
        if rates:
            print(f"\nCached rates (base: {rates['base']})")
            print(f"Fetched: {rates.get('fetched', 'unknown')}")
            print("\nKey rates:")
            for currency in ["CHF", "EUR", "GBP", "USD", "CAD", "AUD", "JPY"]:
                if currency in rates["rates"]:
                    print(f"  {currency}: {rates['rates'][currency]}")
        else:
            print("No cached rates. Run with --fetch to get live rates.")
        sys.exit(0)

    # Convert
    if args.convert:
        rates = load_cached_rates()
        if not rates:
            print("No cached rates. Run with --fetch first, or use default rates.")
            # Use default rates
            rates = {
                "base": "USD",
                "rates": {
                    "CHF": 0.88,
                    "EUR": 0.95,
                    "GBP": 1.15,
                    "USD": 1.0,
                    "CAD": 1.36,
                    "AUD": 1.58,
                    "JPY": 149,
                },
            }

        result = convert(args.convert, args.from_currency, args.to_currency, rates)

        print(
            f"\n{args.convert} {args.from_currency.upper()} = {result:.2f} {args.to_currency.upper()}"
        )
        print(f"(Rates from: {rates.get('fetched', 'defaults')})")
        sys.exit(0)

    # No args, show help
    parser.print_help()


if __name__ == "__main__":
    main()
