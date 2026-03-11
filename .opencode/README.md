# AI Sales Team — OpenCode Skills

> AI-powered sales intelligence skills optimized for OpenCode. Research prospects, qualify leads, map decision makers, generate outreach, prepare for meetings, and build proposals.

---

## Quick Start

### Installation

These skills work with OpenCode's skill system. Use them in two ways:

**Option 1: Task Delegation (Recommended)**
```python
task(
    category="unspecified-high",
    load_skills=["sales-research"],
    prompt="Research https://stripe.com",
    run_in_background=False
)
```

**Option 2: Direct Skill Usage**
```
# Tell the AI what you want:
"Research Stripe for me"
"Find decision makers at Acme"
"Prepare outreach for Notion"
```

---

## Available Skills

| Skill | Purpose | Usage |
|-------|---------|-------|
| `sales` | Orchestrator — routes to all skills | `load_skills=["sales"]` |
| `sales-prospect` | Full audit (5 parallel agents) | `load_skills=["sales-prospect"]` |
| `sales-research` | Company research & firmographics | `load_skills=["sales-research"]` |
| `sales-qualify` | Lead qualification (BANT/MEDDIC) | `load_skills=["sales-qualify"]` |
| `sales-contacts` | Decision maker identification | `load_skills=["sales-contacts"]` |
| `sales-outreach` | Cold outreach sequences | `load_skills=["sales-outreach"]` |
| `sales-followup` | Follow-up sequences | `load_skills=["sales-followup"]` |
| `sales-prep` | Meeting preparation | `load_skills=["sales-prep"]` |
| `sales-proposal` | Client proposals | `load_skills=["sales-proposal"]` |
| `sales-objections` | Objection handling | `load_skills=["sales-objections"]` |
| `sales-icp` | Ideal Customer Profile | `load_skills=["sales-icp"]` |
| `sales-competitors` | Competitive intelligence | `load_skills=["sales-competitors"]` |
| `sales-report` | Pipeline report (Markdown) | `load_skills=["sales-report"]` |
| `sales-report-pdf` | Pipeline report (PDF) | `load_skills=["sales-report-pdf"]` |

---

## Usage Examples

### Full Prospect Analysis
```
task(load_skills=["sales-prospect"], prompt="Analyze https://stripe.com")
```

### Company Research
```
task(load_skills=["sales-research"], prompt="Research https://stripe.com")
```

### Find Decision Makers
```
task(load_skills=["sales-contacts"], prompt="Find decision makers at https://notion.so")
```

### Lead Qualification
```
task(load_skills=["sales-qualify"], prompt="Qualify https://acme.com using BANT")
```

### Generate Outreach
```
task(load_skills=["sales-outreach"], prompt="Write cold outreach for Linear")
```

### Meeting Preparation
```
task(load_skills=["sales-prep"], prompt="Prepare for meeting with https://datadog.com")
```

### Handle Objections
```
task(load_skills=["sales-objections"], prompt="Handle SaaS pricing objections")
```

### Competitive Intelligence
```
task(load_skills=["sales-competitors"], prompt="Analyze competitors for https://stripe.com")
```

### Build ICP
```
task(load_skills=["sales-icp"], prompt="Build ICP for B2B SaaS, 50-200 employees")
```

### Pipeline Report
```
task(load_skills=["sales-report"], prompt="Generate sales pipeline report")
```

### PDF Report
```
task(load_skills=["sales-report-pdf"], prompt="Generate PDF pipeline report")
```

---

## Output Files

All skills save results to the current directory:

- `PROSPECT-ANALYSIS.md` — Full prospect audit
- `COMPANY-RESEARCH.md` — Company research
- `LEAD-QUALIFICATION.md` — BANT/MEDDIC scoring
- `DECISION-MAKERS.md` — Contact mapping
- `OUTREACH-SEQUENCE.md` — Email sequences
- `FOLLOWUP-SEQUENCE.md` — Follow-up emails
- `MEETING-PREP.md` — Meeting brief
- `CLIENT-PROPOSAL.md` — Proposals
- `OBJECTION-PLAYBOOK.md` — Objection responses
- `IDEAL-CUSTOMER-PROFILE.md` — ICP definition
- `COMPETITIVE-INTEL.md` — Competitive analysis
- `SALES-REPORT.md` — Pipeline report
- `SALES-REPORT-*.pdf` — PDF reports

---

## Scoring

### Prospect Score (0-100)

| Category | Weight |
|----------|--------|
| Company Fit | 25% |
| Contact Access | 20% |
| Opportunity Quality | 20% |
| Competitive Position | 15% |
| Outreach Readiness | 20% |

### Grades

| Score | Grade |
|-------|-------|
| 90-100 | A+ (Hot Lead) |
| 75-89 | A (Strong) |
| 60-74 | B (Qualified) |
| 40-59 | C (Lukewarm) |
| 0-39 | D (Poor Fit) |

---

## Requirements

- **OpenCode** — [Install OpenCode](https://opencode.ai)
- **Python 3.8+** (optional) — For PDF generation
- **WebFetch** — For website analysis
- **WebSearch** — For research

---

## License

MIT License
