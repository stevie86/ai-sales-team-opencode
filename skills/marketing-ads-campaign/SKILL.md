---
name: marketing-ads-campaign
description: Create comprehensive multi-channel ad campaigns for Google Ads, Meta, TikTok, and LinkedIn. Use when the user wants to create a new ad campaign, optimize existing campaigns, or develop campaign strategy for a specific product or target audience.
allowed-tools:
  - WebSearch
  - WebFetch
  - Grep
  - Read
  - Glob
  - Write
  - Bash
---

# Multi-Channel Ad Campaign Creator

Create comprehensive, best-practice ad campaigns across Google Ads, Meta (Facebook/Instagram), TikTok, and LinkedIn. This skill produces ready-to-implement campaign structures, keyword lists, ad copy, audience targeting, and budget allocation.

## When to Use

- Create a new multi-channel ad campaign from scratch
- Optimize an existing campaign structure
- Develop campaign strategy for a new product launch
- Audit current campaigns and provide optimization recommendations
- Expand campaigns to new channels (e.g., adding Meta to existing Google Ads)

## Process

### Step 1: Gather Campaign Inputs

Collect from user:

1. **Product/Service** — What are we advertising?
2. **Target Audience** — Who is the ideal customer? (demographics, interests, behaviors)
3. **Geographic targeting** — Which countries/regions?
4. **Campaign goal** — Brand awareness, lead generation, conversions, retargeting?
5. **Budget** — Monthly or total budget
6. **Timeline** — Campaign duration, key dates
7. **Existing channels** — What platforms are already running?
8. **Competitors** — Who are they competing against?

### Step 2: Research Best Practices

For each channel, research current best practices:

**Google Ads:**
- Keyword match types and strategies
- Smart bidding strategies (Maximize Conversions, Target CPA, Target ROAS)
- Responsive search ads best practices
- Performance Max setup
- Display/retargeting strategies

**Meta (Facebook/Instagram):**
- Audience targeting options (interest, lookalike, custom audiences)
- Creative best practices (carousel, video, collection ads)
- Campaign objective selection
- Placement optimization

**TikTok:**
- Ad formats (Spark Ads, In-Feed, TopView)
- Creative specifications
- Audience targeting differences from Meta/Google

**LinkedIn:**
- Campaign Manager targeting (job titles, company sizes, industries)
- Lead Gen Forms
- Sponsored Content vs Message Ads

### Step 3: Build Campaign Architecture

Create a structured campaign hierarchy:

```
Account
└── Campaign 1 (Google Search)
    └── Ad Group 1A: [Keyword Theme]
        └── Ads: Responsive Search Ad
    └── Ad Group 1B: [Keyword Theme]
└── Campaign 2 (Google Display)
    └── Ad Group: [Remarketing]
└── Campaign 3 (Meta)
    └── Ad Set: [Custom Audience]
        └── Ads: Carousel + Single Image
└── Campaign 4 (LinkedIn)
    └── Ad Group: [Targeting]
        └── Ads: Sponsored Content
```

### Step 4: Keyword Strategy (Google)

Build comprehensive keyword lists:

| Match Type | Use Case | Example |
|------------|----------|---------|
| Exact | High intent, precise targeting | [buy running shoes] |
| Phrase | Middle-funnel consideration | "best running shoes for" |
| Broad | Brand awareness (use with negatives) | running shoes |

Include:
- Product keywords
- Problem keywords
- Comparison keywords
- Category keywords
- Competitor keywords (if appropriate)

### Step 5: Audience Strategy (Non-Search)

For Meta, TikTok, LinkedIn:

**Custom Audiences:**
- Website visitors (pixel/data)
- Customer lists (CRM)
- Engagement audiences

**Lookalike/Similar Audiences:**
- Source from converters
- 1-10% similarity

**Interest Targeting:**
- Core interests relevant to product
- Behaviors and demographics

### Step 6: Ad Creative Development

Generate ad copy variations for each channel:

**Google Ads Responsive Search Ads:**
- 15 headlines (up to 30 characters each)
- 4 descriptions (up to 90 characters each)
- Ensure keyword insertion where appropriate
- Include CTA in descriptions

**Meta Ads:**
- Primary text (125 characters)
- Headline (40 characters)
- Description (30 characters)
- Multiple image/video variations

**LinkedIn Ads:**
- Introductory text
- Headline
- Description
- CTA button selection

### Step 7: Budget Allocation

Recommend budget split across channels:

| Channel | % of Budget | Rationale |
|---------|-------------|-----------|
| Google Search | 40-50% | High intent capture |
| Google Display/PMax | 15-20% | Retargeting, awareness |
| Meta | 20-25% | Audience building, retargeting |
| LinkedIn (B2B) | 10-15% | If B2B targeting needed |

### Step 8: Tracking & Measurement

Ensure proper conversion tracking setup:

- Google Ads conversion tracking
- Meta pixel / CAPI
- LinkedIn Insight Tag
- UTM parameter strategy
- Cross-channel attribution approach

### Step 9: Optimization Recommendations

Provide ongoing optimization guidance:

- Bid strategy adjustments
- Creative rotation rules
- Audience refinement
- Keyword expansion/negative building
- A/B testing roadmap

## Output Format

Generate a comprehensive campaign document:

```markdown
# Multi-Channel Ad Campaign Strategy

**Product:** [Name]
**Target Audience:** [Description]
**Total Budget:** [Amount]
**Duration:** [Timeline]
**Created:** [Date]

---

## Executive Summary

[Brief overview of the campaign strategy]

---

## Campaign Architecture

### Google Ads

#### Campaign 1: [Name]
**Objective:** [Goal]
**Bid Strategy:** [Strategy]

**Ad Groups:**
| Ad Group | Keywords | Bids |
|----------|----------|------|
| [Theme 1] | [keywords] | $X.XX |
| [Theme 2] | [keywords] | $X.XX |

**Ads:**
[Responsive Search Ad copy]

#### Campaign 2: [Name]
...

### Meta (Facebook/Instagram)

#### Campaign: [Name]
**Objective:** [Goal]

**Audiences:**
| Audience | Type | Targeting |
|----------|------|-----------|
| [Name] | Custom | [source] |

**Ad Variations:**
[Creative specs]

### TikTok

[Campaign structure]

### LinkedIn

[Campaign structure]

---

## Budget Allocation

| Channel | Budget | % |
|--------|--------|---|
| Google Search | $X,XXX | XX% |
| Google Display | $X,XXX | XX% |
| Meta | $X,XXX | XX% |
| LinkedIn | $X,XXX | XX% |

---

## Creative Assets Required

| Channel | Asset | Specs |
|--------|-------|-------|
| Google | Responsive Search Ad | 15 headlines, 4 descriptions |
| Meta | Carousel | 2-10 cards, 1080x1080 |
| LinkedIn | Sponsored Content | 1200x627 |

---

## Tracking Plan

- Google Ads conversions: [list]
- Meta conversions: [list]
- UTM structure: [format]

---

## Optimization Roadmap

### Week 1-2
- Review initial performance
- Pause underperforming ads
- Adjust bids based on early data

### Week 3-4
- Expand winning audiences
- Test new creative variations
- Build negative keyword list

### Ongoing
- [Additional optimization tasks]
```

## Rules

- Always research current best practices before creating campaigns — ad platform features change frequently
- Ensure proper negative keyword lists to prevent wasted spend
- Match ad copy to landing pages (message match)
- Include proper tracking from day one
- Consider the full funnel — awareness + consideration + conversion
- Budget realistically for meaningful data collection
- Always include retargeting/remarketing audiences
