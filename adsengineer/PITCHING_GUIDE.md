# How to Pitch AdsEngineer to Prospects

This guide explains how to use the AdsEngineer sales system to create targeted, effective pitches for prospects like rm-immo.

## The AdsEngineer Sales Approach

AdsEngineer uses a three-tiered pitching strategy that addresses different stakeholder concerns with escalating value propositions:

### Tier 1: Compliance & Legal Protection (Urgency)
- **Target:** CEO/Founder/Legal Officer
- **Focus:** Regulatory risk, fines, liability
- **Hook:** "Your current tracking likely violates DSGVO/NDSG, exposing you to fines up to €20M"
- **Best for:** Immediate attention-getter, creates urgency

### Tier 2: Attribution Recovery & ROI (Business Impact)
- **Target:** Marketing Director, CFO, Head of Growth
- **Focus:** Wasted ad spend, inaccurate ROAS, budget optimization
- **Hook:** "You're blind to 30-40% of your conversions – your Smart Bidding optimizes on incomplete data"
- **Best for:** Demonstrating tangible financial value

### Tier 3: Opportunity Detection & Speed (Competitive Advantage)
- **Target:** Sales Director, Business Development, Operations
- **Focus:** Missed leads, slow response times, competitive disadvantage
- **Hook:** "You're missing when Bauträger research your site anonymously – no real-time alerts"
- **Best for:** Showing operational superiority and competitive edge

## Using the Prospect Questionnaire

The `PROSPECT-QUESTIONNAIRE.md` file is your discovery tool. Here's how to use it effectively:

### 1. Pre-Meeting Research
- Fill out as much as possible from public sources (website, LinkedIn, news, etc.)
- Use the `/sales research <url>` command to automate company research
- Identify gaps that need to be filled in conversation

### 2. Discovery Conversation
- Use the questionnaire as a flexible guide, not a rigid script
- Focus on uncovering specific pain points, not just checking boxes
- Listen for emotional language around frustrations ("It drives me crazy when...", "We lose so much money because...")
- Quantify impacts where possible ("How many leads do you think you're missing monthly?")

### 3. Post-Meeting Analysis
- Complete the questionnaire with gathered information
- Identify which of the three tiers resonates most strongly
- Look for quantifiable pain points you can tie to AdsEngineer's value propositions
- Note any objections or concerns raised

### 4. Pitch Customization
- Select the tier(s) that address the prospect's strongest pains
- Use their exact language and examples in your pitch
- Reference specific keywords, campaigns, or pain points they mentioned
- Connect features directly to their stated goals and fears

## The rm-immo Example Walkthrough

Looking at the files I created for rm-immo (`adsengineer/prospects/rm-immo/`), you can see how this works in practice:

### From Questionnaire to Pitch
**Questionnaire Insights:**
- Attributions-Lücke: 2-week delay between click and call breaks tracking
- Datenverlust: 30% of clicks lost to Safari/Adblocker  
- DSGVO risk: Inadequate cookie consent creating compliance exposure
- B2B Blindheit: Can't see anonymous construction company visitors
- ROAS Vertrauen: Hard to measure true return due to long sales cycle

**Pitch Translation:**
- **Tier 1 (Compliance):** "Your cookie banner likely doesn't block tracking pre-consent – creating unlawful data transfers under DSGVO"
- **Tier 2 (Attribution):** "Server-side GCLID preservation solves your 2-week attribution gap, showing which ads truly drive million-euro deals"
- **Tier 3 (Opportunity):** "IronClaw B2B identification reveals when Bauträger research your site anonymously – enabling real-time outreach"

### Supporting Documents Created
1. **COMPANY-RESEARCH.md** - Background research on the company
2. **COMPETITIVE-INTEL.md** - Analysis of competitive gaps and positioning
3. **PITCH.md** - The customized three-tier sales pitch
4. **PROSPECT-ANALYSIS.md** - Full scored analysis with outreach recommendations

## Integrating with AdsEngineer Sales Commands

Once you've completed your discovery:

1. **Run `/sales prospect <url>`** - Get a full 5-agent analysis with scoring and ready-to-send email
2. **Use `/sales outreach "<company>"`** - Generate a personalized email sequence
3. **Run `/sales prep <url>`** - Create a meeting preparation brief
4. **Use `/sales proposal "<client>"`** - Generate a formal proposal document
5. **Run `/sales objections "<topic>"`** - Prepare for specific objections (pricing, implementation, etc.)

## Best Practices for AdsEngineer Pitching

### Do:
- Lead with their specific pain points, not generic features
- Quantify the impact of their current gaps (use their numbers when possible)
- Speak their language – use terms like "Attributions-Lücke", "Heißer Fisch", "Macher-Modus"
- Focus on outcomes, not technology (better ROAS, fewer fines, faster deals)
- Provide proof points relevant to their industry (real estate, construction, etc.)
- Make implementation sound simple and low-risk

### Don't:
- Lead with technical specifications or jargon
- Assume they know what GCLID, ITP, or server-side tracking means without explanation
- Forget the compliance angle – it's often the strongest opener in regulated markets
- Overwhelm with features – pick 2-3 that solve their specific pains
- Ignore the human element – even in B2B, decisions are emotional

## Next Steps for Your Sales Process

1. **Template Your Approach:** Create a master questionnaire based on PROSPECT-QUESTIONNAIRE.md
2. **Research Systematically:** Use `/sales research` for initial company intel
3. **Document Discoveries:** Always complete a questionnaire per prospect
4. **Build Your Pitch Library:** Save successful PITCH.md files as templates for similar prospects
5. **Track What Works:** Note which tiers resonate most with different company types
6. **Leverage Social Proof:** When you have wins, create case studies for similar prospects

Remember: The most effective AdsEngineer pitches don't sell tracking – they sell compliance peace of mind, true marketing ROI, and the ability to act on opportunities competitors miss.