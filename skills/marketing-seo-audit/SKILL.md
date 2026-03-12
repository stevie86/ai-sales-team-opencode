---
name: marketing-seo-audit
description: Perform comprehensive SEO audits including technical SEO, on-page optimization, content analysis, and competitor keyword research. Use when the user wants to audit a website's SEO, research keywords for a niche, or analyze competitor search presence.
allowed-tools:
  - WebSearch
  - WebFetch
  - Grep
  - Read
  - Glob
  - Bash
  - Write
---

# SEO Audit & Research Tool

Perform comprehensive SEO audits and keyword research for any website. Covers technical SEO, on-page factors, content analysis, and competitive keyword mapping.

## When to Use

- Audit an existing website's SEO health
- Research keywords for a new product or niche
- Analyze competitor organic search presence
- Identify SEO opportunities and gaps
- Create SEO strategy recommendations

## Process

### Phase 1: Technical SEO Audit

Check technical foundations:

| Factor | What to Check | Tools/Methods |
|--------|---------------|--------------|
| **Site Speed** | Core Web Vitals (LCP, FID, CLS) | PageSpeed Insights, Chrome DevTools |
| **Mobile** | Mobile-friendly, responsive | Google Mobile-Friendly Test |
| **Crawlability** | robots.txt, sitemap.xml | Fetch as Google, sitemap analysis |
| **HTTPS** | SSL certificate | Browser check |
| **Indexation** | Pages indexed vs. pages existing | site: search |
| **Structured Data** | JSON-LD, Schema.org | HTML source inspection |
| **Core Web Vitals** | Real user metrics | PageSpeed Insights, CrUX |

### Phase 2: On-Page SEO Analysis

Evaluate on-page elements:

| Element | Checklist |
|---------|-----------|
| **Title Tags** | Unique, under 60 chars, keyword placement |
| **Meta Descriptions** | Unique, under 155 chars, CTA |
| **H1** | One per page, includes target keyword |
| **H2-H6** | Proper hierarchy, keyword inclusion |
| **URL Structure** | Clean, readable, includes keyword |
| **Internal Linking** | Logical site architecture |
| **Image Alt Text** | Descriptive, keyword where relevant |
| **Content Length** | Sufficient depth for target keywords |

### Phase 3: Keyword Research

Expand seed keywords into strategy:

**Keyword Cluster Approach:**
```
Seed: "project management software"

├── Transactional
│   ├── buy project management software
│   ├── project management software pricing
│   └── best project management software
├── Informational
│   ├── how to manage projects
│   ├── project management methods
│   └── agile vs waterfall
├── Navigational
│   ├── asana alternative
│   ├── monday.com vs trello
│   └── clickup review
```

**Research Methods:**
1. Google Autocomplete
2. People Also Ask
3. Related Searches
4. Keyword Planner
5. Competitor analysis
6. Forum/Reddit research

### Phase 4: Competitor Keyword Analysis

Map competitor organic presence:

1. Identify 3-5 direct competitors
2. Analyze their top ranking pages
3. Identify keyword gaps (keywords they rank for that you don't)
4. Find content opportunities
5. Assess content depth and quality

### Phase 5: Content Audit (for existing sites)

| Metric | What to Measure |
|--------|-----------------|
| **Content Gaps** | Topics covered by competitors but not you |
| **Content Quality** | Depth, freshness, E-E-A-T signals |
| **Thin Content** | Pages under 300 words |
| **Duplicate Content** | Copyscape checks |
| **Orphan Pages** | No internal links |

### Phase 6: Link Building Assessment

| Factor | Evaluation |
|--------|------------|
| **Domain Authority** | Moz, Ahrefs, or SEMrush metrics |
| **Backlink Count** | Total referring domains |
| **Link Quality** | Domain diversity, authority scores |
| **Anchor Text** | Branded vs. exact match vs. natural |
| **Competitor Links** | Where competitors earn links |

## Output Format

```markdown
# SEO Audit Report: [Website]

**Audit Date:** [Date]
**Overall Health Score:** [X/100]

---

## Executive Summary

[Key findings and priority actions]

---

## Technical SEO (Score: X/30)

| Factor | Status | Issue | Recommendation |
|--------|--------|-------|----------------|
| Site Speed | ✅/⚠️/❌ | [issue] | [fix] |
| Mobile | ✅/⚠️/❌ | [issue] | [fix] |
| Crawlability | ✅/⚠️/❌ | [issue] | [fix] |
| HTTPS | ✅/⚠️/❌ | [issue] | [fix] |
| Indexation | ✅/⚠️/❌ | [issue] | [fix] |
| Structured Data | ✅/⚠️/❌ | [issue] | [fix] |

## On-Page SEO (Score: X/25)

| Element | Status | Issue | Recommendation |
|---------|--------|-------|----------------|
| Title Tags | ✅/⚠️/❌ | [issue] | [fix] |
| Meta Descriptions | ✅/⚠️/❌ | [issue] | [fix] |
| H1 | ✅/⚠️/❌ | [issue] | [fix] |
| Internal Links | ✅/⚠️/❌ | [issue] | [fix] |

## Keyword Strategy (Score: X/25)

### Target Keyword Clusters

| Cluster | Primary Keyword | Search Intent | Priority |
|---------|----------------|---------------|----------|
| [Name] | [keyword] | [type] | High/Med/Low |

### Content Opportunities

| Topic | Keyword Gap | Est. Volume | Priority |
|-------|------------|-------------|----------|
| [Topic] | [competitor] | [volume] | High |

## Competitor Analysis (Score: X/20)

### Competitor Keyword Overlap

| Keyword | You | Comp A | Comp B | Opportunity |
|---------|-----|--------|--------|-------------|
| [kw] | ❌ | ✅ | ✅ | High |

---

## Priority Action Items

### Immediate (Week 1-2)
1. [Action] - [Impact]
2. [Action] - [Impact]

### Short-term (Month 1)
1. [Action] - [Impact]
2. [Action] - [Impact]

### Long-term (Month 2-3)
1. [Action] - [Impact]
2. [Action] - [Impact]

---

## Estimated Impact

| Action | Potential Traffic Gain | Difficulty |
|--------|----------------------|------------|
| [Fix title tags] | +X% | Easy |
| [New content] | +X% | Medium |
```

## Best Practices

- Use Google's official tools (Search Console, PageSpeed Insights, Mobile-Friendly Test)
- Check multiple data sources for keyword volume — don't rely on one tool
- Prioritize user intent over keyword volume
- E-E-A-T signals matter: expertise, experience, authoritativeness, trustworthiness
- Core Web Vitals are ranking factors — optimize for real user experience
- Content depth beats content quantity — one comprehensive page beats 10 thin ones
