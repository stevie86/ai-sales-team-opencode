# Stakeholder Briefing Generator

> **OpenCode Usage:** `task(load_skills=["sales-brief"], prompt="<your request>")`

Generate personalized product briefings for any stakeholder — investors, advisors, developers, partners, employees, board members, etc.

---

## Dynamic Product Context

This skill loads your product info from `PRODUCT-BRIEF.md` to create accurate briefings.

### Quick Setup (if not done)

```bash
cp PRODUCT-BRIEF-TEMPLATE.md PRODUCT-BRIEF.md
vim PRODUCT-BRIEF.md
```

---

## What This Skill Does

Generate comprehensive, stakeholder-specific briefings that make anyone immediately up-to-speed on your product.

### Supported Stakeholders

| Stakeholder | Description | Focus Areas |
|-------------|-------------|-------------|
| **Investor/VC** | Funding conversations | Traction, market size, ROI, growth |
| **Advisor** | Strategic guidance | Market position, challenges, opportunities |
| **Developer** | Technical integration | API, docs, architecture, SDKs |
| **Partner** | Business collaboration | Integration, mutual value, technical requirements |
| **Employee** | Onboarding/training | Features, value prop, customer stories |
| **Board** | Governance updates | KPIs, strategic progress, risks |
| **Customer** | Upsell/renewal | ROI, case studies, new features |
| **Prospect** | Sales support | Problem/solution, proof points |

---

## How to Use

### Basic Usage

```bash
# Generate a briefing
task(load_skills=["sales-brief"], prompt="Generate investor briefing for our seed round")
```

### Detailed Usage

```bash
# With specific context
task(load_skills=["sales-brief"], prompt="Create a technical briefing for a potential developer partner integrating with our API")
```

---

## Input Format

The skill accepts:

1. **Stakeholder type:** "investor", "advisor", "developer", "partner", "employee", "board", "customer",2. **Context "prospect"
/Purpose:** Why you're briefing them (fundraising, partnership, onboarding, etc.)
3. **Depth:** Quick overview vs. deep dive
4. **Your product info:** Loaded from PRODUCT-BRIEF.md

---

## Output Format: STAKEHOLDER-BRIEF.md

Each briefing includes:

```
# [Stakeholder] Briefing: [Product Name]

## Overview
[2-3 sentence summary for this stakeholder]

## About [Product]
[Product description tailored to stakeholder]

## Why It Matters to You
[Stakeholder-specific value]

## [Stakeholder-Specific Sections]
[See below for what each type gets]

## Key Talking Points
[3-5 bullets they're most interested in]

## Questions to Ask
[Helpful questions for engagement]

## Next Steps
[Suggested follow-up actions]
```

---

## Stakeholder-Specific Content

### Investor/VC Briefing
- Market opportunity & TAM
- Traction & metrics
- Growth rate & trajectory
- Competitive moat
- Funding ask & use of funds
- Team & background
- Exit potential

### Advisor Briefing
- Strategic challenges
- Market opportunities
- Competitive landscape
- Recommended actions
- Key decisions needed
- Resources needed

### Developer Briefing
- API documentation summary
- Authentication & auth
- Key endpoints/abilities
- SDKs & libraries
- Integration examples
- Rate limits & pricing
- Support channels
- Code samples

### Partner Briefing
- Partnership value proposition
- Integration requirements
- Revenue sharing model
- Mutual benefits
- Go-to-market plan
- Technical requirements

### Employee Briefing
- Product features & roadmap
- Target customer
- Value proposition
- Customer success stories
- Competitive advantages
- How to demo
- Common objections

### Board Briefing
- KPI dashboard
- Strategic progress
- Risks & mitigations
- Resource needs
- Key decisions
- Market context

### Customer Briefing
- ROI & results achieved
- Feature updates
- Case studies
- Expansion opportunities
- Support resources
- Success metrics

---

## Customization

### Adjust for Your Audience

The skill will tailor:
- **Tone:** Technical for devs, high-level for execs
- **Depth:** Overview vs. detailed
- **Focus:** What's relevant to THAT stakeholder
- **Language:** Jargon appropriate to audience

### Example Prompts

```
"Generate a 5-minute investor pitch deck for our Series A"
"Create a technical deep-dive for a developer evaluating our API"
"Build an onboarding brief for new sales hires"
"Prepare a board meeting update on product progress"
"Generate a partner one-pager for co-marketing"
```

---

## File Output

Save as: `STAKEHOLDER-BRIEF-[TYPE].md`

Examples:
- `STAKEHOLDER-BRIEF-INVESTOR.md`
- `STAKEHOLDER-BRIEF-DEVELOPER.md`
- `STAKEHOLDER-BRIEF-PARTNER.md`

---

## Tips

1. **Be specific about stakeholder type** — More targeted output
2. **Mention the purpose** — "for our board meeting" or "to close this deal"
3. **Specify depth** — "quick overview" vs. "30-minute deep dive"
4. **Update PRODUCT-BRIEF.md** — More accurate briefings

---

## Related Skills

- Use `sales-competitors` for competitive positioning in investor briefs
- Use `sales-proposal` for formal partnership proposals
- Use `sales-outreach` for initial partner outreach
