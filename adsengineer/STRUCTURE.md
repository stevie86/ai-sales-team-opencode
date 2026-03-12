# AdsEngineer Sales System — Structure Documentation

---

## Overview

This system manages prospects, partners, and multi-project companies with role-based access control.

---

## Directory Structure

```
adsengineer/
├── PRODUCT/                      # Brand & positioning (public)
│   └── BRAND.md
│
├── PROSPECTS/
│   ├── [company-name]/
│   │   ├── META.json             # Company metadata (languages, industries, projects)
│   │   ├── COMPANY-RESEARCH.md   # What we found (facts)
│   │   ├── COMPETITIVE-INTEL.md  # Deep technical analysis
│   │   ├── PROSPECT-ANALYSIS.md  # Scoring + fit
│   │   ├── PITCH.md              # Sales pitch
│   │   ├── CAMPAIGN.md           # Ad campaign strategy
│   │   ├── projects/
│   │   │   └── [project-name]/   # Individual property/site
│   │   │       ├── META.json     # Project-specific metadata
│   │   │       ├── CAMPAIGN.md   # Project-specific ads
│   │   │       └── outreach/
│   │   │           └── EMAIL-SEQUENCE.md
│   │   │
│   │   └── outreach/             # Company-level outreach
│   │       └── EMAIL-SEQUENCE.md
│   │
│   └── babyrella/
│       └── ...
│
└── PARTNERS/
    ├── [partner-name]/
    │   ├── PARTNERSHIP-PITCH.md
    │   ├── CLEARANCE.md          # Partner's access level
    │   └── outreach/
    │       └── PARTNER-OUTREACH.md
    │
    └── proseller/
        ├── PARTNERSHIP-PITCH.md
        ├── CLEARANCE.md
        ├── PROSPECTS/            # Prospects shared with this partner
        │   └── orderflow.ch/
        └── outreach/
```

---

## META.json Schema

### Company Level

```json
{
  "company": {
    "name": "OrderFlow AG",
    "domain": "orderflow.ch",
    "platform": "ConcertoPro",
    "founded": 2004,
    "employees": "10-50"
  },
  "languages": ["de", "fr"],
  "industries": ["e-commerce", "b2b"],
  "delivery": ["CH", "LI"],
  "projects": ["orderflow"],
  "estimated_ad_spend": "5000-15000",
  "compliance_status": {
    "ndsg": "non-compliant",
    "gdpr": "unknown"
  },
  "data_loss": "35-45%"
}
```

### Project Level

```json
{
  "project": {
    "name": "OrderFlow",
    "domain": "orderflow.ch",
    "type": "e-commerce"
  },
  "languages": ["de", "fr"],
  "delivery": ["CH", "LI"],
  "products": 1000000,
  "compliance": {
    "cmp": false,
    "server_side_tracking": false,
    "consent_mechanism": false
  }
}
```

---

## Multi-Project Examples

### Example 1: Enterprise with Multiple Brands

```
prospects/acme-corp/
├── META.json                    # Company-level: all brands, HQ info
├── projects/
│   ├── brand-a/                # Brand A-specific
│   │   ├── META.json
│   │   └── CAMPAIGN.md
│   ├── brand-b/                # Brand B-specific
│   │   ├── META.json
│   │   └── CAMPAIGN.md
│   └── brand-c/                # Brand C-specific
│       ├── META.json
│       └── CAMPAIGN.md
```

### Example 2: Platform with Multiple Customer Sites

```
prospects/proseller/
├── META.json                    # Platform-level
├── projects/
│   ├── orderflow/              # Referenced customer
│   │   └── META.json
│   └── babyrella/              # Another customer
│       └── META.json
```

---

## Language Codes

Use ISO 639-1 codes:

| Code | Language |
|------|----------|
| de | German |
| fr | French |
| it | Italian |
| en | English |
| rm | Romansh |
| es | Spanish |

---

## Partner Clearance Levels

See: `PARTNERS/[partner-name]/CLEARANCE.md`

---

*Last updated: March 2026*
