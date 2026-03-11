# Product Context Loader

> Dynamic product briefing system for AI Sales Team skills.

This layer loads your product/company information dynamically, so you don't need to hardcode anything in skills.

---

## How It Works

1. **Create your product brief** — Copy `PRODUCT-BRIEF-TEMPLATE.md` to `PRODUCT-BRIEF.md`
2. **Fill in your details** — Edit the file with your product info
3. **Skills auto-load** — All sales skills read this file when generating content

---

## File Hierarchy

```
PROJECT/
├── PRODUCT-BRIEF.md          ← Your product info (git-ignored)
├── PRODUCT-BRIEF-TEMPLATE.md ← Template to copy from
├── .gitignore                 ← Ignores PRODUCT-BRIEF.md
├── .opencode/
│   └── skills/
│       └── (sales skills read PRODUCT-BRIEF.md)
```

---

## How Skills Use This

Each skill checks for these files in order:

1. `./PRODUCT-BRIEF.md` (current directory)
2. `../PRODUCT-BRIEF.md` (parent directory)
3. `../../PRODUCT-BRIEF.md` (grandparent)

If found, the skill loads:
- Product name & description
- ICP (Ideal Customer Profile)
- Pain points
- Proof points
- Competitive differentiators
- Outreach hooks

---

## Quick Setup

```bash
# 1. Copy the template
cp PRODUCT-BRIEF-TEMPLATE.md PRODUCT-BRIEF.md

# 2. Edit your product info
vim PRODUCT-BRIEF.md

# 3. Generate outreach
# The skill now knows your product!
```

---

## Supported Skills

These skills auto-load product context:

- `sales-outreach` — Uses product for email personalization
- `sales-qualify` — Uses ICP for lead scoring
- `sales-prep` — Uses product for meeting prep
- `sales-proposal` — Uses product for proposals
- `sales-objections` — Uses pain points for responses
- `sales-competitors` — Uses differentiators for competitive positioning
- `sales-prospect` — Uses all of the above

---

## Customization Tips

### For Outreach
Focus on:
- What problem you solve
- Who benefits most (ICP)
- Recent triggers/news to reference

### For Qualification
Focus on:
- Budget indicators
- Decision maker titles
- Timeline triggers

### For Competitors
Focus on:
- Your key differentiators
- Competitor names
- Why customers choose you

---

## Advanced: Multiple Products

Need different contexts for different products?

```bash
# Use product-specific briefs
cp PRODUCT-BRIEF.md PRODUCT-BRIEF-PRODUCTA.md
cp PRODUCT-BRIEF.md PRODUCT-BRIEF-PRODUCTB.md

# When generating, ensure the right file is in the working directory
cp PRODUCT-BRIEF-PRODUCTA.md ./PRODUCT-BRIEF.md
sales outreach "CompanyX"
```

---

## Git Safety

`PRODUCT-BRIEF.md` is git-ignored by default so you don't accidentally leak sensitive info.

To commit your template (without sensitive data):
```bash
git add PRODUCT-BRIEF-TEMPLATE.md
# Never commit PRODUCT-BRIEF.md with real data
```
