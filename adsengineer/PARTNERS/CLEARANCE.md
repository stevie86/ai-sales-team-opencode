# Partner Clearance Levels

## Overview

Partners are assigned clearance levels that determine what information they can access and share.

---

## Clearance Levels

| Level | Name | Access | Sharing |
|-------|------|--------|---------|
| **Tier 1** | Strategic Partner | Full prospect data, pricing, roadmap | Can reference publicly |
| **Tier 2** | Integration Partner | Prospect data, campaign strategy | Must anonymize |
| **Tier 3** | Referral Partner | Prospect name + challenge only | No data sharing |

---

## Tier 1: Strategic Partner

### Access

| Resource | Access |
|----------|--------|
| Company Research | ✅ Full |
| Competitive Intel | ✅ Full |
| Prospect Analysis | ✅ Full |
| Pricing | ✅ Full |
| Roadmap | ✅ Full |
| Campaign Strategy | ✅ Full |
| Audit Results | ✅ Full |
| Contact Details | ✅ Full |

### Sharing Rules

- Can mention AdsEngineer by name
- Can share case studies (with permission)
- Can reference prospect names publicly
- Can share pricing in proposals
- Must get approval for press/marketing

### Example: ProSeller (Tier 1)

ProSeller is a **Strategic Partner** because:
- They control the ConcertoPro platform
- They can integrate our solution natively
- They have their own sales team
- They're investing in the partnership

---

## Tier 2: Integration Partner

### Access

| Resource | Access |
|----------|--------|
| Company Research | ✅ Summary only |
| Competitive Intel | ✅ Summary only |
| Prospect Analysis | ✅ Score + key challenges |
| Pricing | ❌ Not disclosed |
| Roadmap | ❌ Not disclosed |
| Campaign Strategy | ✅ Strategy only |
| Audit Results | ❌ Not disclosed |
| Contact Details | ✅ Anonymized |

### Sharing Rules

- Cannot mention AdsEngineer by name (use "our solution")
- Cannot share specific case studies
- Cannot reference prospect names (use "a major Swiss e-commerce company")
- Cannot share pricing
- Must anonymize all data

### Example: Web Agencies (Tier 2)

Web agencies are **Integration Partners** because:
- They implement solutions for clients
- They need campaign strategy guidance
- They don't need full audit data
- They should present as their own service

---

## Tier 3: Referral Partner

### Access

| Resource | Access |
|----------|--------|
| Company Research | ❌ Not disclosed |
| Competitive Intel | ❌ Not disclosed |
| Prospect Analysis | ❌ Not disclosed |
| Pricing | ❌ Not disclosed |
| Campaign Strategy | ❌ Not disclosed |
| Audit Results | ❌ Not disclosed |
| Contact Details | ✅ Company name only |

### Sharing Rules

- Can only share prospect company name
- Cannot share any technical details
- Cannot present as a partner
- Pure referral relationship only

### Example: Consultants (Tier 3)

Consultants are **Referral Partners** because:
- They provide leads only
- They don't implement or manage campaigns
- Minimal relationship required

---

## Prospect Data by Clearance

### OrderFlow.ch Data

| Data Point | Tier 1 | Tier 2 | Tier 3 |
|------------|--------|--------|--------|
| Company Name | ✅ | ❌ | ✅ |
| Domain | ✅ | ❌ | ❌ |
| Compliance Status | ✅ | Summary | ❌ |
| Data Loss % | ✅ | ❌ | ❌ |
| Technical Details | ✅ | ❌ | ❌ |
| Audit Results | ✅ | ❌ | ❌ |
| Contact (Alfred Rossi) | ✅ | Anonymized | ❌ |

---

## Clearance Assignment

| Partner | Level | Reason |
|---------|-------|--------|
| ProSeller AG | Tier 1 | Platform integration, sales team |
| Web Agencies | Tier 2 | Client implementation |
| Consultants | Tier 3 | Lead referrals only |

---

## Updating Clearance

To change a partner's clearance level:

1. Update their `CLEARANCE.md` file
2. Update prospect `META.json` to reflect what they can see
3. Review all shared documents for compliance

---

*Last updated: March 2026*
