"""All copy for www.aattrl.com. Edit here, then run `python3 _build/build.py`.

Body text is Markdown. Keep claims factual: no invented clients, numbers or quotes.
Situations described as examples are illustrative and are labelled as such on the page.
"""

SITE = dict(
    name="AATTRL",
    legal_name="AATTRL Global Expert Advisory",
    url="https://www.aattrl.com",
    tagline="Executive problem-solving",
    descriptor="AATTRL takes on the hard problems that stay on a chief executive's desk and works them through to resolution.",
    email="info@aattrl.com",
    phone_display="+971 50 607 4374",
    wa_number="971506074374",
    regions="India, the GCC and internationally",
    founded_note="Founded by Basheer Thasthakir.",
    enaivu_url="https://enaivu.com",
    # Analytics stay off until IDs are set in assets/js/main.js.
)

# Primary navigation: (label, path). Secondary links live in the footer.
NAV = [
    ("How it works", "/how-it-works/"),
    ("Challenges", "/challenges/"),
    ("Engagements", "/engagements/"),
    ("Who we serve", "/who-we-serve/"),
    ("About", "/about/"),
    ("Insights", "/insights/"),
]
CTA = ("Bring a challenge", "/bring-a-challenge/")

FOOTER_COLUMNS = [
    ("Firm", [("About", "/about/"), ("The senior network", "/network/"), ("Who we serve", "/who-we-serve/"), ("Contact", "/contact/")]),
    ("Work", [("How it works", "/how-it-works/"), ("Challenges we take on", "/challenges/"), ("Engagements", "/engagements/"), ("Insights", "/insights/")]),
    ("Start", [("Bring a challenge", "/bring-a-challenge/"), ("Join the network", "/network/#join"), ("Enaivu, software by AATTRL", SITE["enaivu_url"]), ("Privacy", "/privacy/")]),
]

# --------------------------------------------------------------------------
HOME = dict(
    title="AATTRL | Executive Problem-Solving for Chief Executives",
    desc="AATTRL takes on the problems that stay on a CEO's desk: stalled growth, failing projects, margin pressure, decisions that cannot be wrong. Senior people, one problem, worked through to resolution.",
    h1="The problems that stay on your desk.",
    lead="Every chief executive carries a few problems that no department can solve and no report quite explains. AATTRL takes one of them on, puts senior people around it, and works it through to a resolution you can act on.",
    # Spoken in the executive's own voice. These are the hook.
    voices=[
        "Growth has flattened and every explanation I get is partly true.",
        "The programme is a year late and nobody in the room will say so.",
        "Margins are thinning and the cost plan is already in its third version.",
        "We have spent heavily on digital and I cannot see where it is paying off.",
        "This is the one decision this year I cannot afford to get wrong.",
        "My leadership team agrees in the meeting and diverges in the corridor.",
    ],
    what_h="One problem. Senior people. A resolution.",
    what=[
        ("You bring the problem", "A confidential conversation with the principal. You describe the situation as you see it, including the parts that are political, personal or unproven."),
        ("We put the right senior people around it", "A small team drawn from the AATTRL senior network: people who have run the function, the project or the business you are describing. No junior staff, no bench to fill."),
        ("We work it through to resolution", "Diagnosis you can trust, a decision with its consequences made plain, and the execution support to make it hold. You stay in control; the problem leaves your desk."),
    ],
    different_h="How this differs from hiring a consultancy",
    different=[
        ("Scoped to a problem, not a practice", "The engagement ends when the problem is resolved or the decision is made, not when a phase plan says so."),
        ("Senior throughout", "The people who diagnose are the people who deliver. Nothing is handed down to an analyst team you never meet."),
        ("Answerable to you", "AATTRL works for the chief executive, not for a function or a sponsor. Findings are reported to you first and in full."),
        ("Built for the awkward problems", "The ones that involve people, politics and incomplete information as much as numbers. Those are the ones that stay on a CEO's desk."),
    ],
    serve_h="Who we work with",
    serve="Chief executives, managing directors, owners and group heads of mid-sized and large organisations in India, the GCC and internationally; country and divisional heads with full accountability for a business; and investors who need a portfolio company's hardest problem resolved.",
    cta_h="Start with a conversation",
    cta_p="Describe the situation in a few lines. The principal replies personally, usually within two working days, and tells you honestly whether AATTRL is the right firm to take it on.",
)

# --------------------------------------------------------------------------
HOW = dict(
    title="How It Works: From Brief to Resolution | AATTRL",
    desc="How an AATTRL engagement runs: a confidential brief, a senior team, a diagnosis you can trust, a decision made plain, and execution support until the resolution holds.",
    h1="How an engagement runs",
    lead="Every engagement follows the same spine, from the first confidential conversation to the day the problem is formally handed back, resolved. What varies is the size of the team and how long each stage takes.",
    steps=[
        ("Brief", "A confidential conversation with the principal, in person or online. You describe the problem as you see it; we ask the questions a board would not. Within a few days you receive a one-page statement of the problem, what a resolution would look like, who we propose and the terms. If AATTRL is not the right firm, we say so and, where we can, suggest who is."),
        ("Diagnose", "A small senior team examines the problem from the inside: the numbers, the people, the decisions already made and the ones being avoided. Interviews are held in confidence. The output is a diagnosis in plain language, reported to you first, including the findings that are uncomfortable."),
        ("Decide", "The options are laid out with their consequences, costs and risks made explicit. We give a recommendation and the reasoning behind it. The decision is yours; our job is to make sure it is taken with the full picture and that it will survive contact with the board, the bank or the team."),
        ("Deliver", "Where the resolution needs execution, the same senior people stay to make it happen: leading a recovery, running a negotiation, installing an operating cadence, or standing beside the executive who has to carry it. Progress is reported to you at an agreed rhythm, in writing."),
        ("Hand back", "The engagement ends when the problem is resolved or the decision has been made and is holding. You receive a closing note: what was found, what was done, what to watch for. Nothing is left running without your agreement."),
    ],
    terms_h="Terms you can expect",
    terms=[
        ("Fixed scope and fee", "Each stage is scoped and priced before it starts. A problem that turns out to be larger than briefed is re-scoped with you, not quietly extended."),
        ("Confidentiality by default", "Engagements are not publicised, interviews are held in confidence, and a non-disclosure agreement is signed before the brief if you prefer."),
        ("Independence", "The team has no stake in the answer. AATTRL does not sell software, systems or placements as part of an engagement, and declares any connection to a party involved."),
        ("Direct access", "You deal with the principal and the senior team throughout, by phone, in person and in writing. There is no account manager."),
    ],
    length_h="How long it takes",
    length="A brief is usually complete within a week of the first conversation. Diagnosis typically takes between two and six weeks depending on the size of the business and the access available. Decisions are reached in a matter of days once the diagnosis is accepted. Delivery runs for as long as the resolution needs, in agreed stages, and is reviewed with you at the end of each.",
)

# --------------------------------------------------------------------------
CHALLENGES_HUB = dict(
    title="Challenges We Take On | AATTRL",
    desc="The executive problems AATTRL takes on: stalled growth, margin pressure, a failing programme, operations that do not deliver, transformation that is not paying off, a decision that cannot be wrong, a leadership team that does not execute, a crisis.",
    h1="Challenges we take on",
    lead="These are the problems that stay on a chief executive's desk because they cross functions, involve people as much as numbers, and carry consequences that no one else is accountable for. Each page describes what the problem usually looks like from the top, and how AATTRL works it through.",
)

CHALLENGES = [
dict(
    slug="growth-has-stalled", name="Growth has stalled",
    title="When Growth Has Stalled: Executive Problem-Solving | AATTRL",
    desc="Revenue has flattened and every explanation is partly true. How AATTRL diagnoses a growth stall from the top and gets a CEO to a decision that restarts it.",
    short="Revenue has flattened and every explanation is partly true. Sales blames product, product blames pricing, finance blames the market.",
    h1="Growth has stalled, and every explanation is partly true",
    lead="A stall rarely has one cause. By the time it reaches the chief executive it has several, each owned by a different function, each defended with a plausible story. The problem is not a lack of ideas; it is that no one is accountable for the whole picture.",
    body="""
## What it looks like from the top

- The forecast has been missed for several quarters, each time for a different reason.
- The sales pipeline is large on paper and thin in practice.
- Pricing, product and go-to-market decisions are made separately and contradict each other.
- The growth plan has initiatives in it that nobody would defend one-to-one.
- The board is asking whether the strategy is wrong or the execution is.

## How AATTRL works it through

The diagnosis separates what has changed in the market from what has changed in the business. A small senior team looks at the customer base, the pricing and the sales engine together, talks to customers who left and customers who stayed, and tests each function's story against the numbers rather than against the other functions' stories.

You receive one explanation of the stall, with evidence, and a short list of moves ranked by how much growth they are likely to restart and how fast. Where the honest answer is that the market has moved and the model must change, you hear that first and from us.

## What a resolution looks like

- A clear, shared account of why growth stopped, accepted by the leadership team.
- Two or three decisions taken, not twenty initiatives launched.
- Ownership for the growth plan sitting with named people with the authority to execute it.
- Senior support alongside the executives carrying the hardest moves, for as long as it takes to make them hold.
""",
    related=["margins-under-pressure", "leadership-team-not-executing", "a-decision-you-cannot-get-wrong"],
),
dict(
    slug="margins-under-pressure", name="Margins under pressure",
    title="Margins Under Pressure: Cost and Profitability Resolution | AATTRL",
    desc="Margins are thinning and the cost plan is in its third version. How AATTRL finds where profitability is leaking and helps a CEO take the structural decisions.",
    short="Margins are thinning, the cost plan is in its third version, and the cuts so far have taken capability without taking cost.",
    h1="Margins are thinning and the cost plan keeps being rewritten",
    lead="Cost programmes fail from the top down. Targets are set by the board, divided among functions, and met on paper by actions that remove capability rather than cost. Meanwhile the structural reasons the margin is thinning are not discussed because they belong to no one.",
    body="""
## What it looks like from the top

- Gross margin is drifting down while volume holds or grows.
- Each round of savings is smaller than the last and harder to find.
- Pricing has not been revisited seriously in years; discounts have.
- Overheads were built for a larger or different business.
- Nobody can say which products, customers or sites actually make money.

## How AATTRL works it through

We start with profitability by product, customer, channel and site, built from the ledger rather than from allocations, so that the leadership team is looking at the same picture for the first time. Then we test the structural options: pricing and discount discipline, the shape of the overhead, the contracts and suppliers that have never been renegotiated, the lines that should be exited.

The team has run businesses through this before and knows which savings come back and which do not. The recommendation distinguishes between decisions that restore the margin and actions that merely delay the next cut.

## What a resolution looks like

- A reliable profitability map the leadership team trusts and uses.
- Structural decisions taken: pricing, portfolio, overhead and contracts.
- A cost base that fits the business you have, not the one you planned.
- Senior support running the difficult conversations with customers, suppliers and the team.
""",
    related=["growth-has-stalled", "operations-not-delivering", "crisis-or-turnaround"],
),
dict(
    slug="a-critical-programme-is-failing", name="A critical programme is failing",
    title="A Critical Programme Is Failing: Independent Review and Recovery | AATTRL",
    desc="The programme is late, over budget, and no one in the room will say so. How AATTRL gives a CEO an honest view of a failing programme and leads its recovery.",
    short="The flagship project is late and over budget, the steering committee reports amber, and the people closest to it have stopped telling you the truth.",
    h1="The programme is late and nobody in the room will say so",
    lead="A failing programme produces optimism in direct proportion to its trouble. Milestones are re-baselined, status stays amber, and the people who know are either too invested or too junior to say what they see. The chief executive is the last to hear and the first to be accountable.",
    body="""
## What it looks like from the top

- Dates have moved more than once and the new dates are not believed.
- Spend is ahead of progress and the business case has not been revisited.
- The contractor, the vendor and your own team each blame the other two.
- Governance produces reports, not decisions.
- You suspect the right answer may be to stop, change course or replace people, and no one will put that in writing.

## How AATTRL works it through

An independent senior review, led by people who have delivered and recovered programmes of this kind, establishes within weeks where the programme actually is: the true state of scope, schedule, cost, contracts and the team. Findings are reported to you first, in plain language, including whether the programme should continue.

If it should, the same people lead the recovery: resetting the plan to one that can be believed, renegotiating with the contractor or vendor from a position of fact, and installing governance that takes decisions. If it should not, we help you stop it cleanly and account for it to the board.

## What a resolution looks like

- A true baseline, accepted by the programme and the board.
- A decision to recover, re-scope or stop, taken with the full picture.
- The contractual and commercial position protected.
- A programme leadership and cadence that reports the truth and acts on it.
""",
    related=["operations-not-delivering", "transformation-not-paying-off", "a-decision-you-cannot-get-wrong"],
),
dict(
    slug="operations-not-delivering", name="Operations are not delivering",
    title="Operations Not Delivering: Performance Resolution from the Top | AATTRL",
    desc="Output, quality, service or reliability are below what the business needs, and the operational explanations have run out. How AATTRL resolves operational performance at executive level.",
    short="Output, service or reliability keep falling short, the operational reasons have been fixed twice, and the problem keeps returning.",
    h1="Operations keep falling short and the fixes keep not holding",
    lead="When an operation underperforms for long enough, the organisation stops expecting it to perform. Targets are quietly lowered, workarounds become the process, and the leadership team argues about symptoms. The question for the chief executive is rarely technical. It is why the business has accepted this.",
    body="""
## What it looks like from the top

- Output, quality, delivery or uptime are consistently below plan and the gap is not closing.
- Improvement programmes have come and gone; each one fixed something and the result did not change.
- Operations, sales and finance hold different views of what the operation is for.
- Key people are exhausted, and the ones who could fix it are the ones already overloaded.
- Customers have started to notice.

## How AATTRL works it through

Senior operators who have run plants, networks, service operations and supply chains look at the operation whole: its demand, its capacity, its management system, its people and the commercial promises made on its behalf. The diagnosis is as likely to find a sales or planning cause as an operational one, and says so.

We then work with you on the decisions only the chief executive can take: what the operation is being asked to do, what it will stop doing, who leads it and with what authority. Where the recovery needs senior hands on the ground, the same people provide them.

## What a resolution looks like

- A shared, factual account of why the operation underperforms.
- Decisions on scope, priorities and leadership that remove the structural causes.
- An operating cadence that makes performance visible weekly and acts on it.
- Senior support alongside the operations leadership until the new level holds.
""",
    related=["margins-under-pressure", "a-critical-programme-is-failing", "transformation-not-paying-off"],
),
dict(
    slug="transformation-not-paying-off", name="Transformation is not paying off",
    title="Digital and AI Transformation Not Paying Off: An Executive Reckoning | AATTRL",
    desc="Heavy investment in digital, data or AI and no visible return. How AATTRL helps a CEO see what the transformation has actually delivered and decide what to do next.",
    short="The business has spent heavily on digital, data or AI, the programme reports progress, and you cannot point to where it has paid off.",
    h1="We have spent heavily on digital and I cannot see where it is paying off",
    lead="Transformation programmes are easy to start, hard to stop and almost impossible to assess from the inside. They report activity, licences and go-lives. The chief executive wants to know a simpler thing: has the business become better, faster or cheaper because of this, and if not, why not.",
    body="""
## What it looks like from the top

- Significant spend over several years; benefits described in future tense.
- Systems delivered that the business works around.
- Data and AI initiatives that produce demonstrations rather than decisions.
- A technology function and a business that describe the same programme differently.
- Vendors and integrators more certain of the next phase than of the last one.

## How AATTRL works it through

This is an executive problem, not a technical one, and we treat it as such. Senior people who have led transformations from the business side establish what has been delivered, what it has changed in operating results, and what it has cost in full, including the attention of your best people. The review is independent of the technology function and of any vendor.

The recommendation is a business decision: what to keep and finish, what to stop, what to fix, and how to run the remainder so that it is accountable for results rather than milestones. Where the business is asset-intensive, the team includes people who understand what digital, data and AI can realistically do for plants, networks and fleets, and what they cannot.

## What a resolution looks like

- An honest statement of what the transformation has delivered, agreed with the board.
- A reshaped portfolio: fewer initiatives, each owned by a business leader for a result.
- Vendor and integrator relationships reset on outcomes.
- Senior support for the executives who must now make it pay.
""",
    related=["a-critical-programme-is-failing", "operations-not-delivering", "a-decision-you-cannot-get-wrong"],
),
dict(
    slug="a-decision-you-cannot-get-wrong", name="A decision you cannot get wrong",
    title="A Decision You Cannot Get Wrong: Independent Executive Decision Support | AATTRL",
    desc="A major investment, acquisition, market entry, exit or restructuring. How AATTRL gives a CEO an independent, senior view before the decision is taken.",
    short="A major investment, acquisition, market entry, exit or restructuring. The advisers each have an interest, and the board will remember who decided.",
    h1="This is the one decision this year I cannot get wrong",
    lead="Large decisions arrive with large amounts of advice, most of it from parties who benefit from a particular answer. What a chief executive lacks is not analysis but an independent senior view: people with no stake in the outcome who have taken decisions like this and lived with them.",
    body="""
## What it looks like from the top

- A significant capital investment, acquisition, divestment, market entry or restructuring.
- A recommendation already on the table, from people who want it approved.
- Due diligence that answers the questions asked and not the ones that matter.
- A board that will approve it on your word and remember it on your record.
- Little time, and a sense that the real risks have not been named.

## How AATTRL works it through

A small senior team, chosen for having made and carried decisions of this kind, examines the proposal as an owner would: the assumptions, the downside, the people who will have to deliver it, the exit if it fails. Where technical or operational substance matters, in an asset-heavy acquisition or a major plant investment, the team includes people who can judge it directly rather than rely on the seller's reports.

You receive a written view: what is sound, what is not, what would change our answer, and what we would do. It is addressed to you and can be shared with the board as the independent view it is.

## What a resolution looks like

- The decision taken, or declined, with the full picture and its consequences made plain.
- The risks named in writing before the commitment, not after.
- Terms, conditions and plans improved where the review found weakness.
- Senior support through the first months of carrying it out, where wanted.
""",
    related=["growth-has-stalled", "transformation-not-paying-off", "board-or-investor-pressure"],
),
dict(
    slug="leadership-team-not-executing", name="The leadership team is not executing",
    title="A Leadership Team That Agrees and Does Not Execute | AATTRL",
    desc="Strategy agreed in the room, diverging in the corridor. How AATTRL diagnoses an execution gap at the top of a business and helps the CEO close it.",
    short="Strategy is agreed in the room and diverges in the corridor. Priorities multiply, decisions are revisited, and you are the only person holding the whole plan.",
    h1="My leadership team agrees in the meeting and diverges in the corridor",
    lead="An execution gap at the top of a business is rarely a problem of competence. It is usually a problem of design: unclear accountability, too many priorities, decisions that are not actually decisions, and a chief executive who has become the only integrating point. It is hard to see from inside the team, and harder to raise.",
    body="""
## What it looks like from the top

- Agreed priorities that quietly multiply until nothing is a priority.
- Decisions that are revisited at the next meeting by the same people who took them.
- Functions optimising their own results at the expense of the whole.
- One or two executives everyone works around, including you.
- A plan that lives in your head and nowhere else.

## How AATTRL works it through

The principal and one or two senior people who have led executive teams examine how the team actually works: how decisions are taken and recorded, how accountability is set, how performance is reviewed, and where the structure makes execution hard. Conversations with each executive are held in confidence; the findings are reported to you plainly, including findings about roles, individuals and your own part in the pattern.

The resolution is a set of decisions about design: the operating rhythm, the real priorities, the accountability of each role, and in some cases the composition of the team. We stay to help you install it and to make the hard conversations happen.

## What a resolution looks like

- A short list of priorities every executive can recite and is measured on.
- Decisions taken once, recorded and acted on.
- Accountability and authority aligned role by role.
- A leadership team you can leave in the room without the plan falling apart.
""",
    related=["growth-has-stalled", "operations-not-delivering", "crisis-or-turnaround"],
),
dict(
    slug="crisis-or-turnaround", name="A crisis or turnaround",
    title="Crisis and Turnaround Leadership for Chief Executives | AATTRL",
    desc="A liquidity squeeze, a lost major customer, a safety or regulatory event, a business that must be turned around in months. How AATTRL puts senior people beside a CEO in a crisis.",
    short="A liquidity squeeze, a lost major customer, a serious incident or a business that must be turned around in months, with everyone watching.",
    h1="The business is in trouble and the next few months decide it",
    lead="A crisis compresses every other problem into weeks and removes the margin for learning on the job. The chief executive needs people beside them who have been through this before, who can take real work off their hands, and who will tell them the truth when everyone else is managing them.",
    body="""
## What it looks like from the top

- Cash is tighter than the forecast admitted; the bank or investors want a plan.
- A major customer, contract or licence has been lost or is at risk.
- A serious safety, quality, regulatory or reputational event is unfolding.
- The business must be stabilised and turned around within a defined period.
- Information arrives late, filtered and optimistic.

## How AATTRL works it through

In the first days, senior people establish the facts: the cash position, the commitments, the exposures and the options. A stabilisation plan is agreed with you and, where required, presented with you to lenders, investors, regulators or the board. The same people then take on defined parts of the response, leading the cash discipline, the customer recovery, the incident response or the restructuring, while you lead the business.

Throughout, you have a small group that reports to you alone, has no stake in the outcome beyond resolving it, and has done this before.

## What a resolution looks like

- Stabilised cash, commitments and stakeholders within the first weeks.
- A credible plan accepted by lenders, investors or the board.
- The business through the acute phase with its options preserved.
- A structured handover to a leadership team that can run what remains.
""",
    related=["margins-under-pressure", "board-or-investor-pressure", "leadership-team-not-executing"],
),
dict(
    slug="board-or-investor-pressure", name="Board or investor pressure",
    title="Under Pressure From the Board or Investors: Counsel for the CEO | AATTRL",
    desc="The board, an investor or a parent company has lost patience and the CEO needs an independent view, a credible plan and senior support before the next meeting.",
    short="The board, an investor or the parent has lost patience. You need an independent view of your own position and a plan they will believe before the next meeting.",
    h1="The board has lost patience and I need a plan they will believe",
    lead="When confidence at the top is in question, a chief executive has few people to turn to: the leadership team has an interest, the advisers have a fee, and the board is the audience. What helps is an independent senior view of the position and a plan built to survive scrutiny from people who have sat on both sides of that table.",
    body="""
## What it looks like from the top

- Results have missed expectations and the explanations are no longer being accepted.
- A new investor, chair or parent company with a different view of the business.
- Requests for plans, reviews and reporting that consume the leadership team.
- Advisers to the board who are not advisers to you.
- Uncertainty about what the board actually wants, and whether it can be delivered.

## How AATTRL works it through

The principal and senior people who have served as chief executives, directors and investors give you a frank, confidential assessment: the real state of the business, the real concerns of the board or investor, and the realistic options. We then help you build the plan and the case, test it the way the board will, and prepare you for the meeting.

Where the plan needs to be delivered, the same people stay to help you deliver it, so that the next board paper reports results rather than intentions.

## What a resolution looks like

- A frank assessment of your position and options, held in confidence.
- A plan the board or investor accepts because it answers their actual concerns.
- Results in the first quarter that restore confidence, with senior support to achieve them.
- Where the honest conclusion is a change of course, a managed one on your terms.
""",
    related=["crisis-or-turnaround", "a-decision-you-cannot-get-wrong", "growth-has-stalled"],
),
]

# --------------------------------------------------------------------------
ENGAGEMENTS_HUB = dict(
    title="Engagements: How AATTRL Works With a Chief Executive | AATTRL",
    desc="Four ways AATTRL works with chief executives: executive problem-solving, independent decision review, execution and recovery, and standing counsel.",
    h1="Engagements",
    lead="Most engagements begin with a single problem. Some are a review before a decision, some are hands-on recovery, and some become a standing relationship. The format follows the problem; the people and the terms stay the same.",
)

ENGAGEMENTS = [
dict(
    slug="executive-problem-solving", name="Executive problem-solving",
    title="Executive Problem-Solving: One Problem, Worked Through to Resolution | AATTRL",
    desc="The core AATTRL engagement. A chief executive brings one hard problem; a small senior team diagnoses it, brings it to a decision and supports execution until the resolution holds.",
    short="The core engagement. One problem, a small senior team, worked from brief to resolution.",
    h1="One problem, worked through to resolution",
    lead="The engagement AATTRL was built for. A chief executive brings a problem that crosses functions and has resisted the organisation's own attempts; a small team of senior people takes it from a confidential brief through diagnosis and decision to a resolution that holds.",
    body="""
## When it is the right format

- The problem belongs to the chief executive because no function can own it.
- The organisation has tried, and the attempts have produced reports rather than change.
- The situation involves people, politics or incomplete information as much as numbers.
- You want it resolved, not studied.

## What you get

- A one-page brief: the problem as we understand it, what resolution means, who we propose and the terms.
- A diagnosis in plain language, reported to you first and in full.
- A decision paper: options, consequences, our recommendation and why.
- Senior support in execution until the resolution holds, in agreed stages.
- A closing note: what was found, what was done, what to watch.

## Team and duration

Typically the principal and one to three senior people from the network, chosen for having run the function, project or business in question. Diagnosis usually takes two to six weeks; execution support runs in stages of one to three months, each reviewed with you. See [how it works](/how-it-works/) for the full sequence.
""",
),
dict(
    slug="independent-decision-review", name="Independent decision review",
    title="Independent Decision Review for Chief Executives | AATTRL",
    desc="Before a major investment, acquisition, exit or restructuring: an independent senior view of the proposal, its risks and the alternatives, addressed to the CEO and shareable with the board.",
    short="A senior, independent view of a major decision before it is taken, addressed to you and shareable with the board.",
    h1="An independent view before the decision",
    lead="For a major investment, acquisition, divestment, market entry, restructuring or programme commitment: senior people with no stake in the outcome examine the proposal as an owner would and give you a written view you can take to the board.",
    body="""
## When it is the right format

- A significant, hard-to-reverse decision is about to be taken.
- The recommendation comes from people who benefit from a particular answer.
- Due diligence has answered the questions asked, not the ones that matter.
- You want to know what could go wrong before the board remembers who decided.

## What you get

- A review of the proposal's assumptions, downside, delivery and exit.
- Where relevant, direct technical or operational judgement of the asset, plant, programme or business being acquired or built, from people who have run such things.
- A written view: what is sound, what is not, what would change our answer, what we would do.
- Preparation for the board, investor or lender discussion.

## Team and duration

The principal and one to three senior people selected for the decision at hand. Two to four weeks is typical; shorter when the decision cannot wait, with the limits of a shorter review stated plainly.
""",
),
dict(
    slug="execution-and-recovery", name="Execution and recovery",
    title="Execution and Recovery: Senior Hands on a Programme, Operation or Turnaround | AATTRL",
    desc="When the resolution needs senior hands: leading a programme recovery, an operational turnaround, a negotiation or a crisis response alongside the CEO's own team.",
    short="Senior people leading a recovery, a turnaround, a negotiation or a crisis response, alongside your team.",
    h1="Senior hands when the resolution needs them",
    lead="Some problems are resolved by a decision. Others are resolved by someone experienced taking the work on: a programme recovery, an operational turnaround, a critical negotiation, a crisis. AATTRL provides senior people who lead that work beside your team, report to you, and leave when it holds.",
    body="""
## When it is the right format

- The diagnosis is clear and the business lacks the senior capacity or experience to act on it.
- A programme, operation or function needs recovery leadership for a defined period.
- A negotiation, restructuring or incident needs someone who has done it before.
- You want to keep your own leadership team running the business while this is resolved.

## What you get

- A named senior lead, accountable to you, with a defined mandate and end point.
- A recovery or delivery plan that can be believed, with progress reported weekly in writing.
- Decisions escalated to you early, with options, rather than surfaced late as surprises.
- A structured handover to your own people, so the result does not leave with us.

## Team and duration

One senior lead, sometimes with one or two others for specific work. Engagements run in stages of one to three months, each reviewed and renewed with you. The role is not a placement: the lead works for AATTRL and for you, on the problem, not in a vacancy.
""",
),
dict(
    slug="standing-counsel", name="Standing counsel",
    title="Standing Counsel for Chief Executives | AATTRL",
    desc="A continuing, confidential relationship with the principal and senior network: a sounding board on the hard calls, a rapid review when something lands, and senior people on call for the problems that follow.",
    short="A continuing, confidential relationship: a sounding board, rapid reviews, and senior people on call.",
    h1="A standing relationship with people who have done it",
    lead="Some chief executives, having resolved one problem with AATTRL, keep the relationship: a confidential sounding board for the decisions that cannot be discussed inside the business, a rapid senior review when something lands, and people on call for the next problem.",
    body="""
## When it is the right format

- You want an independent senior view available on short notice, not a new engagement each time.
- The business is in a period of change: new ownership, succession, expansion, restructuring.
- You value a conversation with people who have no stake in the answer and have carried the consequences themselves.

## What you get

- Scheduled conversations with the principal, as often as monthly, and access between them.
- Rapid review of a decision, paper or situation, usually within days.
- Priority access to the senior network when a problem needs a team.
- Complete discretion. The relationship is not publicised and nothing is discussed outside it.

## Terms

An annual or half-yearly retainer with agreed access, and separate terms for any problem that becomes a full engagement. Standing counsel is offered to a limited number of chief executives at a time so that the principal's attention is real.
""",
),
]

# --------------------------------------------------------------------------
SERVE = dict(
    title="Who We Serve: Chief Executives, Owners and Group Heads | AATTRL",
    desc="AATTRL works with chief executives, managing directors, owners, group and country heads, and investors in India, the GCC and internationally, across asset-intensive and service businesses.",
    h1="Who we serve",
    lead="AATTRL works for the person accountable for the whole business. The title varies; the position does not.",
    groups=[
        ("Chief executives and managing directors", "Of mid-sized and large companies, whether listed, private or part of a group, who carry a problem that no function can own and need it resolved rather than studied."),
        ("Owners and family businesses", "Owners and the executives who run businesses for them, often across generations and geographies, where the hardest problems involve family, succession and the professionalisation of the business as much as the market."),
        ("Group, country and divisional heads", "Executives with full accountability for a business inside a larger organisation, who need an independent view and senior support that does not come through the group's own channels."),
        ("Investors and boards", "Private equity, family offices and boards who need a portfolio company's hardest problem diagnosed and resolved by senior people who work with, not around, the chief executive."),
    ],
    sectors_h="Sectors",
    sectors_p="The problems AATTRL takes on are executive problems, and they occur in every sector. The senior network is deepest in asset-intensive and industrial businesses: energy, process and manufacturing industries, infrastructure, utilities, logistics and the engineering and services businesses around them. It also includes people who have run service, technology and trading businesses. Where a problem needs sector depth the network does not have, we say so.",
    where_h="Where we work",
    where_p="Clients are principally in India and the GCC. Engagements are also delivered in Europe, Asia and Africa, and anywhere the principal and the team can be present where the problem is. Diagnosis and counsel can be delivered remotely; recovery and execution usually cannot, and we plan for presence.",
)

# --------------------------------------------------------------------------
ABOUT = dict(
    title="About AATTRL: A Firm Built Around the Chief Executive's Problems | AATTRL",
    desc="AATTRL is an executive problem-solving firm founded by Basheer Thasthakir. It takes on the problems that stay on a CEO's desk and works them through to resolution with a network of senior people.",
    h1="A firm built around the chief executive's problems",
    lead="AATTRL exists for one reason: the hardest problems in a business are the ones that reach the chief executive, and the people best placed to resolve them are rarely available inside it.",
    body="""
## What AATTRL is

AATTRL is an executive problem-solving firm. It works for chief executives, owners and group heads, takes on one hard problem at a time, and puts senior people around it until it is resolved. It is not a consultancy with a bench to fill, a placement agency, or a software company; the problem defines the engagement, and the engagement ends when the problem does.

## How it came to be

The firm grew out of twenty years spent inside asset-heavy businesses in India, the Gulf and Europe, in design, project delivery, commissioning, operations and management. The pattern was the same everywhere: the problems that decided a business's fortunes were not technical, they were executive. They crossed functions, they involved people and politics, and they reached the top because no one below could own them. AATTRL was founded to take those problems on, with people who had carried them before.

## Principles

- **Senior throughout.** The people who diagnose are the people who deliver. Nothing is handed down to a team you never meet.
- **Answerable to the chief executive.** Findings are reported to you first and in full, including the uncomfortable ones.
- **Scoped to the problem.** Fixed scope and fee for each stage. A larger problem is re-scoped with you, not quietly extended.
- **Independent.** No products, systems or placements sold inside an engagement; any connection to a party involved is declared.
- **Discreet.** Engagements are not publicised. Interviews are held in confidence. A non-disclosure agreement is signed on request before the brief.
- **Honest about fit.** If AATTRL is not the right firm for a problem, we say so at the brief and, where we can, suggest who is.
""",
    principal_h="The principal",
    principal=dict(
        name="Basheer Thasthakir",
        role="Founder and Principal",
        bio="Basheer Thasthakir founded AATTRL after approximately twenty years in asset-heavy industry across India, Saudi Arabia, the United Arab Emirates and Norway, spanning design, EPC project delivery, commissioning and start-up, operations, maintenance, asset management and digital transformation. He leads every brief personally, assembles the senior team for each engagement and remains involved to its close.",
        facts=[("Based", "United Arab Emirates and India"), ("Experience", "Approximately 20 years, international"), ("Countries", "India, Saudi Arabia, UAE, Norway"), ("Background", "Mechanical engineer; asset-heavy industry"), ("Contact", "info@aattrl.com")],
    ),
    network_h="The senior network",
    network_p="Engagement teams are drawn from a network of senior people who have run businesses, functions, programmes and operations, and who take on a limited number of problems a year. The network is described on [its own page](/network/), and senior people who wish to be considered can apply there.",
    enaivu_h="Enaivu",
    enaivu_p="AATTRL also builds Enaivu, business software for small and mid-sized firms. It is a separate business with its own site at [enaivu.com](https://enaivu.com) and is never sold inside an AATTRL engagement.",
)

NETWORK = dict(
    title="The Senior Network: People Who Have Run Businesses | AATTRL",
    desc="AATTRL engagement teams are drawn from a network of senior people who have led businesses, functions, programmes and operations. How the network works, and how to join it.",
    h1="The senior network",
    lead="Every AATTRL team is assembled for the problem from a network of senior people: former chief executives and managing directors, functional heads, programme and operations leaders, and specialists with judgement earned in practice. There is no bench and nobody is assigned because they are free.",
    body="""
## Who is in it

- People who have run businesses, divisions or country operations with full accountability for results.
- Former heads of finance, operations, commercial, projects, technology and people functions who have carried an executive problem of their own.
- Programme and operations leaders who have delivered and recovered large undertakings.
- Technical and commercial specialists whose judgement is sought directly, for decisions in asset-heavy businesses in particular.
- Many have worked across India, the GCC and Europe and in more than one of them.

## How teams are formed

The principal briefs each problem and proposes the team, usually one to three people, named in the brief with their relevant experience. Members work on a limited number of problems at a time, directly with the client, and remain on the problem until it is resolved. They are bound by the same confidentiality and independence terms as the firm.

## Names

Network members are introduced to a client by name at the brief, with their experience. They are not listed publicly, because most hold or have held positions that make a public listing inappropriate, and because the right team depends on the problem.
""",
    join_h="Joining the network",
    join_p="AATTRL is interested in hearing from senior people who have run businesses, functions, programmes or operations, who are available for a small number of engagements a year, and who are comfortable working directly with a chief executive on a problem rather than delivering a method. Applications are reviewed by the principal and followed by a conversation.",
)

# --------------------------------------------------------------------------
INSIGHTS_HUB = dict(
    title="Insights for Chief Executives | AATTRL",
    desc="Short, practical pieces for chief executives on the problems that reach the top: diagnosis, decisions, execution and the use of outside senior help.",
    h1="Insights",
    lead="Short pieces written for chief executives, on the problems that reach the top and how to work them through. No frameworks, no jargon, and nothing longer than a flight.",
)

INSIGHTS = [
dict(
    slug="why-the-hardest-problems-stay-on-the-ceos-desk",
    name="Why the hardest problems stay on the CEO's desk",
    date="2026-10-26", minutes=5,
    desc="Some problems reach the chief executive and stay there. Not because the CEO hoards them, but because of how they are shaped. Understanding the shape is the first step to resolving them.",
    body="""
Every chief executive has a short list of problems that have been there for a while. They are discussed at offsites, appear in board papers under different names, and survive each reorganisation. They are not neglected. They are simply shaped in a way that the organisation cannot grip.

## Three shapes

The first shape is the problem that crosses functions. Growth that depends on product, pricing and sales together; a margin that depends on the operation, the contracts and the overhead together. Each function owns a piece and can defend its piece. Nobody owns the whole, except the person at the top.

The second is the problem that involves people. A programme is failing because of who is running it. An operation underperforms because of who has been allowed to run it that way. A leadership team does not execute because of two individuals and the way the rest work around them. These cannot be raised in the normal course of business, and the people who could raise them have the most to lose.

The third is the problem that is not yet proven. The CEO senses that the transformation is not paying off, that the acquisition is being oversold, that the forecast will be missed again. There is no report that says so, and asking for one changes the answer.

## Why the organisation cannot resolve them

In each case the organisation's normal machinery works against resolution. Functions produce functional answers. People protect positions. Reports confirm what their authors need confirmed. The chief executive is left with partial truths from several directions and no one accountable for assembling them.

## What resolves them

What these problems have in common is that they need someone with the authority of the chief executive, the independence of an outsider and the experience to tell the difference between a story and a fact. The CEO has the first. The organisation rarely has the second or the third. That is the gap AATTRL exists to fill: senior people, answerable to the chief executive, who take the whole problem and work it through.
""",
),
dict(
    slug="when-to-bring-in-outside-senior-help",
    name="When to bring in outside senior help, and when not to",
    date="2026-10-26", minutes=4,
    desc="Outside help is sometimes the right answer and sometimes an expensive way of avoiding one. A short test for chief executives.",
    body="""
Chief executives are offered outside help constantly, and most of it is sold rather than needed. Here is a short way to decide.

## Bring in outside senior help when

- The problem crosses functions and nobody inside can own the whole of it.
- The people who could resolve it have a stake in the answer.
- The question is not what to do but whether what you are being told is true.
- The business lacks someone who has done this before, and the cost of learning on the job is higher than the fee.
- You need a view the board will accept as independent.

## Do not bring it in when

- The problem has a clear owner inside the business who has not yet been asked.
- What you need is a decision you have already made and are avoiding.
- The help on offer is a method or a product looking for a problem.
- The real issue is a person, and the help is a way of not having that conversation. Outside senior help can run the conversation with you; it should not run it instead of you.

## The test

Ask who would be accountable for the result if the outside people left tomorrow. If the answer is "nobody", the problem is not yet shaped for outside help; it needs an owner first. If the answer is "me, and I do not have the people to do it", that is the point at which senior outside help pays for itself.
""",
),
dict(
    slug="the-difference-between-a-decision-and-a-meeting",
    name="The difference between a decision and a meeting",
    date="2026-10-26", minutes=4,
    desc="Many leadership teams believe they decide. What they do is meet. How to tell the difference and what to do about it.",
    body="""
A leadership team that agrees in the room and diverges in the corridor usually believes it is taking decisions. Look at the minutes. What is recorded is a discussion and a sense of the room. What is missing is the three things that make a decision a decision.

## What a decision has

**A sentence.** One line that states what has been decided, in terms that would make sense to someone who was not there. "We will exit the small-customer segment by year end" is a decision. "Agreed to review the segment strategy" is a meeting.

**An owner and a date.** One person accountable for making it happen and a date by which it will be visible. Two owners is no owner.

**A consequence.** Something that will now not happen because of it: budget withdrawn, a project stopped, a role changed. A decision that costs nothing has not been taken.

## Why teams avoid it

Because real decisions create losers in the room, and leadership teams are built for consensus. The chief executive often absorbs the gap, carrying the real decision alone while the team enjoys the sense of agreement.

## What to do

Change the record before changing the people. Require that every decision be minuted as a sentence, an owner, a date and a consequence, and that it be read back before the meeting ends. Within a quarter, the team will either be taking decisions or it will be clear who is preventing it. Both are progress.
""",
),
dict(
    slug="how-to-tell-whether-a-programme-is-really-amber",
    name="How to tell whether a programme is really amber",
    date="2026-10-26", minutes=5,
    desc="Programme status reports describe the programme's mood, not its state. Five questions a chief executive can ask to find out where a programme really is.",
    body="""
Programmes report amber for the same reason weather forecasts say "changeable": it is rarely wrong and never alarming. A chief executive who wants to know the real state of a programme cannot get it from the status report. These five questions usually get closer.

## Five questions

1. **What was the original date, and what is the date now?** Not the baseline, which has been reset; the first date anyone wrote down. The gap between the two is the true schedule position.

2. **How much has been spent, and what fraction of the scope is finished and in use?** Spend ahead of usable scope is the clearest early signal there is, and it is almost never on the dashboard.

3. **Who would say the programme is in trouble if it were?** If the answer is "no one would", the programme has no honest channel, which is a bigger problem than any delay.

4. **What has the contractor or vendor been paid for that has not yet been accepted?** The commercial position is where leverage lives and where it is most often lost.

5. **If we stopped today, what would we have?** The answer tells you whether the programme is delivering value incrementally or betting everything on the end.

## What the answers mean

If the answers come quickly and with evidence, the programme is probably as reported. If they come slowly, with caveats, or require a meeting to be arranged, the programme is not amber. It is red, and it is reporting amber because the people closest to it have decided that is what the chief executive wants to hear. That is the moment for an independent senior review, before the next re-baseline makes the truth harder to find.
""",
),
dict(
    slug="the-first-ninety-days-of-a-resolution",
    name="The first ninety days of a resolution",
    date="2026-10-26", minutes=4,
    desc="A diagnosis is accepted and a decision is taken. The next ninety days decide whether anything changes. What to insist on.",
    body="""
Most resolutions fail after the decision, not before it. The diagnosis was right, the decision was sound, and ninety days later the organisation has absorbed it without changing. Here is what to insist on in that period.

## Week one: the decision in writing

The decision as a sentence, an owner, a date and a consequence, circulated by the chief executive, not by the team that was reviewed. Anyone who disagrees should say so in the first week; after that, disagreement is a performance matter.

## Weeks two to four: the first visible consequence

Something that could not have happened before the decision must happen now: a contract renegotiated, a project stopped, a role changed, a price raised. Until it does, the organisation will assume the decision is like the others.

## Weeks four to twelve: a cadence you attend

A short weekly review of the resolution, attended by the chief executive, with a written record. Not to manage the work, but to make it unmistakable that this is the priority and that the person at the top is watching. Attendance is the signal; the review is the mechanism.

## The two failure modes

The first is dilution: the decision is reinterpreted by each function into something it was already doing. The second is displacement: a new crisis arrives and the resolution quietly stops. Both are prevented by the same thing, the chief executive's visible attention, and both are the reason senior support alongside the executives carrying the decision is worth more in these ninety days than in any other period.
""",
),
]

# --------------------------------------------------------------------------
BRING = dict(
    title="Bring a Challenge | AATTRL",
    desc="Describe the problem on your desk in a few lines. The AATTRL principal replies personally, in confidence, usually within two working days.",
    h1="Bring a challenge",
    lead="Describe the situation in a few lines, as you see it. The principal reads every message personally and replies in confidence, usually within two working days, with an honest view of whether AATTRL is the right firm to take it on.",
    aside_h="What happens next",
    aside=[
        "A confidential conversation with the principal, in person or online, at a time that suits you.",
        "Within a few days, a one-page brief: the problem as we understand it, what resolution would look like, who we propose and the terms.",
        "No obligation at any point before the brief is agreed. A non-disclosure agreement is available before the first conversation.",
    ],
    direct_h="Prefer to speak directly?",
)

CONTACT = dict(
    title="Contact AATTRL",
    desc="Contact AATTRL by email or WhatsApp. For a problem you would like taken on, use the bring-a-challenge page.",
    h1="Contact",
    lead="For a problem you would like AATTRL to take on, the quickest route is to [bring a challenge](/bring-a-challenge/). For anything else, use the form or write directly.",
)

THANK_YOU = dict(
    title="Message received | AATTRL",
    desc="Your message has reached AATTRL.",
    h1="Your message has reached us.",
    lead="The principal will reply personally, usually within two working days. If the matter is urgent, write to info@aattrl.com or send a WhatsApp message and say so.",
)

PRIVACY = dict(
    title="Privacy | AATTRL",
    desc="How AATTRL handles the information you send through this website.",
    h1="Privacy",
    lead="This site collects only what you send it, and uses it only to reply to you.",
    body="""
## What is collected

The forms on this site collect the details you enter: your name, email address, organisation, role and the message you write. Submissions are delivered to AATTRL by the site's hosting provider, Netlify, and are read by the principal. No account is created and no marketing list is built from them.

## Analytics and cookies

This site does not set analytics cookies and does not run third-party advertising or tracking scripts. The hosting provider keeps standard server logs for security and reliability.

## Confidentiality

Anything you tell AATTRL about your business is treated as confidential from the first message. A non-disclosure agreement can be signed before any substantive conversation.

## Your information

To ask what AATTRL holds about you, or to have it deleted, write to info@aattrl.com.
""",
)

NOT_FOUND = dict(
    title="Page not found | AATTRL",
    h1="That page is not here.",
    lead="The address may have changed. The site was reorganised in October 2026 around the problems AATTRL takes on; the links below will get you to the right place.",
)

# Old URLs (engineering-era site) -> new destinations. Netlify 301s.
REDIRECTS = [
    ("/services/*", "/engagements/"),
    ("/industries/*", "/who-we-serve/"),
    ("/experts/*", "/about/"),
    ("/training/", "/engagements/"),
    ("/request-expert/", "/bring-a-challenge/"),
    ("/request-proposal/", "/bring-a-challenge/"),
    ("/join-expert-network/", "/network/"),
    ("/insights/what-is-a-hazop-study/", "/insights/"),
    ("/insights/hazid-vs-hazop/", "/insights/"),
    ("/insights/feed-to-operations-project-lifecycle/", "/insights/"),
    ("/insights/operational-readiness-checklist/", "/insights/"),
    ("/insights/plant-start-up-checks/", "/insights/"),
    ("/insights/rcm-vs-preventive-maintenance/", "/insights/"),
    ("/insights/technical-due-diligence-checklist/", "/insights/"),
]
