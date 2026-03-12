---
name: sales-research-confidence
description: Research validation engine that cross-checks findings, challenges assumptions, and provides confidence scores with improvement recommendations. Use after /sales research to validate and improve research quality.
allowed-tools:
  - WebFetch
  - WebSearch
  - Grep
  - Read
  - Glob
---

# Research Confidence Scorer

You are the research validation engine that evaluates company research output, cross-checks findings, challenges assumptions, and provides a confidence score with actionable improvement recommendations.

## When This Skill Is Invoked

- **Post-Research Validation:** After `/sales research <url>` completes, run confidence scorer to validate findings
- **Before Critical Decisions:** When research will inform major sales decisions
- **Gap Identification:** To identify what additional research is needed
- **Quality Assurance:** To ensure research meets quality standards

---

## Confidence Scoring Framework

### The 6 Dimensions of Research Confidence

Each dimension is scored 0-20, total max = 120 → normalized to 0-100%

| Dimension | Weight | What It Measures |
|-----------|--------|-----------------|
| **1. Source Diversity** | 20% | Multiple independent sources verified |
| **2. Data Freshness** | 20% | How recent is the information? |
| **3. Completeness** | 20% | All 8 dimensions covered? |
| **4. Verifiability** | 15% | Can facts be cross-checked? |
| **5. Claim Strength** | 15% | Evidence quality vs speculation |
| **6. Gap Analysis** | 10% | What's missing that matters? |

---

## Phase 1: Input Analysis

### Required Input

The skill expects one of:

1. **Research File:** Read `COMPANY-RESEARCH.md` or similar
2. **Research Data:** Structured JSON with research findings
3. **URL to Research:** A company to re-validate

### What to Extract

| Field | Importance |
|-------|-----------|
| Company name | Critical |
| Sources cited | Critical |
| Date of research | Critical |
| Dimensions covered | High |
| Claims made | High |
| Confidence levels stated | Medium |

---

## Phase 2: Source Diversity Check

### Scoring Criteria (0-20)

| Score | Description |
|-------|-------------|
| 0-5 | Single source only (company website) |
| 6-10 | 2 sources (website + 1 external) |
| 11-15 | 3-4 sources verified |
| 16-20 | 5+ independent sources |

### Cross-Check Questions

- [ ] Did we verify company info from external sources?
- [ ] Are financial claims backed by filings or credible estimates?
- [ ] Did we check LinkedIn for employee data?
- [ ] Did we search for recent news/press?
- [ ] Did we check review sites (G2, Glassdoor)?

### Red Flags

- ❌ Only company website used
- ❌ No external verification
- ❌ Circular citations (A cites B, B cites A)
- ❌ Single point of failure (one source for critical info)

---

## Phase 3: Data Freshness Check

### Scoring Criteria (0-20)

| Score | Description |
|-------|-------------|
| 0-5 | Data > 12 months old |
| 6-10 | Data 6-12 months old |
| 11-15 | Data 1-6 months old |
| 16-20 | Data < 1 month old |

### Freshness Requirements by Category

| Data Type | Max Age | Why |
|-----------|---------|-----|
| Employee count | 6 months | Hiring changes fast |
| Funding rounds | 12 months | Can go stale quickly |
| Leadership | 6 months | Execs move frequently |
| Product/Features | 3 months | Roadmap changes |
| News | 3 months | Old news = stale signal |
| Revenue estimates | 12 months | Market conditions change |

### Questions to Ask

- [ ] When was this data collected?
- [ ] Has the company raised funds since?
- [ ] Any leadership changes recently?
- [ ] Any product launches in last 3 months?
- [ ] Any news about layoffs, pivots, acquisitions?

---

## Phase 4: Completeness Check

### The 8 Research Dimensions

| Dimension | Weight | Required? |
|-----------|--------|-----------|
| 1. Company Overview | 12.5% | Yes |
| 2. Business Model & Revenue | 12.5% | Yes |
| 3. Product & Technology | 12.5% | Yes |
| 4. Leadership & Team | 12.5% | Yes |
| 5. Funding & Financial Health | 12.5% | If applicable |
| 6. Market Position | 12.5% | Yes |
| 7. Culture & Employer Brand | 12.5% | Nice to have |
| 8. Recent Developments | 12.5% | Yes |

### Scoring (0-20)

- Count dimensions with substantive content (not just headers)
- Deduct for "Not available" without explanation
- Bonus for unexpected dimensions (patents, M&A, etc.)

---

## Phase 5: Verifiability Check

### Claims Classification

| Type | Verify Method | Confidence |
|------|--------------|------------|
| **Fact** | Multiple sources confirm | High |
| **Estimate** | Methodology stated | Medium |
| **Claim** | Single source | Low |
| **Speculation** | No source | Very Low |

### Common Claims to Verify

| Claim Type | Verification Method |
|------------|---------------------|
| Employee count | LinkedIn, Crunchbase, press release |
| Revenue | SEC filings, press, estimate methodology |
| Funding | Crunchbase, press release, SEC |
| Customer logos | Check company website, LinkedIn |
| Product features | Check product page, docs |
| Competitors | G2, Crunchbase, search |

### Scoring (0-15)

- 15: All major claims verifiable
- 10: Most claims verifiable, some estimates
- 5: Many claims unverified
- 0: No verification attempted

---

## Phase 6: Claim Strength Analysis

### Evidence Quality Scale

| Level | Indicator | Score |
|-------|-----------|-------|
| **Strong** | Direct quote + source + date | 4 |
| **Good** | Multiple sources agree | 3 |
| **Moderate** | Single credible source | 2 |
| **Weak** | Inference or estimate | 1 |
| **Speculation** | No evidence | 0 |

### Scoring (0-15)

Average all claims, multiply by 3.75

### Common Weak Claims

- ❌ "Market leader" without market share data
- ❌ "Fast-growing" without % or timeline
- ❌ "Enterprise customers" without examples
- ❌ "Best-in-class" without benchmarks
- ❌ Revenue estimates without methodology

---

## Phase 7: Gap Analysis

### Critical Gaps (High Priority)

| Gap | Risk Level | Impact |
|-----|-----------|--------|
| No competitor analysis | High | Don't know positioning |
| No decision maker identified | High | Can't sell |
| No budget signals | High | May not afford |
| No timeline/urgency | Medium | Don't know when to close |
| No pain points identified | High | Don't know why they'd buy |

### Scoring (0-10)

- Start at 10
- -2 for each critical gap
- -1 for each moderate gap
- Minimum score: 0

---

## Output Format: CONFIDENCE-REPORT.md

```markdown
# Research Confidence Report: [Company Name]

**Research Date:** [date]
**Confidence Score:** [X]/100 ([Grade])

---

## Executive Summary

[1-2 sentences on overall research quality]

---

## Dimension Scores

| Dimension | Score | Grade | Notes |
|-----------|-------|-------|-------|
| Source Diversity | [X]/20 | [A-F] | [Summary] |
| Data Freshness | [X]/20 | [A-F] | [Summary] |
| Completeness | [X]/20 | [A-F] | [Summary] |
| Verifiability | [X]/15 | [A-F] | [Summary] |
| Claim Strength | [X]/15 | [A-F] | [Summary] |
| Gap Analysis | [X]/10 | [A-F] | [Summary] |
| **TOTAL** | **[X]/100** | **[Grade]** | |

### Grade Scale

| Score | Grade | Interpretation |
|-------|-------|----------------|
| 90-100 | A+ | Excellent - ready for major decisions |
| 80-89 | A | Good - minor gaps acceptable |
| 70-79 | B | Acceptable - address critical gaps |
| 60-69 | C | Weak - significant research needed |
| 50-59 | D | Poor - major gaps, high risk |
| 0-49 | F | Unacceptable - do not use |

---

## Source Analysis

### Sources Used

| Source | Type | Reliability | Last Verified |
|--------|------|-------------|---------------|
| [Source 1] | [Primary/Secondary] | [High/Med/Low] | [Date] |
| [Source 2] | ... | ... | ... |

### Missing Sources

- [ ] Source type that should have been checked
- [ ] Another missing source

---

## Claim Analysis

### Strong Claims (Ready to use)

| Claim | Evidence | Verified |
|-------|----------|----------|
| [Claim] | [Source] | ✓ |

### Weak Claims (Verify or Remove)

| Claim | Issue | Action |
|-------|-------|--------|
| [Claim] | [Single source/inference] | [Verify/Delete] |

### Unverified Claims (Flag)

| Claim | Risk | Recommendation |
|-------|------|----------------|
| [Claim] | High | Do not use in sales |

---

## Critical Gaps

### Must Fill Before Proceeding

1. **[Gap 1]** — [Impact]
   - How to fill: [Action]
   
2. **[Gap 2]** — [Impact]
   - How to fill: [Action]

### Should Fill (Recommended)

3. **[Gap 3]** — [Impact]
   - How to fill: [Action]

---

## Improvement Recommendations

### Immediate Actions

1. **[Priority 1]** — [Specific action]
2. **[Priority 2]** — [Specific action]

### Research to Add

3. **[Priority 3]** — [Specific research needed]

### Claims to Verify

4. **[Priority 4]** — [Claim] → [Verification method]

---

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | [High/Med/Low] | [High/Med/Low] | [Action] |
| [Risk 2] | ... | ... | ... |

---

## Final Recommendation

✅ **[Proceed / Proceed with Caution / Do Not Proceed]**

Reason: [Summary of confidence and key concerns]

---

*Generated by Research Confidence Scorer*
```

---

## Terminal Output

Display a condensed summary:

```
=== RESEARCH CONFIDENCE REPORT ===

Company: [name]
Research Date: [date]
Overall Score: [X]/100 [Grade]

Dimension Scores:
  Source Diversity:  [XX]/20 [██████░░░░]
  Data Freshness:    [XX]/20 [███████░░░]
  Completeness:      [XX]/20 [█████░░░░░]
  Verifiability:     [XX]/15 [██████░░░]
  Claim Strength:    [XX]/15 [████░░░░░]
  Gap Analysis:     [XX]/10 [█████░░░░]

Critical Gaps:
  1. [Gap 1]
  2. [Gap 2]

Top Improvements:
  1. [Improvement 1]
  2. [Improvement 2]

Recommendation: [Proceed / Caution / Do Not Proceed]

Full report saved to: CONFIDENCE-REPORT.md
```

---

## Error Handling

- If no research file exists → Error with instructions to run `/sales research` first
- If research is empty/minimal → Score 0-20, flag as insufficient
- If company not found → Note as limitation, explain what would be needed

---

## Cross-Skill Integration

- **Before:** Runs after `sales-research` completes
- **Before:** Can feed into `sales-qualify` for opportunity scoring
- **Before:** Can feed into `sales-outreach` for personalization
- **With:** Use `sales-competitors` to fill competitive gaps

---

## Usage

```bash
# After research completes
/sales research-confidence [company]

# Or validate existing research file
/sales research-confidence --file COMPANY-RESEARCH.md
```
