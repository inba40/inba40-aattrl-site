#!/usr/bin/env python3
"""Generate www.aattrl.com from _build/content.py into the repository root.

    python3 _build/build.py

Requires: python3, `markdown` (pip install markdown). Output is plain HTML under
URL paths (pathways/net-zero-operations/index.html -> /pathways/net-zero-operations/).
"""
import datetime
import html as H
import json
import pathlib
import sys

import markdown

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import content as C  # noqa: E402

TODAY = datetime.date.today().isoformat()
S = C.SITE
GENERATED = []

MARK = '<svg class="mark" viewBox="0 0 64 64" aria-hidden="true"><path d="M32 12 17 50M32 12l15 38M24 38h16" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><path d="M8 54c10 0 14-6 24-6s14 6 24 6" fill="none" stroke="#2E8C75" stroke-width="3.5" stroke-linecap="round"/></svg>'

def md(text):
    return markdown.markdown(text.strip(), extensions=["smarty"], output_format="html5")

def e(s):
    return H.escape(s, quote=True)

def ld(obj):
    return '<script type="application/ld+json">%s</script>' % json.dumps(obj, ensure_ascii=False)

ORG_LD = {
    "@context": "https://schema.org", "@type": "Organization",
    "name": S["legal_name"], "url": S["url"] + "/", "logo": S["url"] + "/assets/images/apple-touch-icon.png",
    "description": S["descriptor"], "email": S["email"],
    "founder": {"@type": "Person", "name": "Basheer Thasthakir"},
    "areaServed": "Worldwide",
    "knowsAbout": ["Industrial decarbonisation", "Net zero", "Nature-positive industry", "Circular economy", "Just transition"],
}

# --------------------------------------------------------------------------
def header(current):
    items = []
    for label, path in C.NAV:
        cur = ' aria-current="page"' if current.startswith(path) else ""
        items.append('<li><a href="%s"%s>%s</a></li>' % (path, cur, e(label)))
    nav = "".join(items)
    mob = nav + '<li><a href="%s">%s</a></li><li><a href="/events/">Events</a></li><li><a href="/about/">About</a></li><li><a href="/contact/">Contact</a></li>' % (C.CTA[1], e(C.CTA[0]))
    return f'''<a class="skip" href="#main">Skip to main content</a>
<header class="site-header">
  <div class="header-row">
    <a class="brand" href="/" aria-label="AATTRL home">{MARK}AATTRL <small>{e(S["tagline"])}</small></a>
    <nav class="nav" aria-label="Main"><ul>{nav}</ul></nav>
    <a class="btn accent header-cta" href="{C.CTA[1]}">{e(C.CTA[0])}</a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="mobile-nav">Menu</button>
  </div>
  <nav class="mobile-nav" id="mobile-nav" aria-label="Main, mobile" data-open="false"><ul>{mob}</ul></nav>
</header>'''

def footer():
    cols = []
    for title, links in C.FOOTER_COLUMNS:
        lis = "".join('<li><a href="%s"%s>%s</a></li>' % (p, ' rel="noopener"' if p.startswith("http") else "", e(l)) for l, p in links)
        cols.append(f'<div><h2>{e(title)}</h2><ul>{lis}</ul></div>')
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="top">
      <div>
        <a class="brand" href="/">{MARK}AATTRL <small>{e(S["tagline"])}</small></a>
        <p>{e(S["descriptor"])}</p>
        <p><a href="mailto:{S["email"]}">{S["email"]}</a><br><a href="https://wa.me/{S["wa_number"]}" rel="noopener">WhatsApp {e(S["phone_display"])}</a></p>
      </div>
      {"".join(cols)}
    </div>
    <div class="bottom"><span>&copy; {TODAY[:4]} {e(S["legal_name"])}</span><span>{e(S["regions"])}</span></div>
  </div>
</footer>
<script src="/assets/js/main.js" defer></script>'''

def page(path, title, desc, body, noindex=False, lastmod=TODAY, ld_extra=None):
    canonical = S["url"] + path
    robots = '<meta name="robots" content="noindex, nofollow">' if noindex else ""
    lds = ld(ORG_LD) + (ld(ld_extra) if ld_extra else "")
    doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canonical}">
{robots}
<meta property="og:type" content="website">
<meta property="og:site_name" content="AATTRL">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{S["url"]}/assets/images/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#15302A">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/assets/images/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/images/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/assets/fonts/archivo-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/source-serif-4-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/style.css">
{lds}
</head>
<body>
{header(path)}
<main id="main">
{body}
</main>
{footer()}
</body>
</html>
'''
    out = ROOT / path.strip("/") / "index.html" if path != "/404.html" else ROOT / "404.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc, encoding="utf-8")
    if not noindex and path != "/404.html":
        GENERATED.append((path, lastmod))

def crumbs(*items):
    parts = []
    for label, path in items:
        parts.append('<a href="%s">%s</a>' % (path, e(label)) if path else e(label))
    return '<p class="crumbs">' + '<span aria-hidden="true">/</span>'.join(parts) + "</p>"

def page_head(h1, lead, crumb=None, tag=None):
    tag_html = f'<p class="horizon-tag">{e(tag)}</p>' if tag else ""
    return f'<section class="page-head"><div class="wrap">{crumb or ""}{tag_html}<h1>{e(h1)}</h1><div class="lead">{md(lead)}</div></div></section>'

def cta_band(h=None, p=None):
    h = h or C.HOME["cta_h"]; p = p or C.HOME["cta_p"]
    return f'''<section class="section dark cta-band"><div class="wrap">
  <div><h2>{e(h)}</h2><p class="lead">{e(p)}</p></div>
  <div class="actions"><a class="btn accent" href="/join/">Join as an individual</a><a class="btn secondary" style="color:#fff;border-color:rgba(255,255,255,.6)" href="/pledge/#sign">Sign the Pledge</a></div>
</div></section>'''

def curve_svg():
    """The curve to zero: emissions falling to the horizon, then restoration beyond it."""
    return '''<svg class="curve" viewBox="0 0 1120 320" role="img" aria-labelledby="curve-t curve-d">
  <title id="curve-t">The curve to zero</title>
  <desc id="curve-d">Industrial impact rising through the past, bending down to net zero at the horizon, then continuing below it as industry restores more than it takes.</desc>
  <line class="axis" x1="0" y1="190" x2="1120" y2="190"/>
  <text class="sub" x="0" y="212">Horizon: net zero</text>
  <path class="past" d="M0 150 C 120 140, 220 110, 330 78"/>
  <path class="path" d="M330 78 C 460 52, 570 120, 640 190 C 700 250, 800 268, 1120 274"/>
  <circle class="dot" cx="330" cy="78" r="6"/>
  <text class="lbl" x="330" y="56" text-anchor="middle">Today</text>
  <line class="tick" x1="640" y1="190" x2="640" y2="140"/>
  <text class="lbl" x="652" y="140">Net zero</text>
  <text class="sub" x="652" y="160">Emissions to zero</text>
  <line class="tick" x1="900" y1="190" x2="900" y2="265"/>
  <text class="lbl" x="912" y="160">Close to nature</text>
  <text class="sub" x="912" y="180">Sites that give back</text>
  <text class="lbl" x="1120" y="302" text-anchor="end">Zero impact</text>
  <text class="sub" x="0" y="40">Industrial impact</text>
  <text class="sub" x="0" y="60">rising through the past</text>
</svg>'''

def form(name, fields, button, subject, consent_text=None):
    rows = []
    i = 0
    while i < len(fields):
        f = fields[i]
        if f.get("half") and i + 1 < len(fields) and fields[i + 1].get("half"):
            rows.append('<div class="row">%s%s</div>' % (field_html(f), field_html(fields[i + 1]))); i += 2
        else:
            rows.append(field_html(f)); i += 1
    consent = consent_text or 'I understand that this will be read by AATTRL and handled as described in the <a href="/privacy/">privacy note</a>.'
    return f'''<form class="form" name="{name}" method="POST" action="/thank-you/" data-netlify="true" netlify-honeypot="company-website" novalidate>
  <input type="hidden" name="form-name" value="{name}">
  <input type="hidden" name="subject" value="{e(subject)}">
  <p class="hp" aria-hidden="true"><label>Leave this field empty <input type="text" name="company-website" tabindex="-1" autocomplete="off"></label></p>
  {"".join(rows)}
  <div class="field consent"><input type="checkbox" id="{name}-consent" name="consent" value="yes" required><label for="{name}-consent">{consent}</label></div>
  <div class="actions"><button class="btn accent" type="submit">{e(button)}</button></div>
  <p class="note">Submitted details are delivered to AATTRL by the site's hosting provider and are not shared with anyone else.</p>
</form>'''

def field_html(f):
    n = f["name"]; req = ' required' if f.get("required") else ""
    hint = '<span class="hint">%s</span>' % e(f["hint"]) if f.get("hint") else ""
    err = '<p class="error">%s</p>' % e(f.get("error", "Please complete this field."))
    t = f.get("type", "text")
    if t == "textarea":
        ctl = f'<textarea id="{n}" name="{n}"{req}></textarea>'
    elif t == "select":
        opts = "".join('<option value="%s">%s</option>' % (e(o), e(o)) for o in f["options"])
        ctl = f'<select id="{n}" name="{n}"{req}><option value="">Select</option>{opts}</select>'
    elif t == "checks":
        boxes = "".join(f'<label class="check"><input type="checkbox" name="{n}[]" value="{e(o)}"><span>{e(o)}</span></label>' for o in f["options"])
        return f'<fieldset><legend>{e(f["label"])}{hint}</legend><div class="checks">{boxes}</div></fieldset>'
    else:
        ac = ' autocomplete="%s"' % f["ac"] if f.get("ac") else ""
        ctl = f'<input id="{n}" name="{n}" type="{t}"{ac}{req}>'
    return f'<div class="field"><label for="{n}">{e(f["label"])}{hint}</label>{ctl}{err}</div>'

STAKEHOLDER_OPTIONS = [s["name"] for s in C.STAKEHOLDERS]
PATHWAY_OPTIONS = [p["name"] for p in C.PATHWAYS]

# --------------------------------------------------------------------------
def build_home():
    h = C.HOME
    horizons = "".join("<li><h3>%s</h3><p>%s</p></li>" % (e(a), e(b)) for a, b in h["horizons"])
    stakes = "".join('<li><h3><a href="/stakeholders/%s/">%s</a></h3><p>%s</p></li>' % (s["slug"], e(s["name"]), e(s["short"])) for s in C.STAKEHOLDERS)
    how = "".join("<div><dt>%s</dt><dd>%s</dd></div>" % (e(a), e(b)) for a, b in h["how"])
    paths = "".join('<li><h3><a href="/pathways/%s/">%s</a></h3><p>%s</p></li>' % (p["slug"], e(p["name"]), e(p["short"])) for p in C.PATHWAYS)
    body = f'''
<section class="hero"><div class="wrap">
  <h1>{e(h["h1"])}</h1>
  <p class="lead">{e(h["lead"])}</p>
  <div class="actions"><a class="btn accent" href="/join/">Join as an individual</a><a class="btn secondary" style="color:#fff;border-color:rgba(255,255,255,.6)" href="/pledge/">Sign the Pledge</a><a class="plain" href="/mission/">Read the mission</a></div>
  {curve_svg()}
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><h2>{e(h["horizons_h"])}</h2></div>
  <ul class="horizons">{horizons}</ul>
</div></section>

<section class="section tint"><div class="wrap">
  <div class="section-head"><h2>{e(h["who_h"])}</h2><p class="lead">{e(h["who_p"])}</p></div>
  <ul class="stake-grid">{stakes}</ul>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><h2>{e(h["how_h"])}</h2></div>
  <dl class="defs verbs">{how}</dl>
  <p class="mt-2"><a href="/programmes/">The five programmes</a></p>
</div></section>

<section class="section tint"><div class="wrap">
  <div class="section-head"><h2>Six pathways</h2><p class="lead">One direction, several roads. Each has a working group, a body of knowledge and its own measures of progress.</p></div>
  <ul class="index-list">{paths}</ul>
</div></section>

<section class="section"><div class="wrap grid c2">
  <div><h2>{e(h["founding_h"])}</h2><p>{e(h["founding_p"])}</p></div>
  <div><h2>The Pledge</h2><p>Organisations join by signing the AATTRL Pledge: a public baseline within a year, a dated target with interim milestones, annual progress, commitments to nature and people, and one shared case a year. Reviewed independently. Free to sign; something to keep.</p><p><a href="/pledge/">Read the Pledge</a></p></div>
</div></section>

{cta_band()}
'''
    page("/", h["title"], h["desc"], body)

def build_mission():
    m = C.MISSION
    body = page_head(m["h1"], m["lead"], crumbs(("Home", "/"), ("Mission", None))) + f'''
<section class="section" style="padding-top:0"><div class="wrap prose">{md(m["body"])}</div></section>
{cta_band()}'''
    page("/mission/", m["title"], m["desc"], body)

def build_stakeholders():
    hub = C.STAKEHOLDERS_HUB
    lis = "".join('<li><h3><a href="/stakeholders/%s/">%s</a></h3><p>%s</p></li>' % (s["slug"], e(s["name"]), e(s["short"])) for s in C.STAKEHOLDERS)
    body = page_head(hub["h1"], hub["lead"], crumbs(("Home", "/"), ("Stakeholders", None))) + f'''
<section class="section" style="padding-top:0"><div class="wrap"><ul class="index-list">{lis}</ul></div></section>
{cta_band()}'''
    page("/stakeholders/", hub["title"], hub["desc"], body)
    for s in C.STAKEHOLDERS:
        needs = "".join("<li>%s</li>" % e(n) for n in s["needs"])
        others = "".join('<li><a href="/stakeholders/%s/">%s</a></li>' % (o["slug"], e(o["name"])) for o in C.STAKEHOLDERS if o is not s)
        aside = f'<aside class="aside"><h2>What this stakeholder needs from the others</h2><ul>{needs}</ul><h2 class="mt-2">Other stakeholders</h2><ul style="list-style:none;padding:0">{others}</ul></aside>'
        body = page_head(s["h1"], s["lead"], crumbs(("Home", "/"), ("Stakeholders", "/stakeholders/"), (s["name"], None))) + f'''
<section class="section" style="padding-top:0"><div class="wrap two-col"><div class="prose">{md(s["body"])}</div>{aside}</div></section>
{cta_band()}'''
        page(f'/stakeholders/{s["slug"]}/', s["title"], s["desc"], body)

def build_pathways():
    hub = C.PATHWAYS_HUB
    lis = "".join('<li><div><h3><a href="/pathways/%s/">%s</a></h3><p class="meta">%s</p></div><p>%s</p></li>' % (p["slug"], e(p["name"]), e(p["horizon"]), e(p["short"])) for p in C.PATHWAYS)
    body = page_head(hub["h1"], hub["lead"], crumbs(("Home", "/"), ("Pathways", None))) + f'''
<section class="section" style="padding-top:0"><div class="wrap"><ul class="index-list">{lis}</ul></div></section>
{cta_band()}'''
    page("/pathways/", hub["title"], hub["desc"], body)
    for p in C.PATHWAYS:
        others = "".join('<li><a href="/pathways/%s/">%s</a></li>' % (o["slug"], e(o["name"])) for o in C.PATHWAYS if o is not p)
        aside = f'<aside class="aside"><h2>Join this working group</h2><p><a href="/join/">Join the platform</a> and choose this pathway. Organisations join through <a href="/pledge/">the Pledge</a>.</p><h2 class="mt-2">Other pathways</h2><ul style="list-style:none;padding:0">{others}</ul></aside>'
        body = page_head(p["h1"], p["lead"], crumbs(("Home", "/"), ("Pathways", "/pathways/"), (p["name"], None)), tag="Horizon: " + p["horizon"]) + f'''
<section class="section" style="padding-top:0"><div class="wrap two-col"><div class="prose">{md(p["body"])}</div>{aside}</div></section>
{cta_band()}'''
        page(f'/pathways/{p["slug"]}/', p["title"], p["desc"], body)

def build_programmes():
    g = C.PROGRAMMES
    items = "".join(f'<li id="{slug}"><h3>{e(name)}</h3><div>{md(text)}</div></li>' for slug, name, text in g["items"])
    body = page_head(g["h1"], g["lead"], crumbs(("Home", "/"), ("Programmes", None))) + f'''
<section class="section" style="padding-top:0"><div class="wrap"><ol class="numbered">{items}</ol><p class="mt-3 prose">{e(g["note"])}</p></div></section>
{cta_band()}'''
    page("/programmes/", g["title"], g["desc"], body)

def build_pledge():
    p = C.PLEDGE; f = C.PLEDGE_FORM
    commitments = "".join("<li><h3>%s</h3><p>%s</p></li>" % (e(a), e(b)) for a, b in p["commitments"])
    by_type = "".join("<div><dt>%s</dt><dd>%s</dd></div>" % (e(a), e(b)) for a, b in p["by_type"])
    fields = [
        dict(name="organisation", label="Organisation", required=True, ac="organization", half=True),
        dict(name="stakeholder", label="Stakeholder group", type="select", required=True, half=True, options=STAKEHOLDER_OPTIONS),
        dict(name="name", label="Your name", required=True, ac="name", half=True),
        dict(name="role", label="Your role", required=True, ac="organization-title", half=True),
        dict(name="email", label="Work email", type="email", required=True, ac="email", half=True, error="Please enter a valid email address."),
        dict(name="country", label="Country", required=True, ac="country-name", half=True),
        dict(name="scope", label="Scope you intend to sign for", required=True, hint="A site, a business unit or the whole organisation. Name it."),
        dict(name="pathways", label="Pathways most relevant to you", type="checks", options=PATHWAY_OPTIONS),
        dict(name="status", label="Where you are today", type="select", options=["No baseline yet", "Baseline measured, no target", "Target set, no public plan", "Plan published, want review"]),
        dict(name="message", label="Anything else", type="textarea", hint="Optional. Sites, questions, or what you would want from the platform."),
    ]
    consent = 'I am authorised to begin this on behalf of the organisation, and I understand that signatories are listed publicly on the register as described in the <a href="/privacy/">privacy note</a>.'
    body = page_head(p["h1"], p["lead"], crumbs(("Home", "/"), ("The Pledge", None))) + f'''
<section class="section" style="padding-top:0"><div class="wrap">
  <div class="section-head"><h2>{e(p["commitments_h"])}</h2></div>
  <ol class="numbered">{commitments}</ol>
</div></section>
<section class="section tint"><div class="wrap">
  <div class="section-head"><h2>{e(p["by_type_h"])}</h2></div>
  <dl class="defs">{by_type}</dl>
</div></section>
<section class="section"><div class="wrap grid c2">
  <div><h2>{e(p["review_h"])}</h2><p>{e(p["review_p"])}</p></div>
  <div><h2>{e(p["register_h"])}</h2><p>{e(p["register_p"])}</p></div>
</div></section>
<section class="section tint" id="sign"><div class="wrap two-col">
  <div><h2>{e(f["h"])}</h2><p>{e(f["lead"])}</p>{form("pledge", fields, "Begin the Pledge", "Pledge signatory", consent)}</div>
  <aside class="aside"><h2>What happens next</h2><ul><li>The founder replies within a week to confirm the scope.</li><li>You agree a date for the baseline, within twelve months.</li><li>You are placed in the working groups for your pathways.</li><li>Your organisation is listed as a founding signatory when the register opens.</li></ul><p class="meta">No fee in the founding phase. Questions first? <a href="/contact/">Contact the platform</a>.</p></aside>
</div></section>'''
    page("/pledge/", p["title"], p["desc"], body)

def build_events():
    ev = C.EVENTS
    formats = "".join("<div><dt>%s</dt><dd>%s</dd></div>" % (e(a), e(b)) for a, b in ev["formats"])
    body = page_head(ev["h1"], ev["lead"], crumbs(("Home", "/"), ("Events", None))) + f'''
<section class="section" style="padding-top:0"><div class="wrap"><dl class="defs">{formats}</dl><p class="mt-3 prose">{e(ev["note"])}</p></div></section>
{cta_band("Be told when the dates are published", "Members receive the convening programme first.")}'''
    page("/events/", ev["title"], ev["desc"], body)

def nice_date(d):
    return datetime.date.fromisoformat(d).strftime("%-d %B %Y")

def build_knowledge():
    hub = C.KNOWLEDGE_HUB
    items = sorted(C.KNOWLEDGE, key=lambda i: i["date"], reverse=True)
    lis = "".join('<li><div><h3><a href="/knowledge/%s/">%s</a></h3><p class="meta">%s · %d min</p></div><p>%s</p></li>' % (i["slug"], e(i["name"]), nice_date(i["date"]), i["minutes"], e(i["desc"])) for i in items)
    body = page_head(hub["h1"], hub["lead"], crumbs(("Home", "/"), ("Knowledge", None))) + f'''
<section class="section" style="padding-top:0"><div class="wrap"><ul class="index-list">{lis}</ul></div></section>
{cta_band()}'''
    page("/knowledge/", hub["title"], hub["desc"], body)
    for i in items:
        art_ld = {"@context": "https://schema.org", "@type": "Article", "headline": i["name"], "datePublished": i["date"], "author": {"@type": "Person", "name": "Basheer Thasthakir"}, "publisher": {"@type": "Organization", "name": S["legal_name"]}, "description": i["desc"], "mainEntityOfPage": f'{S["url"]}/knowledge/{i["slug"]}/'}
        others = "".join('<li><a href="/knowledge/%s/">%s</a></li>' % (o["slug"], e(o["name"])) for o in items if o is not i)
        body = f'''<section class="page-head"><div class="wrap article">{crumbs(("Home", "/"), ("Knowledge", "/knowledge/"), (i["name"], None))}<h1>{e(i["name"])}</h1><p class="meta">AATTRL · {nice_date(i["date"])} · {i["minutes"]} min read</p><div class="lead">{e(i["desc"])}</div></div></section>
<section class="section" style="padding-top:0"><div class="wrap"><div class="article prose">{md(i["body"])}</div>
<div class="related article"><h2>More knowledge</h2><ul>{others}</ul></div></div></section>
{cta_band()}'''
        page(f'/knowledge/{i["slug"]}/', i["name"] + " | AATTRL", i["desc"], body, lastmod=i["date"], ld_extra=art_ld)

def build_about():
    a = C.ABOUT; p = a["principal"]
    facts = "".join("<div><dt>%s</dt><dd>%s</dd></div>" % (e(k), e(v)) for k, v in p["facts"])
    person_ld = {"@context": "https://schema.org", "@type": "Person", "name": p["name"], "jobTitle": p["role"], "worksFor": {"@type": "Organization", "name": S["legal_name"]}, "email": S["email"]}
    body = page_head(a["h1"], a["lead"], crumbs(("Home", "/"), ("About", None))) + f'''
<section class="section" style="padding-top:0"><div class="wrap prose">{md(a["body"])}</div></section>
<section class="section tint" id="founder"><div class="wrap">
  <div class="section-head"><h2>{e(a["principal_h"])}</h2></div>
  <div class="principal">
    <div><h3 class="name">{e(p["name"])}</h3><p class="role">{e(p["role"])}</p><p>{e(p["bio"])}</p></div>
    <dl class="facts">{facts}</dl>
  </div>
</div></section>
{cta_band()}'''
    page("/about/", a["title"], a["desc"], body, ld_extra=person_ld)

def build_join():
    j = C.JOIN
    fields = [
        dict(name="name", label="Name", required=True, ac="name", half=True),
        dict(name="email", label="Email", type="email", required=True, ac="email", half=True, error="Please enter a valid email address."),
        dict(name="organisation", label="Organisation", ac="organization", half=True, hint="Optional"),
        dict(name="role", label="Role", ac="organization-title", half=True),
        dict(name="country", label="Country", required=True, ac="country-name", half=True),
        dict(name="stakeholder", label="Which stakeholder are you?", type="select", required=True, half=True, options=STAKEHOLDER_OPTIONS),
        dict(name="pathways", label="Pathways you want to work on", type="checks", options=PATHWAY_OPTIONS),
        dict(name="contribution", label="What you bring", type="textarea", hint="A few lines: your experience, what you could contribute to a working group or a review, or what you want from the platform."),
    ]
    aside_lis = "".join("<li>%s</li>" % e(x) for x in j["aside"])
    body = page_head(j["h1"], j["lead"], crumbs(("Home", "/"), ("Join", None))) + f'''
<section class="section" style="padding-top:0"><div class="wrap two-col">
  <div>{form("join", fields, "Join the platform", "New member")}</div>
  <aside class="aside"><h2>{e(j["aside_h"])}</h2><ul>{aside_lis}</ul><h2 class="mt-2">{e(j["org_h"])}</h2>{md(j["org_p"])}</aside>
</div></section>'''
    page("/join/", j["title"], j["desc"], body)

def build_contact():
    c = C.CONTACT
    fields = [
        dict(name="name", label="Name", required=True, ac="name", half=True),
        dict(name="email", label="Email", type="email", required=True, ac="email", half=True, error="Please enter a valid email address."),
        dict(name="organisation", label="Organisation", ac="organization"),
        dict(name="message", label="Message", type="textarea", required=True),
    ]
    body = page_head(c["h1"], c["lead"], crumbs(("Home", "/"), ("Contact", None))) + f'''
<section class="section" style="padding-top:0"><div class="wrap two-col">
  <div>{form("contact", fields, "Send message", "Website enquiry")}</div>
  <aside class="aside"><h2>Directly</h2><p><a href="mailto:{S["email"]}">{S["email"]}</a><br><a href="https://wa.me/{S["wa_number"]}" rel="noopener">WhatsApp {e(S["phone_display"])}</a></p>
  <h2 class="mt-2">Where</h2><p>Founded in the United Arab Emirates and India. The platform is global; the first chapters are India and the GCC.</p></aside>
</div></section>'''
    page("/contact/", c["title"], c["desc"], body)

def build_misc():
    t = C.THANK_YOU
    page("/thank-you/", t["title"], t["desc"], page_head(t["h1"], t["lead"]) + '<section class="section" style="padding-top:0"><div class="wrap prose"><p><a href="/mission/">The mission</a> · <a href="/pathways/">The six pathways</a> · <a href="/knowledge/">Knowledge</a></p></div></section>', noindex=True)
    p = C.PRIVACY
    page("/privacy/", p["title"], p["desc"], page_head(p["h1"], p["lead"], crumbs(("Home", "/"), ("Privacy", None))) + f'<section class="section" style="padding-top:0"><div class="wrap prose">{md(p["body"])}</div></section>')
    n = C.NOT_FOUND
    links = "".join('<li><a href="%s">%s</a></li>' % (path, e(label)) for label, path in [("Home", "/"), ("Mission", "/mission/"), ("Stakeholders", "/stakeholders/"), ("Pathways", "/pathways/"), ("Programmes", "/programmes/"), ("The Pledge", "/pledge/"), ("Join", "/join/"), ("Contact", "/contact/")])
    page("/404.html", n["title"], n["lead"], page_head(n["h1"], n["lead"]) + f'<section class="section" style="padding-top:0"><div class="wrap prose"><ul>{links}</ul></div></section>', noindex=True)

def build_meta():
    urls = "".join(f'  <url><loc>{S["url"]}{p}</loc><lastmod>{lm}</lastmod></url>\n' for p, lm in GENERATED)
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /thank-you/\n\nSitemap: {S['url']}/sitemap.xml\n")
    (ROOT / "site.webmanifest").write_text('{"name":"AATTRL","short_name":"AATTRL","icons":[{"src":"/assets/images/apple-touch-icon.png","sizes":"180x180","type":"image/png"}],"theme_color":"#15302A","background_color":"#F7F7F3","display":"browser","start_url":"/"}\n')
    redirects = "".join(f'\n[[redirects]]\n  from = "{a}"\n  to = "{b}"\n  status = 301\n' for a, b in C.REDIRECTS)
    (ROOT / "netlify.toml").write_text(f'''# Netlify configuration for www.aattrl.com (AATTRL, the platform for industry within nature's limits).
# Static site: no build step. Publish the repository root. Pages are generated
# from _build/content.py by `python3 _build/build.py` and committed.

[build]
  publish = "."
  command = ""

# --- Future: Zoho-style product path -----------------------------------------
# To serve Enaivu at aattrl.com/one instead of enaivu.com, uncomment the
# proxy below AFTER the Enaivu app has been rebuilt with basePath "/one".
#
# [[redirects]]
#   from = "/one/*"
#   to = "https://enaivu.com/one/:splat"
#   status = 200
#   force = true

# --- Redirects from the two previous sites --------------------------------------{redirects}
[[headers]]
  for = "/*"
  [headers.values]
    X-Content-Type-Options = "nosniff"
    X-Frame-Options = "DENY"
    Referrer-Policy = "strict-origin-when-cross-origin"
    Permissions-Policy = "camera=(), microphone=(), geolocation=()"

[[headers]]
  for = "/assets/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"
''')

def main():
    build_home(); build_mission(); build_stakeholders(); build_pathways(); build_programmes()
    build_pledge(); build_events(); build_knowledge(); build_about(); build_join(); build_contact(); build_misc()
    build_meta()
    print("Generated %d indexable pages + thank-you, 404, sitemap, robots, manifest, netlify.toml" % len(GENERATED))

if __name__ == "__main__":
    main()
