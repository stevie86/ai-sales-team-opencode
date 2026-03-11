# AI Sales Team — OpenCode Orchestrator

> Your AI-powered sales intelligence system for OpenCode. Research prospects, qualify leads, identify decision makers, generate personalized outreach, prepare for meetings, and build winning proposals.

This is the main orchestrator skill that routes to 13 sub-skills. Use it directly or invoke individual skills.

---

## Available Skills

| Skill | Purpose | Input | Output |
|-------|---------|-------|--------|
| `sales-prospect` | Full audit — 5 parallel agents | URL | PROSPECT-ANALYSIS.md |
| `sales-research` | Company research & firmographics | URL | COMPANY-RESEARCH.md |
| `sales-qualify` | Lead qualification (BANT/MEDDIC) | URL | LEAD-QUALIFICATION.md |
| `sales-contacts` | Decision maker identification | URL | DECISION-MAKERS.md |
| `sales-outreach` | Cold outreach email sequence | Company name | OUTREACH-SEQUENCE.md |
| `sales-followup` | Follow-up email sequence | Company name | FOLLOWUP-SEQUENCE.md |
| `sales-prep` | Meeting preparation brief | URL | MEETING-PREP.md |
| `sales-proposal` | Client proposal generator | Client name | CLIENT-PROPOSAL.md |
| `sales-objections` | Objection handling playbook | Topic/industry | OBJECTION-PLAYBOOK.md |
| `sales-icp` | Ideal Customer Profile builder | Description | IDEAL-CUSTOMER-PROFILE.md |
| `sales-competitors` | Competitive intelligence | URL | COMPETITIVE-INTEL.md |
| `sales-brief` | Stakeholder briefing generator | Stakeholder type | STAKEHOLDER-BRIEF-*.md |
| `sales-report` | Pipeline report (Markdown) | — | SALES-REPORT.md |
| `sales-report-pdf` | Pipeline report (PDF) | — | SALES-REPORT-*.pdf |

---

## Quick Start

### Method 1: Use Orchestrator

Tell the orchestrator what you want to do:

```
Research Stripe for me → invokes sales-research
Find decision makers at Acme → invokes sales-contacts
Prepare for a meeting with Notion → invokes sales-prep
Handle SaaS pricing objections → invokes sales-objections
```

### Method 2: Use Individual Skills Directly

```python
# Via task() with load_skills
task(
    category="unspecified-high",
    load_skills=["sales-research"],
    prompt="Research https://stripe.com",
    run_in_background=False
)
```

---

## Command Reference

### Full Prospect Analysis
```
Input: URL (e.g., "https://stripe.com")
Output: PROSPECT-ANALYSIS.md
Score: 0-100 with grade (A+ to D)

The flagship command. Runs 5 parallel agents:
- Company Research (25% weight)
- Contact Discovery (20% weight)
- Opportunity Scoring (20% weight)
- Competitive Intel (15% weight)
- Outreach Strategy (20% weight)
```

### Company Research
```
Input: URL (e.g., "https://stripe.com")
Output: COMPANY-RESEARCH.md
Score: Company Fit 0-100

8 research dimensions:
1. Company Overview
2. Business Model & Revenue
3. Product & Technology
4. Leadership & Team
5. Funding & Financial Health
6. Market Position
7. Culture & Employer Brand
8. Recent Developments
```

### Lead Qualification
```
Input: URL (e.g., "https://stripe.com")
Output: LEAD-QUALIFICATION.md
Score: BANT 0-100, MEDDIC %

BANT Framework:
- Budget (0-25)
- Authority (0-25)
- Need (0-25)
- Timeline (0-25)

MEDDIC: Metrics, Economic Buyer, Decision Criteria, Decision Process, Identify Pain, Champion
```

### Contact Discovery
```
Input: URL (e.g., "https://stripe.com")
Output: DECISION-MAKERS.md

Finds:
- C-suite executives
- VP/Director level
- Key managers
- Board members
- Advisory connections
```

### Outreach Generation
```
Input: Company name (e.g., "Linear")
Output: OUTREACH-SEQUENCE.md

Generates:
- 5-email cold sequence
- Personalized hooks
- Multi-channel approach
- Follow-up cadence
```

### Meeting Preparation
```
Input: URL (e.g., "https://stripe.com")
Output: MEETING-PREP.md

Creates:
- Attendee profiles
- Talking points
- Discovery questions
- Objection responses
- Cheat sheet
```

### Objection Handling
```
Input: Topic or industry (e.g., "SaaS pricing")
Output: OBJECTION-PLAYBOOK.md

15 universal objections + industry-specific:
- Pricing / Budget
- Timing / Urgency
- Competition
- Authority
- Need / Fit
- Security / Compliance
- Technical concerns
```

### Competitive Intelligence
```
Input: URL (e.g., "https://stripe.com")
Output: COMPETITIVE-INTEL.md

Maps:
- Direct competitors
- Alternative solutions
- Switching costs
- Competitive advantages
- Win/loss factors
```

### Ideal Customer Profile
```
Input: Description (e.g., "B2B SaaS, 50-200 employees")
Output: IDEAL-CUSTOMER-PROFILE.md

Defines:
- Firmographic criteria
- Behavioral indicators
- Pain points
- Buying triggers
- Ideal customer journey
```

### Pipeline Reports
```
Input: None (reads existing analysis files)
Output: SALES-REPORT.md or SALES-REPORT-*.pdf

Compiles:
- All prospect analyses
- Pipeline summary
- Next actions
- Priority ranking
```

---

## Scoring Methodology

### Prospect Score (0-100)

| Category | Weight | What It Measures |
|----------|--------|------------------|
| Company Fit | 25% | Size, industry, growth, tech stack, budget signals |
| Contact Access | 20% | Decision makers identified, contact info, warm paths |
| Opportunity Quality | 20% | Pain points, timing, budget, urgency signals |
| Competitive Position | 15% | Current solutions, switching costs, gaps exploitable |
| Outreach Readiness | 20% | Personalization anchors, channel strategy, messaging |

### Grade Interpretation

| Score | Grade | Meaning |
|-------|-------|---------|
| 90-100 | A+ | Hot Lead — prioritize immediately |
| 75-89 | A | Strong Prospect — worth significant investment |
| 60-74 | B | Qualified Lead — pursue with standard approach |
| 40-59 | C | Lukewarm — nurture, don't hard sell |
| 0-39 | D | Poor Fit — deprioritize or disqualify |

---

## Business Context Detection

Automatically detect company type and adjust analysis:

- **SaaS/Software** → Tech stack, ARR, product-led growth
- **Agency/Services** → Client roster, case studies, team size
- **E-commerce** → Product catalog, traffic, revenue estimates
- **Enterprise** → Org structure, procurement, compliance
- **SMB** → Owner-operator signals, budget constraints
- **Startup** → Funding stage, burn rate, growth trajectory

---

## Output Standards

All outputs follow these rules:
1. **Actionable** — Every recommendation is specific enough to execute
2. **Personalized** — Generic advice is worthless in sales
3. **Evidence-based** — Cite specific sources for every claim
4. **Ready to use** — Emails are copy-paste ready

---

## Cross-Skill Integration

Skills build on each other's output:

```
sales-prospect → PROSPECT-ANALYSIS.md
                      ↓
sales-outreach ← uses contacts + research data
sales-prep ← uses all prior analysis
sales-proposal ← uses qualification + competitive intel
sales-report ← compiles all analyses
```

---

## Usage Examples

### Research a company
```
"Research https://stripe.com for enterprise sales"
→ Uses sales-research skill
→ Outputs COMPANY-RESEARCH.md
```

### Find decision makers
```
"Who are the decision makers at https://notion.so?"
→ Uses sales-contacts skill
→ Outputs DECISION-MAKERS.md
```

### Full prospect audit
```
"Do a full analysis of https://acme.com"
→ Uses sales-prospect skill (5 parallel agents)
→ Outputs PROSPECT-ANALYSIS.md with score
```

### Generate outreach
```
"Write cold outreach for Linear"
→ Uses sales-outreach skill
→ Outputs OUTREACH-SEQUENCE.md
```

### Prepare for meeting
```
"Prepare for a meeting with Datadog"
→ Uses sales-prep skill
→ Outputs MEETING-PREP.md
```

### Handle objections
```
"Help me handle objections about enterprise pricing"
→ Uses sales-objections skill
→ Outputs OBJECTION-PLAYBOOK.md
```

---

## File Outputs

All outputs saved to current directory:
- PROSPECT-ANALYSIS.md
- COMPANY-RESEARCH.md
- LEAD-QUALIFICATION.md
- DECISION-MAKERS.md
- OUTREACH-SEQUENCE.md
- FOLLOWUP-SEQUENCE.md
- MEETING-PREP.md
- CLIENT-PROPOSAL.md
- OBJECTION-PLAYBOOK.md
- IDEAL-CUSTOMER-PROFILE.md
- COMPETITIVE-INTEL.md
- SALES-REPORT.md
- SALES-REPORT-*.pdf
