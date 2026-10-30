"""All copy for www.aattrl.com. Edit here, then run `python3 _build/build.py`.

Body text is Markdown. Keep claims factual: no invented members, numbers or quotes.
The platform is in its founding phase and the copy says so.
"""

SITE = dict(
    name="AATTRL",
    legal_name="AATTRL",
    url="https://www.aattrl.com",
    tagline="Industry within nature's limits",
    descriptor="AATTRL is a global platform that brings every stakeholder of industry together to move it to net zero, closer to nature and towards zero impact.",
    email="info@aattrl.com",
    phone_display="+971 50 607 4374",
    wa_number="971506074374",
    regions="Founded in the UAE and India. Open to the world.",
    enaivu_url="https://enaivu.com",
)

NAV = [
    ("Mission", "/mission/"),
    ("Stakeholders", "/stakeholders/"),
    ("Pathways", "/pathways/"),
    ("Programmes", "/programmes/"),
    ("The Pledge", "/pledge/"),
    ("Knowledge", "/knowledge/"),
]
CTA = ("Join the platform", "/join/")

FOOTER_COLUMNS = [
    ("Platform", [("Mission", "/mission/"), ("Stakeholders", "/stakeholders/"), ("Pathways", "/pathways/"), ("Programmes", "/programmes/"), ("Events", "/events/")]),
    ("Take part", [("Join as an individual", "/join/"), ("Sign the Pledge", "/pledge/"), ("Knowledge", "/knowledge/"), ("Contact", "/contact/")]),
    ("AATTRL", [("About", "/about/"), ("Privacy", "/privacy/"), ("Enaivu, software by AATTRL", SITE["enaivu_url"])]),
]

# --------------------------------------------------------------------------
HOME = dict(
    title="AATTRL | A Global Platform for Industry Within Nature's Limits",
    desc="AATTRL brings every stakeholder of industry, operators, engineers, investors, regulators, researchers, workers and communities, together to move industry to net zero, closer to nature and towards zero impact.",
    h1="Industry can run within nature's limits. It takes all of us.",
    lead="Industry made the modern world and is responsible for about a quarter of the emissions now changing it. Fixing that is not one company's job, one government's job or one technology's job. AATTRL is a platform where every stakeholder of industry works on it together.",
    horizons_h="Three horizons, one direction",
    horizons=[
        ("Net zero", "Industrial emissions brought to net zero: energy efficiency first, then electrification and clean fuels, with removals only for what cannot be avoided."),
        ("Close to nature", "Sites that give back more than they take: water returned clean, land restored, biodiversity protected and measured like any other asset."),
        ("Zero impact", "Materials kept in use, waste designed out, and no harm to the people who work in industry or live beside it."),
    ],
    who_h="Built for every stakeholder, not just the operator",
    who_p="A plant does not reach net zero alone. It needs the engineer who designs the change, the investor who funds it, the regulator who sets the rule, the university that proves the method, the worker who runs it and the community that lives with it. AATTRL gives each of them a place on the same platform.",
    how_h="What the platform does",
    how=[
        ("Convenes", "Brings stakeholders who rarely sit together into working groups, roundtables and convenings, by pathway, by sector and by region."),
        ("Commits", "Asks organisations to sign the AATTRL Pledge: a public baseline, a dated target, annual progress and a commitment to nature and people."),
        ("Shares", "Collects what has worked on real sites, in plain language, and makes it available to anyone who will use it."),
        ("Verifies", "Connects experienced engineers and researchers to review transition plans independently, so targets are real and progress is honest."),
    ],
    founding_h="The founding phase",
    founding_p="AATTRL is being built in the open. The first members, working groups and pledge signatories are being gathered now, starting in India and the GCC, where industry is growing fastest and the stakes are highest. If you work in, with, for or beside industry, this is the moment to join.",
    cta_h="Take your place on the platform",
    cta_p="Join as an individual, or sign the Pledge on behalf of your organisation. Both are free in the founding phase.",
)

# --------------------------------------------------------------------------
MISSION = dict(
    title="Mission: Net Zero, Close to Nature, Zero Impact | AATTRL",
    desc="Why AATTRL exists, what the three horizons mean in practice, and the principles the platform runs on.",
    h1="Industry within nature's limits",
    lead="Industry is where the world's materials, energy and products are made. It is also where a large share of emissions, water use, waste and habitat loss comes from. AATTRL exists to bring industry back within the limits of the natural world, without pretending that the world can do without it.",
    body="""
## Why this, why now

Industry accounts for roughly a quarter of global greenhouse-gas emissions directly, and more than a third once the electricity and heat it buys are counted ([IPCC AR6 Working Group III, 2022](https://www.ipcc.ch/report/ar6/wg3/)). The science is settled on the direction: global carbon-dioxide emissions must reach net zero around mid-century to hold warming near 1.5 °C. The technology for most of the industrial transition exists. What is missing is coordination: between the people who own the assets, the people who can change them, the people who pay for it, the people who regulate it and the people who live with it.

That coordination does not happen by itself. Each stakeholder meets the others only at the edges: a tender, a permit, a protest, a conference. AATTRL is built to be the place where they meet in the middle, on the work.

## The three horizons

**Net zero.** Industrial emissions, scope 1 and 2 first and scope 3 as methods mature, brought to net zero on a dated path. The order matters: efficiency before new supply, electrification and clean fuels before offsets, removals only for what cannot be avoided.

**Close to nature.** Industrial sites that are part of their landscape rather than a hole in it. Water drawn and returned clean. Land restored, not just reclaimed. Biodiversity around the site measured and reported as seriously as production. Buffers, corridors and habitats designed in, not fenced off.

**Zero impact.** Materials kept in use through design, reuse, remanufacture and recycling. Waste designed out of processes rather than managed at the end of them. No harm to the people who work in industry or beside it: safety, health and livelihoods treated as part of the same transition.

## Principles

- **Every stakeholder has a seat.** Operators, providers, investors, regulators, researchers, professionals, workers, communities and innovators. The platform is designed around all eight, not around one.
- **Practice over pledges.** Commitments matter only when they are followed by a baseline, a plan and public progress. The Pledge is built that way.
- **Honest numbers.** Targets are checked by people with no stake in the answer. Progress is reported as it is, including when it is behind.
- **Open knowledge.** What works on one site is shared so that it can work on the next. Nothing on the platform is paywalled.
- **Independent.** AATTRL does not sell carbon credits, certify products or take fees from vendors for placement. Its independence is what makes its reviews worth having.
- **Start where the stakes are highest.** India and the GCC first, because industry there is growing fastest and decisions made now will stand for decades. Then everywhere.
""",
)

# --------------------------------------------------------------------------
STAKEHOLDERS_HUB = dict(
    title="Stakeholders of Industry: Who the Platform Is For | AATTRL",
    desc="Eight stakeholder groups, one platform: operators, engineering and technology providers, investors, governments, universities, professionals, workers and communities, and innovators.",
    h1="Eight stakeholders, one platform",
    lead="Each group holds a piece of the transition. None can finish it alone. Each page describes what that stakeholder brings, what it needs from the others, and how to take part.",
)

STAKEHOLDERS = [
dict(
    slug="operators", name="Industry operators and asset owners",
    short="The companies that own and run plants, networks, fleets and mines. The transition happens on their sites or not at all.",
    title="For Industry Operators and Asset Owners | AATTRL",
    desc="How industrial operators and asset owners use the AATTRL platform: baseline, target, plan, independent review, and access to the engineers, financiers and researchers who can help.",
    h1="For the people who run industry",
    lead="Operators carry the transition. They also carry the production targets, the maintenance backlog and the balance sheet. The platform exists to make the transition the operator's easiest path, not an extra burden on top of everything else.",
    body="""
## What you bring

The assets, the data, the operating knowledge and the decisions. Nothing moves until an operator decides it will.

## What you get

- A structured way to set a baseline, a dated target and a plan, using the Pledge framework, without hiring a consultancy to tell you what it is.
- Independent review of that plan by engineers and researchers who have no product to sell you.
- Direct access to technology providers, financiers and universities working on the problems your sites have, in working groups by pathway and sector.
- Case material from other operators: what was done, what it cost, what it saved, what went wrong.
- A voice in the regulatory conversation, alongside the regulators, rather than after them.

## How to take part

Sign the [Pledge](/pledge/) on behalf of a site, a business unit or the whole company. Nominate the people who will represent you in working groups. Share one thing that has worked.
""",
    needs=["Engineering and technology providers with proven methods", "Finance structured for long-payback efficiency and electrification", "Regulators who set clear, stable rules", "Universities to validate methods and train people"],
),
dict(
    slug="providers", name="Engineering, technology and solution providers",
    short="EPCs, OEMs, engineering consultancies, digital and process technology companies. They turn intent into installed change.",
    title="For Engineering, Technology and Solution Providers | AATTRL",
    desc="How engineering firms, OEMs and technology providers take part in the AATTRL platform: working groups with operators, demonstration projects and honest performance data.",
    h1="For the people who build the change",
    lead="Engineering firms and technology providers know what is possible and what it costs. They are also, too often, met with suspicion because they have something to sell. The platform gives them a place to contribute on the merits.",
    body="""
## What you bring

Methods, equipment, software and delivery capability. The practical knowledge of what has been installed, where, and how it performed.

## What you get

- Working groups where operators describe real problems before a tender exists.
- Demonstration and pilot opportunities with operators and universities, with results published whether they succeed or not.
- A performance record on the platform built from independently reviewed project outcomes, which is worth more than a brochure.
- Early sight of regulatory direction, and a channel to inform it.

## The rule

Providers take part as contributors, not sponsors. AATTRL takes no placement fees and gives no preferred listings. A provider's standing on the platform comes from reviewed results.

## How to take part

[Join](/join/) individually, or sign the [Pledge](/pledge/) as an organisation, which for providers means committing to publish performance data for the solutions you supply.
""",
    needs=["Operators willing to pilot and publish results", "Universities to validate performance claims", "Investors who understand the technology risk"],
),
dict(
    slug="investors", name="Investors and finance",
    short="Banks, funds, development finance, insurers and corporate treasuries. The transition is capital-intensive and they decide what gets funded.",
    title="For Investors and Finance | AATTRL",
    desc="How investors, lenders and insurers use the AATTRL platform: reviewed transition plans, a pipeline of real projects, and technical judgement they can rely on.",
    h1="For the people who fund it",
    lead="The industrial transition is a capital problem as much as a technical one. Investors want projects they can assess; operators want capital on terms that match the long paybacks of efficiency, electrification and restoration. The platform puts both in the same room with the engineers who can judge the risk.",
    body="""
## What you bring

Capital, structures and the discipline of asking whether a plan is credible.

## What you get

- Transition plans that have been through independent technical review before they reach you.
- A pipeline of projects from pledged operators, by pathway, sector and region.
- Access to engineers and researchers who can assess technology and execution risk, not just financial risk.
- Working groups on finance structures for industrial decarbonisation and nature restoration: what has worked in India, the GCC and elsewhere.

## How to take part

[Join](/join/) individually, or sign the [Pledge](/pledge/) as an institution, which for finance means committing to report the share of industrial lending or investment aligned with net-zero and nature goals.
""",
    needs=["Operators with reviewed, bankable plans", "Regulators with stable policy", "Engineers who can assess technical risk independently"],
),
dict(
    slug="governments", name="Governments and regulators",
    short="Ministries, regulators, industrial zones and municipalities. They set the rules, the incentives and the timelines.",
    title="For Governments and Regulators | AATTRL",
    desc="How governments, regulators and industrial-zone authorities take part in the AATTRL platform: direct dialogue with industry, evidence from real sites, and policy tested before it is set.",
    h1="For the people who set the rules",
    lead="Regulation works best when the regulated understand it and the regulator understands what is possible. The platform offers a working relationship between the two that is neither lobbying nor enforcement: shared evidence, early dialogue and policy tested against real sites.",
    body="""
## What you bring

Authority, timelines, incentives and the public interest.

## What you get

- Evidence from pledged sites about what measures cost and deliver, to inform standards and incentives.
- Early dialogue with operators, providers and financiers on proposed rules, before positions harden.
- Independent technical input from engineers and researchers with no commercial stake.
- Regional chapters, starting in India and the GCC, where industrial-zone authorities, ministries and industry can work on the same plan.

## How to take part

Government and regulatory bodies take part as observers or members of regional chapters and working groups. [Contact the platform](/contact/) to discuss participation.
""",
    needs=["Honest data from operators", "Independent technical advice", "A forum that is not a lobby"],
),
dict(
    slug="universities", name="Universities and research",
    short="Research groups, institutes and teaching departments. They prove what works, train who does it, and keep everyone honest.",
    title="For Universities and Research Institutions | AATTRL",
    desc="How universities and research institutes take part in the AATTRL platform: industry problems to work on, access to sites and data, and a route from research to installed practice.",
    h1="For the people who prove it",
    lead="Universities hold the methods, the measurement and the next generation of engineers. What they often lack is access: to sites, to data, to the problems industry actually has. The platform is built to close that gap in both directions.",
    body="""
## What you bring

Research capability, measurement and validation, independent judgement, and students.

## What you get

- Real industrial problems, posed by operators in working groups, with sites and data to work on.
- A role in independent review of transition plans and technology performance.
- Industry partners for applied projects, pilots and field trials.
- A route for research findings to reach the people who can install them.
- Guest lectures, industry projects and placements for students, drawn from the platform's members.

## How to take part

[Join](/join/) individually as a researcher or lecturer, or sign the [Pledge](/pledge/) as an institution, which for universities means committing research time to platform working groups and reviews.
""",
    needs=["Access to sites and operating data", "Industry partners for applied research", "Funding routes for pilots"],
),
dict(
    slug="professionals", name="Professionals and experts",
    short="Engineers, scientists, safety and environmental specialists, project and operations leaders. The transition is delivered by people with experience.",
    title="For Professionals and Experts | AATTRL",
    desc="How engineers, scientists and industrial professionals take part in the AATTRL platform: working groups, independent reviews, mentoring and a community of practice.",
    h1="For the people with the experience",
    lead="Much of what the transition needs is already known by people who have spent careers in industry: how a plant really runs, what a retrofit really involves, which numbers to trust. The platform gives that experience a place to be used.",
    body="""
## What you bring

Judgement earned in practice: in design, projects, commissioning, operations, maintenance, safety, environment and management.

## What you get

- Working groups by pathway and sector where that judgement shapes what is done.
- A role in independent reviews of transition plans and technology performance.
- A community of practice across India, the GCC and internationally.
- Opportunities to teach, mentor and lecture through the platform's university members.
- Recognition for contribution, on a platform where standing comes from reviewed work.

## How to take part

[Join as an individual](/join/). Say what you know and which pathways you want to work on.
""",
    needs=["Problems worth working on", "Operators who will act on advice", "Peers across disciplines"],
),
dict(
    slug="communities", name="Workers and communities",
    short="The people who work in industry and the people who live beside it. They carry the impact and should share the benefit.",
    title="For Workers and Communities | AATTRL",
    desc="How workers, unions, community organisations and civil society take part in the AATTRL platform: a seat in the working groups, access to site information, and a transition that includes them.",
    h1="For the people who live with it",
    lead="Industry's impact lands first on the people who work inside it and the people who live around it. A transition designed without them tends to fail, or to succeed at their expense. The platform gives workers and communities a seat at the table, not a consultation at the end.",
    body="""
## What you bring

Lived knowledge of the site and its effects, the skills that run it, and the legitimacy without which no transition lasts.

## What you get

- A place in working groups on the pathways that affect you most: people and just transition, water and ecosystems, nature-positive sites.
- Plain-language information about pledged sites in your area: what they have committed to and how they are doing.
- A channel to operators and regulators that does not depend on protest.
- Skills and training routes as jobs change, through the platform's university and operator members.

## How to take part

[Join](/join/) individually, or as an organisation representing workers or a community. Membership is free.
""",
    needs=["Information in plain language", "Operators who engage before deciding", "Training for the jobs that come next"],
),
dict(
    slug="innovators", name="Startups and innovators",
    short="New companies with new methods: materials, processes, sensors, software, biology. They need sites to prove it on.",
    title="For Startups and Innovators | AATTRL",
    desc="How startups and innovators take part in the AATTRL platform: real industrial problems, pilot sites, honest validation and introductions to operators and investors.",
    h1="For the people with the new idea",
    lead="Most industrial innovation fails not in the laboratory but in the gap between a demonstration and a plant that will try it. The platform is built to close that gap: operators with a stated problem, universities to validate, investors watching, and results published.",
    body="""
## What you bring

New methods and the willingness to test them where it is hard.

## What you get

- Operators' stated problems, by pathway and sector, before anyone has written a tender.
- Pilot and field-trial opportunities with pledged operators and university partners.
- Independent validation of results, published on the platform.
- Visibility to investors who are looking for exactly this.

## The rule

The same as for established providers: contributors, not sponsors. Standing comes from reviewed results.

## How to take part

[Join](/join/) and describe what you have and what you need to prove it.
""",
    needs=["A site willing to pilot", "Independent validation", "Patient capital"],
),
]

# --------------------------------------------------------------------------
PATHWAYS_HUB = dict(
    title="Pathways to Net Zero, Nature and Zero Impact | AATTRL",
    desc="Six pathways along which industry moves within nature's limits: net-zero operations, clean energy and fuels, circular materials, water and ecosystems, nature-positive sites, people and just transition.",
    h1="Six pathways",
    lead="The transition is one direction with several roads. Each pathway has its own working group, its own knowledge and its own measures of progress. Most sites will travel more than one at a time.",
)

PATHWAYS = [
dict(
    slug="net-zero-operations", name="Net-zero operations", horizon="Net zero",
    short="Energy efficiency, process heat, electrification and the honest handling of what cannot yet be avoided.",
    title="Net-Zero Operations: The Pathway for Industrial Sites | AATTRL",
    desc="How an industrial site moves to net-zero operations: efficiency first, electrification and clean heat, emissions that cannot yet be avoided handled honestly.",
    h1="Net-zero operations",
    lead="The first and largest pathway. Most industrial emissions come from burning fuel for heat and power and from process chemistry. The order of work is well established: use less, electrify what can be electrified, switch fuels for what cannot, and be honest about the remainder.",
    body="""
## What it covers

- Energy efficiency across process, utilities and buildings: the cheapest tonne is the one not emitted.
- Process heat: heat pumps, electric boilers and furnaces, thermal storage, and the sequencing of their introduction.
- Electrification of drives, vehicles and material handling.
- Process emissions in cement, steel, chemicals and refining, and the technologies that address them.
- Measurement: a baseline that can be audited, and progress reported the same way every year.
- Residual emissions: what carbon capture and removals can and cannot do, and how to avoid using them as an excuse.

## What the working group does

Operators bring sites and data; engineers and providers bring methods; universities validate; investors watch for projects. Outputs are shared case studies, a practical sequencing guide for sites in India and the GCC, and reviewed plans for pledged operators.

## Measures of progress

Absolute scope 1 and 2 emissions against a published baseline; energy intensity per unit of output; share of heat and power from clean sources.
""",
),
dict(
    slug="clean-energy", name="Clean energy and fuels", horizon="Net zero",
    short="Renewable power, storage, green hydrogen and the fuels that will replace gas and coal in industrial processes.",
    title="Clean Energy and Fuels for Industry | AATTRL",
    desc="The clean energy and fuels pathway: renewable supply for industrial sites, storage, green hydrogen and alternative fuels, and the grid and policy conditions they need.",
    h1="Clean energy and fuels",
    lead="Electrification only helps if the electricity is clean, and some processes will need a fuel for a long time yet. This pathway is about the supply side: renewable power for industry, storage, green hydrogen and the fuels and infrastructure that make them usable.",
    body="""
## What it covers

- On-site and contracted renewable power for industrial sites, and the regulatory conditions that make it work.
- Storage, firming and the economics of running industrial processes on variable supply.
- Green hydrogen and its derivatives: where they are the right answer, where they are not, and what they cost.
- Alternative fuels for high-temperature and mobile applications.
- Industrial-zone-scale energy systems, which matter especially in the GCC and India.

## What the working group does

Brings operators, energy developers, grid operators, regulators and financiers together on specific sites and zones. Outputs are case studies, zone-level studies and reviewed supply plans for pledged operators.

## Measures of progress

Share of a site's energy from clean sources; contracted clean capacity; cost per unit delivered.
""",
),
dict(
    slug="circular-materials", name="Circular materials and zero waste", horizon="Zero impact",
    short="Design for reuse, remanufacture and recycling; waste designed out of processes; by-products that become inputs.",
    title="Circular Materials and Zero Waste in Industry | AATTRL",
    desc="The circular materials pathway: keeping materials in use, designing waste out of industrial processes, and turning by-products into inputs for other industries.",
    h1="Circular materials and zero waste",
    lead="Zero impact begins with materials. Every tonne of input that is kept in use is a tonne that does not have to be mined, made and moved again. This pathway is about designing waste out of industry rather than managing it at the end.",
    body="""
## What it covers

- Material efficiency in process and product design.
- Reuse, remanufacture and recycling at industrial scale, and the reverse logistics they need.
- Industrial symbiosis: one plant's by-product as another's feedstock, especially within industrial zones.
- Hazardous and process waste: elimination first, then safe treatment.
- Measurement: material flows, waste intensity and recycled content, reported consistently.

## What the working group does

Maps material flows in participating zones and sectors, matches by-products to uses, and shares what has worked. Outputs are zone-level symbiosis maps, case studies and reviewed material plans for pledged operators.

## Measures of progress

Waste to landfill per unit of output; recycled or reused share of input; by-product utilisation.
""",
),
dict(
    slug="water-and-ecosystems", name="Water and ecosystems", horizon="Close to nature",
    short="Water drawn responsibly and returned clean; rivers, aquifers, coasts and wetlands protected around industrial sites.",
    title="Water and Ecosystems Around Industrial Sites | AATTRL",
    desc="The water and ecosystems pathway: water stewardship for industrial sites, discharge quality, and the protection of rivers, aquifers, coasts and wetlands they depend on.",
    h1="Water and ecosystems",
    lead="Industry depends on water and often sits beside the ecosystems that provide it. In India and the GCC water stress is already acute. This pathway is about drawing less, returning it clean, and treating the river, aquifer or coast as a stakeholder in its own right.",
    body="""
## What it covers

- Water balance and efficiency: measuring, reducing and recycling process and cooling water.
- Discharge quality beyond compliance, and zero liquid discharge where it is the right answer.
- Shared water resources: catchment-level cooperation between industrial users, agriculture and communities.
- Ecosystems around sites: rivers, groundwater, coasts, mangroves and wetlands, monitored and protected.
- Desalination and its energy and brine implications, which matter especially in the Gulf.

## What the working group does

Brings operators, water utilities, regulators, researchers and communities together at catchment level. Outputs are catchment studies, case material and reviewed water plans for pledged operators.

## Measures of progress

Freshwater withdrawal per unit of output; share recycled; discharge quality; ecosystem indicators agreed with local stakeholders.
""",
),
dict(
    slug="nature-positive-sites", name="Nature-positive sites", horizon="Close to nature",
    short="Industrial sites designed into their landscape: habitats, corridors, soil and restoration treated as part of the asset.",
    title="Nature-Positive Industrial Sites | AATTRL",
    desc="The nature-positive sites pathway: designing and operating industrial sites so that they restore more than they take, with land, habitats and biodiversity measured and managed.",
    h1="Nature-positive sites",
    lead="An industrial site occupies land for decades. It can be a wound in the landscape or part of it. This pathway is about site design and operation that restores habitat, protects biodiversity and leaves the land better than it was found.",
    body="""
## What it covers

- Site design: buffers, corridors, native planting, soil and drainage treated as engineering, not landscaping.
- Biodiversity baselines and monitoring around operating sites.
- Restoration of disturbed and decommissioned land, including mines and legacy sites.
- Nature-related disclosure, and how to do it without greenwash.
- Working with communities and ecologists as partners in the site's management.

## What the working group does

Pairs operators with ecologists, universities and local organisations on specific sites. Outputs are design guidance for new and existing sites, case studies and reviewed nature plans for pledged operators.

## Measures of progress

Area restored; habitat and species indicators agreed for each site; share of site land under active ecological management.
""",
),
dict(
    slug="people-and-just-transition", name="People and just transition", horizon="Zero impact",
    short="Workers and communities through the change: safety, health, skills, livelihoods and a fair share of the benefit.",
    title="People and a Just Transition in Industry | AATTRL",
    desc="The people and just transition pathway: workers and communities through the industrial transition, with safety, health, skills, livelihoods and fair benefit built in.",
    h1="People and just transition",
    lead="Zero impact includes people. A transition that closes a plant without a plan for its workers, or cleans a site while the community beside it is still unheard, is not one AATTRL will call a success. This pathway keeps people in the plan.",
    body="""
## What it covers

- Safety and health through change: new processes, new fuels and new hazards.
- Skills: what the transition needs and how existing workers get there.
- Livelihoods and communities where industry is changing or closing.
- Community engagement that starts before decisions, not after.
- Fair distribution of the benefits: jobs, local supply, shared infrastructure.

## What the working group does

Brings operators, unions and worker representatives, community organisations, universities and governments together on specific sites and regions. Outputs are practical guidance, case studies and reviewed people plans for pledged operators.

## Measures of progress

Safety and health indicators; workers trained for transition roles; community engagement that can be shown, not asserted.
""",
),
]

# --------------------------------------------------------------------------
PROGRAMMES = dict(
    title="Programmes: Working Groups, Reviews, Chapters and Convenings | AATTRL",
    desc="How the AATTRL platform works in practice: pathway working groups, independent transition reviews, industry–academia projects, regional chapters and convenings.",
    h1="How the platform works",
    lead="Five programmes turn the mission into work. All of them are open to members. All of them are starting in the founding phase, and members shape them.",
    items=[
        ("working-groups", "Pathway working groups", "One working group per [pathway](/pathways/), with sector sub-groups where needed. Members from every stakeholder group work on specific problems brought by operators: a site, a zone, a process. Groups meet online monthly and in person at convenings. Outputs are published on the platform: case studies, guidance and the problems still open."),
        ("reviews", "Independent transition reviews", "Experienced engineers and researchers from the platform review an organisation's baseline, target and plan, and say in writing whether they are credible. Reviews are required for Pledge signatories within their first year and available to any member organisation. Reviewers have no commercial stake in the outcome and declare any connection."),
        ("projects", "Industry–academia projects", "Applied research, pilots and field trials matched between operator members and university members, with providers and innovators where a method is being tested. Results are published whether or not they succeed, because a documented failure saves the next site the cost of repeating it."),
        ("chapters", "Regional chapters", "The platform is global; the work is local. Chapters bring the stakeholders of one region together on its own industry, water, grid and rules. The first chapters are India and the GCC. Further chapters open where members ask for them and will lead them."),
        ("convenings", "Convenings", "A global convening each year, regional roundtables, monthly online pathway sessions and campus sessions at member universities. Formats and the first programme of dates are on the [events page](/events/)."),
    ],
    note="AATTRL does not charge for membership or programmes in the founding phase. How the platform is funded over the long term, by members, grants and institutional partners, will be decided with the founding members and published.",
)

# --------------------------------------------------------------------------
PLEDGE = dict(
    title="The AATTRL Pledge for Organisations | AATTRL",
    desc="The AATTRL Pledge: a public baseline, a dated net-zero target with interim milestones, annual progress, commitments on nature and people, and shared knowledge. Open to operators, providers, investors, universities and public bodies.",
    h1="The Pledge",
    lead="Signing the Pledge is how an organisation takes its place on the platform. It is short, public and specific, and it is followed by an independent review within the first year. It costs nothing to sign and something to keep.",
    commitments_h="What a signatory commits to",
    commitments=[
        ("A public baseline", "Within twelve months of signing, publish a baseline of scope 1 and 2 emissions, water withdrawal and waste for the signed scope, with the method stated."),
        ("A dated target", "A net-zero target for the signed scope with interim milestones at no more than five-year intervals, and the first actions named."),
        ("Nature and water", "Commitments specific to the sites in scope: water returned clean, land and biodiversity around the site measured and protected."),
        ("People", "Commitments to the safety, skills and livelihoods of workers and to engagement with the communities beside each site, before decisions rather than after."),
        ("Annual progress", "Progress published on the platform every year against the baseline, including where it is behind, and an independent review within the first year."),
        ("Shared knowledge", "At least one documented case per year of what was done, what it cost and what it delivered, for other members to use."),
    ],
    by_type_h="What the Pledge means for each stakeholder",
    by_type=[
        ("Operators", "The commitments above, for a site, a business unit or the whole company."),
        ("Engineering and technology providers", "Published performance data for the solutions supplied, and the baseline and target for the provider's own operations."),
        ("Investors and finance", "Published share of industrial lending or investment aligned with net-zero and nature goals, and a target for it."),
        ("Universities and research", "Committed research time to platform working groups and reviews, and the baseline and target for the campus."),
        ("Governments and public bodies", "Participation in a regional chapter and publication of the industrial-zone or jurisdiction's own baseline and target."),
    ],
    review_h="Independent review",
    review_p="Every signatory's baseline, target and plan is reviewed within the first year by platform members with the relevant experience and no stake in the outcome. The review says in writing whether the target is credible and the plan sufficient. A signatory whose plan is found wanting is helped to fix it, not expelled; a signatory that does not publish is removed from the register.",
    register_h="The register",
    register_p="Signatories are listed publicly on the platform with their scope, baseline date, target and latest progress. The register opens with the founding signatories; organisations that sign now are founding signatories.",
)

# --------------------------------------------------------------------------
EVENTS = dict(
    title="Events and Convenings | AATTRL",
    desc="AATTRL convenings: the annual global convening, regional roundtables in India and the GCC, monthly online pathway sessions and campus sessions.",
    h1="Convenings",
    lead="The platform meets in four formats. The first programme of dates will be published here and sent to members; join to be told.",
    formats=[
        ("Global convening", "Once a year, in person with online participation. All stakeholders, all pathways: the state of the transition, the year's reviewed cases, the open problems, and the next year's working-group agenda. The first will be held in India or the GCC."),
        ("Regional roundtables", "Chapter-level, several times a year. The stakeholders of one region on its own industry, water, grid and rules. Small enough to work; attended by the people who decide."),
        ("Pathway sessions", "Monthly, online, one per pathway. A site or a problem brought by an operator, worked through by the group. Open to all members of the working group."),
        ("Campus sessions", "At member universities: lectures and workshops by industry members for students and faculty, and research presentations to industry. Arranged with each university's department."),
    ],
    note="Members can propose a roundtable or a campus session for their region or institution through the platform.",
)

# --------------------------------------------------------------------------
KNOWLEDGE_HUB = dict(
    title="Knowledge: Practical Guidance for the Industrial Transition | AATTRL",
    desc="Short, practical pieces on how industry moves to net zero, closer to nature and towards zero impact: baselines, targets, site design, the first year of a plan, and why every stakeholder matters.",
    h1="Knowledge",
    lead="Short, practical pieces for people doing the work. Case studies from member sites will appear here as the working groups publish them. Nothing on this page is paywalled.",
)

KNOWLEDGE = [
dict(
    slug="what-net-zero-means-for-an-industrial-site",
    name="What net zero means for an industrial site, in practice",
    date="2026-10-31", minutes=6,
    desc="Net zero is a national slogan until it is translated into a site. Here is what it means for one plant: a boundary, a baseline, a sequence and an honest remainder.",
    body="""
Net zero is easy to say about a country and hard to say about a plant. A plant has a fence, a meter, a fuel bill and a production target. Translating the slogan into those terms is the first real step, and most organisations have not taken it.

## Draw the boundary

Decide what is in scope: the site, the business unit, the company. Decide which emissions are in: scope 1 (fuel burned and process emissions on site), scope 2 (electricity and heat bought in), and, for now, which parts of scope 3 you will count. A narrow boundary honestly stated is worth more than a wide one vaguely drawn.

## Measure the baseline

One year, measured, with the method written down: fuel quantities, electricity purchased, process emissions calculated by a stated factor. Water withdrawn and waste produced, the same way. This is the number everything else is compared to, so it must be one that an outsider could check.

## Sequence the work

The order is well established and rarely followed. First, efficiency: the tonne not emitted is the cheapest. Second, electrify what can be electrified, which is more than most plants assume. Third, switch fuels for the heat and processes that cannot be electrified yet. Fourth, only then, deal with the remainder through capture or removals. Plants that start at the fourth step are usually avoiding the first three.

## Be honest about the remainder

Some emissions cannot yet be avoided with available technology. Say which ones, how much, and what would change the answer. A target that hides the remainder inside an offset purchase is not a net-zero target; it is a net-zero invoice.

## Publish and repeat

Baseline, target, plan and annual progress, published the same way every year, including the years that go badly. That is what the [Pledge](/pledge/) asks for, and it is what makes a site's net zero mean something.
""",
),
dict(
    slug="industry-close-to-nature-five-principles",
    name="Industry close to nature: five design principles",
    date="2026-10-31", minutes=5,
    desc="A site can be part of its landscape or a hole in it. Five principles for designing and operating industrial sites that give back more than they take.",
    body="""
"Close to nature" is not a planting scheme at the gate. It is a way of designing and running a site so that the land, water and life around it are better for the site being there. Five principles, drawn from sites that have done it.

## 1. Treat the landscape as the client

Before the site layout, understand the catchment, the soil, the wind, the species and the seasons. The site is a tenant in that system. Design it to fit, not to flatten.

## 2. Water in, water out, both measured

Every litre drawn and every litre returned, with its quality. Returned water should be fit for the river, the aquifer or the sea it goes to, not merely compliant. Where the resource is shared, as it is almost everywhere in India and the Gulf, the plan is made with the other users.

## 3. Buffers, corridors and habitats are infrastructure

They are designed, budgeted and maintained like a road or a pipe. Native species, connected to the habitat beyond the fence, with someone accountable for them.

## 4. Measure life like production

A biodiversity baseline before construction or at the start of the commitment; indicators agreed with ecologists and local people; reported every year beside the production figures. What is not measured is not managed.

## 5. Restore more than you disturb

Every site disturbs land. The commitment is to restore more than that, on site or in the same landscape, over the life of the asset, and to leave the land in better condition at closure than at opening. This is the test that separates nature-positive from nature-neutral.

These principles are the basis of the [nature-positive sites pathway](/pathways/nature-positive-sites/), and of the nature commitments in the Pledge.
""",
),
dict(
    slug="the-first-twelve-months-of-a-transition-plan",
    name="The first twelve months of a transition plan",
    date="2026-10-31", minutes=5,
    desc="What a pledged organisation should do in its first year: the baseline, the quick wins, the review and the habit of publishing.",
    body="""
The Pledge gives a signatory twelve months to publish a baseline and a dated target. Here is how to spend them.

## Months one to three: boundary and data

Agree the scope. Find the meters, the invoices and the production records. Where a meter does not exist, install one; where a number must be estimated, write down how. Appoint one person accountable for the numbers.

## Months three to six: the baseline and the obvious wins

Compile the baseline year. While doing so, you will find the leaks, the idling, the compressed air, the steam traps, the lighting. Fix them. The savings pay for the measurement and show the organisation that this is real.

## Months six to nine: the target and the plan

Set the net-zero date and the interim milestones. Sequence the plan: efficiency, electrification, fuel switching, remainder. Add the water, nature and people commitments for each site. Cost it honestly, including the projects you cannot yet fund, and say so.

## Months nine to twelve: review and publish

Submit the baseline, target and plan for independent review. Fix what the reviewers find. Publish, on the platform and in your own reporting, with the method and the gaps stated.

## The habit that matters

Everything above is worth little without the annual repetition. The organisations that get to net zero are not the ones with the best first plan; they are the ones that publish every year and act on what the numbers say.
""",
),
dict(
    slug="how-to-tell-a-real-target-from-a-slogan",
    name="How to tell a real target from a slogan",
    date="2026-10-31", minutes=4,
    desc="Six questions that separate a net-zero commitment from a press release. Useful for investors, regulators, communities and the organisation itself.",
    body="""
Every organisation now has a net-zero statement. Fewer have a net-zero target. Six questions tell them apart; anyone can ask them, and a signatory of the Pledge must be able to answer all six.

1. **What is the boundary?** Which sites, which scopes, which activities. A target without a boundary is a sentiment.

2. **What is the baseline, and when was it measured?** A year, a number, a method. If the answer is a percentage reduction from an unstated base, ask what the base is.

3. **What is the date, and what are the milestones?** Net zero by 2050 with nothing before it is a promise made to someone who will have retired. Milestones at five-year intervals or shorter are what make the target the current management's problem.

4. **What are the first three actions, and are they funded?** If the plan begins with a study, the target has not been taken seriously yet.

5. **How much is the remainder, and how will it be handled?** A target that relies mostly on offsets or future technology has deferred the question, not answered it.

6. **Who checked it?** A target reviewed by people with no stake in the answer is worth more than one reviewed by the people who wrote it.

The [Pledge](/pledge/) is built so that signatories must answer these questions in public. That is the point of it.
""",
),
dict(
    slug="why-every-stakeholder-not-just-the-operator",
    name="Why every stakeholder, not just the operator",
    date="2026-10-31", minutes=5,
    desc="Industrial transitions fail in the gaps between stakeholders. The case for a platform built around all eight of them.",
    body="""
Ask why a good industrial transition plan did not happen and the answer is rarely technical. The technology existed. The money existed. The plan failed in a gap between stakeholders.

## Where plans fail

The operator wanted to electrify and the grid could not supply clean power on the timescale. The provider had a proven method and the operator would not pilot it without a reference, which no one would be. The investor would fund the project with a shorter payback than efficiency offers. The regulator set a rule that made the right answer uneconomic, because no one explained the engineering. The university had the measurement method and no access to the site. The community found out at the public hearing and stopped it. The workers were told at the end.

Each of these is a failure of coordination, not of will or technology. And each stakeholder, acting alone, could not have fixed it.

## Why a platform

The usual answer is a conference, a consultancy or a government committee. Conferences convene without working. Consultancies work for one client. Committees have one chair. None of them gives every stakeholder a standing place on the same work.

A platform does: working groups where the operator's problem is heard by the provider, the financier, the regulator and the researcher at the same time; a pledge that applies to all of them, each in their own terms; reviews done by people with no stake; and knowledge published for whoever will use it.

## Why eight

Because that is how many it takes. Leave out the investor and nothing is funded. Leave out the regulator and the rules fight the plan. Leave out the community and the permit is lost. Leave out the worker and the plant cannot run. AATTRL is designed around [all eight](/stakeholders/) because the transition is.
""",
),
]

# --------------------------------------------------------------------------
ABOUT = dict(
    title="About AATTRL: A Global Platform for Industry Within Nature's Limits",
    desc="AATTRL is a global platform founded by engineer Basheer Thasthakir to bring every stakeholder of industry together on net zero, nature and zero impact. Independent, open and in its founding phase.",
    h1="About AATTRL",
    lead="AATTRL is a global platform for the industrial transition, founded by an engineer who spent twenty years inside the industries that need it most.",
    body="""
## What AATTRL is

A platform, not a consultancy, a certifier or a vendor. It convenes the stakeholders of industry, asks organisations to make public commitments, connects experienced people to review them, and publishes what works. It is open to anyone who works in, with, for or beside industry, anywhere in the world.

## How it came to be

The platform grew out of twenty years spent in asset-heavy industry in India, the Gulf and Europe, in design, project delivery, commissioning, operations and asset management. The pattern was visible from inside: the technology for a cleaner industry existed, the money existed, and the work was stuck in the gaps between operators, engineers, financiers, regulators, researchers and communities who never sat at the same table. AATTRL was founded to be that table.

## Independence

- AATTRL does not sell carbon credits, certify products or take fees from vendors for placement or listing.
- Reviews are done by members with no commercial stake in the outcome, who declare any connection.
- Membership and programmes are free in the founding phase. Long-term funding, by members, grants and institutional partners, will be decided with the founding members and published.
- Software built by AATTRL under the Enaivu name is a separate business and is never required for participation.

## Governance

The platform is in its founding phase. An advisory council drawn from the founding members, one seat per stakeholder group, will be formed in the first year and will set the platform's rules, review standards and funding model. Until then, decisions are taken by the founder and published.
""",
    principal_h="The founder",
    principal=dict(
        name="Basheer Thasthakir",
        role="Founder",
        bio="Basheer Thasthakir is a mechanical engineer with approximately twenty years of international industrial experience across India, Saudi Arabia, the United Arab Emirates and Norway, spanning design, EPC project delivery, commissioning and start-up, operations, maintenance, asset management and digital transformation. He founded AATTRL to bring the stakeholders of industry together on the transition he watched stall from the inside.",
        facts=[("Based", "United Arab Emirates and India"), ("Experience", "Approximately 20 years, international"), ("Countries", "India, Saudi Arabia, UAE, Norway"), ("Background", "Mechanical engineer; asset-heavy industry"), ("Contact", "info@aattrl.com")],
    ),
)

# --------------------------------------------------------------------------
JOIN = dict(
    title="Join the Platform | AATTRL",
    desc="Join AATTRL as an individual: engineer, researcher, investor, official, worker, community member or innovator. Free in the founding phase.",
    h1="Join the platform",
    lead="Membership is for individuals from every stakeholder group and is free in the founding phase. Tell us who you are and which pathways you want to work on. You will be placed in working groups as they form and told about convenings.",
    aside_h="What membership means",
    aside=[
        "A place in the pathway working groups you choose, as they form.",
        "Invitations to convenings, roundtables and pathway sessions.",
        "Access to case material and reviewed plans as they are published.",
        "The opportunity to take part in independent reviews, if you have the experience.",
        "No fee in the founding phase, and no obligation beyond honest participation.",
    ],
    org_h="Signing for an organisation?",
    org_p="Organisations take part by signing [the Pledge](/pledge/#sign).",
)

PLEDGE_FORM = dict(
    h="Sign the Pledge",
    lead="Complete this to begin. The founder will reply within a week to confirm the scope, agree the baseline timeline and explain the review. Founding signatories are listed on the register when it opens.",
)

CONTACT = dict(
    title="Contact AATTRL",
    desc="Contact AATTRL by email or WhatsApp, or use the form. To join, use the join page; to sign the Pledge, use the pledge page.",
    h1="Contact",
    lead="To join as an individual, use [the join page](/join/). To sign the Pledge for an organisation, use [the pledge page](/pledge/#sign). Governments, regulators and press, or anything else, use the form or write directly.",
)

THANK_YOU = dict(
    title="Received | AATTRL",
    desc="Your message has reached AATTRL.",
    h1="Received. Thank you.",
    lead="You will hear from the founder, usually within a week. In the meantime, the mission, the pathways and the knowledge pages are the best places to start.",
)

PRIVACY = dict(
    title="Privacy | AATTRL",
    desc="How AATTRL handles the information you send through this website.",
    h1="Privacy",
    lead="This site collects only what you send it, and uses it only for the platform.",
    body="""
## What is collected

The forms on this site collect the details you enter: your name, email address, organisation, role, stakeholder group, the pathways you choose and the message you write. Submissions are delivered to AATTRL by the site's hosting provider, Netlify, and are read by the founder. Members' details are used to form working groups and to send platform notices. No details are sold or shared with vendors.

## The register

Organisations that sign the Pledge are listed publicly on the register with their name, scope, baseline date, target and progress. Individuals are never listed publicly without their agreement.

## Analytics and cookies

This site does not set analytics cookies and does not run third-party advertising or tracking scripts. The hosting provider keeps standard server logs for security and reliability.

## Your information

To ask what AATTRL holds about you, or to have it deleted, write to info@aattrl.com.
""",
)

NOT_FOUND = dict(
    title="Page not found | AATTRL",
    h1="That page is not here.",
    lead="The site was reorganised around the platform in October 2026; the links below will get you to the right place.",
)

# Old URLs (engineering-era and executive-era sites) -> new destinations. Netlify 301s.
REDIRECTS = [
    # engineering advisory site (to 2026-10-26)
    ("/services/*", "/programmes/"),
    ("/industries/*", "/stakeholders/"),
    ("/experts/*", "/about/"),
    ("/training/", "/programmes/"),
    ("/request-expert/", "/join/"),
    ("/request-proposal/", "/contact/"),
    ("/join-expert-network/", "/join/"),
    # executive problem-solving site (2026-10-26 to 2026-10-31)
    ("/how-it-works/", "/programmes/"),
    ("/challenges/*", "/pathways/"),
    ("/engagements/*", "/programmes/"),
    ("/who-we-serve/", "/stakeholders/"),
    ("/network/", "/join/"),
    ("/bring-a-challenge/", "/join/"),
    ("/insights/*", "/knowledge/"),
]
