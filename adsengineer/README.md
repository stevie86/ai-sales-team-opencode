# AdsEngineer Sales System

**Note:** This folder contains sensitive customer data and is NOT committed to GitHub. The `.gitignore` protects actual prospect/partner data.

---

## Quick Reference: Where Are My Files?

### For Alfred Rossi (Partner)
```
adsengineer/partners/proseller/
├── PARTNERSHIP-PITCH.md      ← Partnership proposal
├── outreach/
│   └── PARTNER-OUTREACH.md  ← Emails to Alfred
└── META.json                ← Partner details
```

### For OrderFlow.ch (Prospect)
```
adsengineer/prospects/orderflow.ch/
├── COMPANY-RESEARCH.md      ← Background research
├── COMPETITIVE-INTEL.md     ← Technical audit
├── PROSPECT-ANALYSIS.md     ← Scoring & fit
├── PITCH.md                 ← Sales pitch (3-tier)
├── CAMPAIGN.md              ← Ad campaign strategy
├── outreach/
│   └── EMAIL-SEQUENCE.md    ← 4-email sequence
├── META.json                ← Company data
└── projects/
    └── orderflow/
        └── META.json       ← Project-specific data
```

---

## Directory Structure

```
adsengineer/
├── STRUCTURE.md              ← Full schema documentation
├── PARTNERS/
│   └── CLEARANCE.md         ← Access level definitions
│
├── PRODUCT/
│   └── BRAND.md             ← General brand positioning
│
├── PROSPECTS/
│   ├── orderflow.ch/        ← Prospect: OrderFlow
│   ├── proseller/           ← Prospect + Partner (both!)
│   └── babyrella/           ← Another prospect
│
├── BRIEF/
│   └── PRODUCT-BRIEF.md     ← Product information
│
└── TEMPLATES/
    ├── PROSPECT-META.json   ← Prospect data template
    ├── PROJECT-META.json    ← Project data template
    └── PARTNER-META.json    ← Partner data template
```

---

## File Types Explained

| File | Purpose |
|------|---------|
| `META.json` | Structured data (languages, compliance, metrics) |
| `COMPANY-RESEARCH.md` | Background on the company |
| `COMPETITIVE-INTEL.md` | Technical analysis, audit results |
| `PROSPECT-ANALYSIS.md` | Fit score, BANT scoring |
| `PITCH.md` | Sales pitch script |
| `CAMPAIGN.md` | Ad campaign strategy |
| `EMAIL-SEQUENCE.md` | Outreach emails |
| `PARTNERSHIP-PITCH.md` | Partner proposal |
| `PARTNER-OUTREACH.md` | Partner outreach emails |

---

## Language Tracking

Languages are stored in `META.json`:

```json
"languages": {
  "website": ["de", "fr"],
  "sales": ["de", "fr", "en"],
  "support": ["de", "fr"]
}
```

### Language Codes
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

See: `PARTNERS/CLEARANCE.md`

| Level | Name | Access |
|-------|------|--------|
| 1 | Strategic | Full data, pricing, roadmap |
| 2 | Integration | Summary only, anonymized |
| 3 | Referral | Name only |

---

## How to Add New Prospects

1. Create folder: `adsengineer/prospects/[company-name]/`
2. Copy template: `cp adsengineer/templates/PROSPECT-META.json adsengineer/prospects/[company-name]/META.json`
3. Fill in META.json with company data
4. Create subfolders: `projects/`, `outreach/`
5. Generate documents using skills

---

## How to Add New Partners

1. Create folder: `adsengineer/partners/[partner-name]/`
2. Copy template: `cp adsengineer/templates/PARTNER-META.json adsengineer/partners/[partner-name]/META.json`
3. Fill in META.json with partner data
4. Create: `PARTNERSHIP-PITCH.md`, `outreach/PARTNER-OUTREACH.md`

---

## Git & Data Privacy

| What | Status |
|------|--------|
| Templates | ✅ Committed to GitHub |
| Structure docs | ✅ Committed |
| Clearance docs | ✅ Committed |
| Actual prospect data | ❌ In .gitignore |
| Actual partner data | ❌ In .gitignore |

This protects sensitive customer information from being committed to the repository.

---

## Skills Available

| Skill | Purpose |
|-------|---------|
| `sales-research` | Company research |
| `sales-pilot-pricing` | Pilot program pricing |
| `marketing-ads-campaign` | Create ad campaigns |
| `marketing-seo-audit` | SEO audits |

---

*Last updated: March 2026*
