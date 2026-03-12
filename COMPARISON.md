# AI Sales Team: OpenCode Edition vs Claude Code Original

## Overview

| Feature | Original (Claude Code) | OpenCode Edition |
|---------|----------------------|------------------|
| **Platform** | Claude Code only | OpenCode + CLI |
| **Slash Commands** | Native `/sales` | `/sales` CLI wrapper |
| **Product Context** | Hardcoded | Dynamic `PRODUCT-BRIEF.md` |
| **Skills** | 14 Claude skills | 15 OpenCode skills |
| **Reusability** | Single product | Multi-product ready |
| **Customization** | Edit skill files | Config files only |

---

## What We Built (OpenCode Edition)

### 1. Dynamic Product Context System

| Original | OpenCode Edition |
|----------|-----------------|
| Hardcode product in skill files | External `PRODUCT-BRIEF.md` |
| Edit SKILL.md to change product | Edit config file |
| Single product per installation | Multiple products supported |
| No git safety | `PRODUCT-BRIEF.md` git-ignored |

**Files:**
```
PRODUCT-BRIEF.md              # Your product config (git-ignored)
PRODUCT-BRIEF-TEMPLATE.md    # Template to copy from
PRODUCT-CONTEXT.md           # Documentation
```

### 2. CLI Slash Commands

| Original | OpenCode Edition |
|----------|-----------------|
| `/sales prospect` (Claude Code native) | `sales prospect` (bash CLI) |
| Only works in Claude Code | Works in any terminal |
| No installation needed | `cp sales-cli /usr/local/bin/` |

**Installation:**
```bash
cp sales-cli /usr/local/bin/sales
chmod +x /usr/local/bin/sales

# Now use anywhere!
sales prospect https://stripe.com
sales research https://notion.so
```

### 3. Stakeholder Briefing Skill (NEW)

Generate briefings for any stakeholder:

| Stakeholder | Output |
|-------------|--------|
| Investor | `STAKEHOLDER-BRIEF-INVESTOR.md` |
| Developer | `STAKEHOLDER-BRIEF-DEVELOPER.md` |
| Partner | `STAKEHOLDER-BRIEF-PARTNER.md` |
| Board | `STAKEHOLDER-BRIEF-BOARD.md` |
| Employee | `STAKEHOLDER-BRIEF-EMPLOYEE.md` |

### 4. Persistent Product Memory

| Original | OpenCode Edition |
|----------|-----------------|
| Repeat product info every prompt | `CURRENT-PRODUCT.md` remembers |
| No context persistence | Context auto-loaded |

### 5. Organized Output Hierarchy

```
adsengineer/
├── brief/
│   └── PRODUCT-BRIEF.md
├── pipeline/
│   └── SALES-REPORT.md
└── prospects/
    └── babyrella/
        ├── instructions.md
        ├── outreach/
        │   ├── urgent.md
        │   ├── email-sequence.md
        │   └── linkedin.md
        └── competitive/
            └── intel.md
```

---

## Feature Comparison Table

| Feature | Claude Code | OpenCode | Notes |
|---------|-------------|----------|-------|
| `/sales prospect` | ✅ | ✅ | Full audit |
| `/sales research` | ✅ | ✅ | Company research |
| `/sales qualify` | ✅ | ✅ | BANT/MEDDIC |
| `/sales contacts` | ✅ | ✅ | Decision makers |
| `/sales outreach` | ✅ | ✅ | Email sequences |
| `/sales followup` | ✅ | ✅ | Follow-ups |
| `/sales prep` | ✅ | ✅ | Meeting prep |
| `/sales proposal` | ✅ | ✅ | Proposals |
| `/sales objections` | ✅ | ✅ | Objection handling |
| `/sales icp` | ✅ | ✅ | ICP builder |
| `/sales competitors` | ✅ | ✅ | Competitive intel |
| `/sales report` | ✅ | ✅ | Pipeline report |
| `/sales report-pdf` | ✅ | ✅ | PDF reports |
| `/sales brief` | ❌ | ✅ | **NEW** Stakeholder briefings |
| Dynamic product config | ❌ | ✅ | **NEW** PRODUCT-BRIEF.md |
| CLI commands | ❌ | ✅ | **NEW** sales-cli |
| Persistent memory | ❌ | ✅ | **NEW** CURRENT-PRODUCT.md |

---

## Why OpenCode Edition?

### Advantages

1. **Works outside Claude Code** - CLI works in any terminal
2. **Product-agnostic** - Change products without editing code
3. **Git-safe** - Sensitive data in git-ignored files
4. **Multi-product** - Run different products from same installation
5. **Stakeholder briefings** - New skill for internal/external comms

### Use Cases

| Scenario | Original | OpenCode |
|----------|----------|----------|
| Using Claude Code | ✅ | ✅ |
| Using OpenCode | ❌ | ✅ |
| CLI terminal | ❌ | ✅ |
| Multiple products | Hard | Easy |
| Team sharing | Hard | Easy |

---

## Installation

### Claude Code (Original)
```bash
curl -fsSL https://raw.githubusercontent.com/zubair-trabzada/ai-sales-team-claude/main/install.sh | bash
```

### OpenCode Edition
```bash
# Clone
git clone https://github.com/stevie86/ai-sales-team-opencode.git

# Install CLI
cp sales-cli /usr/local/bin/sales
chmod +x /usr/local/bin/sales

# Configure product
cp PRODUCT-BRIEF-TEMPLATE.md PRODUCT-BRIEF.md
vim PRODUCT-BRIEF.md

# Use!
sales prospect https://stripe.com
```

---

## Repo Links

| Version | URL |
|---------|-----|
| **Original (Claude Code)** | github.com/zubair-trabzada/ai-sales-team-claude |
| **OpenCode Edition** | github.com/stevie86/ai-sales-team-opencode |

---

*Comparison generated March 2026*
