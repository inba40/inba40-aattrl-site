#!/usr/bin/env python3
"""Generate www.aattrl.com from _build/content.py into the repository root.

    python3 _build/build.py

Requires: python3, `markdown` (pip install markdown). Output is plain HTML under
URL paths (challenges/growth-has-stalled/index.html -> /challenges/growth-has-stalled/).
"""
import datetime
import html as H
import os
import pathlib
import re
import shutil
import sys

import markdown

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import content as C  # noqa: E402

TODAY = datetime.date.today().isoformat()
S = C.SITE
GENERATED = []  # (path, lastmod) for the sitemap

def md(text):
    return markdown.markdown(text.strip(), extensions=["smarty"], output_format="html5")

def e(s):
    return H.escape(s, quote=True)

def ld(obj):
    import json
    return '<script type="application/ld+json">%s</script>' % json.dumps(obj, ensure_ascii=False)

ORG_LD = {
    "@context": "https://schema.org", "@type": "ProfessionalService",
    "name": S["legal_name"], "alternateName": "AATTRL", "url": S["url"] + "/",
    "description": S["descriptor"], "email": S["email"], "telephone": "+" + S["wa_number"],
    "founder": {"@type": "Person", "name": "Basheer Thasthakir"},
    "areaServed": ["India", "United Arab Emirates", "Saudi Arabia", "Qatar", "Oman", "Kuwait", "Bahrain", "Europe", "Asia", "Africa"],
    "knowsAbout": ["Executive problem-solving", "Turnaround", "Programme recovery", "Decision review", "Leadership team effectiveness"],
}

# --------------------------------------------------------------------------
def header(current):
    items = []
    for label, path in C.NAV:
        cur = ' aria-current="page"' if current.startswith(path) else ""
        items.append('<li><a href="%s"%s>%s</a></li>' % (path, cur, e(label)))
    nav = "".join(items)
    mob = nav + '<li><a href="%s">%s</a></li><li><a href="/contact/">Contact</a></li>' % (C.CTA[1], e(C.CTA[0]))
    return f'''<a class="skip" href="#main">Skip to main content</a>
<header class="site-header">
  <div class="header-row">
    <a class="brand" href="/" aria-label="AATTRL home">AATTRL <small>{e(S["tagline"])}</small></a>
    <nav class="nav" aria-label="Main"><ul>{nav}</ul></nav>
    <a class="btn header-cta" href="{C.CTA[1]}">{e(C.CTA[0])}</a>
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
        <a class="brand" href="/">AATTRL <small>{e(S["tagline"])}</small></a>
        <p>{e(S["descriptor"])}</p>
        <p><a href="mailto:{S["email"]}">{S["email"]}</a><br><a href="https://wa.me/{S["wa_number"]}" rel="noopener">WhatsApp {e(S["phone_display"])}</a></p>
      </div>
      {"".join(cols)}
    </div>
    <div class="bottom"><span>&copy; {TODAY[:4]} {e(S["legal_name"])}</span><span>{e(S["regions"])}</span></div>
  </div>
</footer>
<script src="/assets/js/main.js" defer></script>'''

def page(path, title, desc, body, extra_head="", noindex=False, lastmod=TODAY, ld_extra=None):
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
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/assets/images/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/images/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/assets/fonts/newsreader-latin-500-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/newsreader-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/style.css">
{lds}
{extra_head}
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

def page_head(h1, lead, crumb=None, lead_html=False):
    lead_html_s = lead if lead_html else md(lead)
    return f'<section class="page-head"><div class="wrap">{crumb or ""}<h1>{e(h1)}</h1><div class="lead">{lead_html_s}</div></div></section>'

def cta_band(h=None, p=None):
    h = h or C.HOME["cta_h"]; p = p or C.HOME["cta_p"]
    return f'''<section class="section dark cta-band"><div class="wrap">
  <div><h2>{e(h)}</h2><p class="lead">{e(p)}</p></div>
  <div class="actions"><a class="btn light" href="{C.CTA[1]}">{e(C.CTA[0])}</a>
    <span class="direct"><a href="mailto:{S["email"]}">{S["email"]}</a> &nbsp;·&nbsp; <a href="https://wa.me/{S["wa_number"]}" rel="noopener">WhatsApp</a></span></div>
</div></section>'''

def form(name, fields, button, subject):
    """Netlify form. `fields` is a list of dicts: name, label, type, required, hint, options, half."""
    rows = []
    i = 0
    while i < len(fields):
        f = fields[i]
        if f.get("half") and i + 1 < len(fields) and fields[i + 1].get("half"):
            rows.append('<div class="row">%s%s</div>' % (field_html(f), field_html(fields[i + 1]))); i += 2
        else:
            rows.append(field_html(f)); i += 1
    return f'''<form class="form" name="{name}" method="POST" action="/thank-you/" data-netlify="true" netlify-honeypot="company-website" novalidate>
  <input type="hidden" name="form-name" value="{name}">
  <input type="hidden" name="subject" value="{e(subject)}">
  <p class="hp" aria-hidden="true"><label>Leave this field empty <input type="text" name="company-website" tabindex="-1" autocomplete="off"></label></p>
  {"".join(rows)}
  <div class="field consent"><input type="checkbox" id="{name}-consent" name="consent" value="yes" required><label for="{name}-consent">I understand that this message will be read by the AATTRL principal and handled in confidence, as described in the <a href="/privacy/">privacy note</a>.</label></div>
  <div class="actions"><button class="btn" type="submit">{e(button)}</button></div>
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
    else:
        ac = ' autocomplete="%s"' % f["ac"] if f.get("ac") else ""
        ctl = f'<input id="{n}" name="{n}" type="{t}"{ac}{req}>'
    return f'<div class="field"><label for="{n}">{e(f["label"])}{hint}</label>{ctl}{err}</div>'

# --------------------------------------------------------------------------
def build_home():
    h = C.HOME
    voices = "".join("<li>%s</li>" % e(v) for v in h["voices"])
    what = "".join("<li><h3>%s</h3><p>%s</p></li>" % (e(a), e(b)) for a, b in h["what"])
    diff = "".join("<div><dt>%s</dt><dd>%s</dd></div>" % (e(a), e(b)) for a, b in h["different"])
    ch = "".join('<li><h3><a href="/challenges/%s/">%s</a></h3><p>%s</p></li>' % (c["slug"], e(c["name"]), e(c["short"])) for c in C.CHALLENGES[:6])
    body = f'''
<section class="hero"><div class="wrap">
  <h1>{e(h["h1"])}</h1>
  <p class="lead">{e(h["lead"])}</p>
  <div class="actions"><a class="btn" href="{C.CTA[1]}">{e(C.CTA[0])}</a><a class="plain" href="/how-it-works/">How an engagement runs</a></div>
</div></section>

<section class="section tint"><div class="wrap">
  <ul class="voices">{voices}</ul>
  <p class="voices-note">If one of these sounds like yours, it is the kind of problem AATTRL takes on. <a href="/challenges/">See the challenges we take on.</a></p>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><h2>{e(h["what_h"])}</h2></div>
  <ol class="steps-3">{what}</ol>
</div></section>

<section class="section tint"><div class="wrap">
  <div class="section-head"><h2>Challenges we take on</h2><p class="lead">Named by the problem as it reaches the chief executive, not by the discipline that might address it.</p></div>
  <ul class="index-list">{ch}</ul>
  <p class="mt-2"><a href="/challenges/">All challenges, including board and investor pressure</a></p>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><h2>{e(h["different_h"])}</h2></div>
  <dl class="defs">{diff}</dl>
</div></section>

<section class="section tint"><div class="wrap">
  <div class="grid c2">
    <div><h2>{e(h["serve_h"])}</h2><p>{e(h["serve"])}</p><p><a href="/who-we-serve/">Who we serve</a></p></div>
    <div><h2>Who does the work</h2><p>Every brief is led personally by the founder, Basheer Thasthakir, and every team is drawn from a network of senior people who have run businesses, functions, programmes and operations. There is no bench. <a href="/about/">About the firm</a> and <a href="/network/">the senior network</a>.</p></div>
  </div>
</div></section>

{cta_band()}
'''
    page("/", h["title"], h["desc"], body)

def build_how():
    h = C.HOW
    steps = "".join("<li><h3>%s</h3><p>%s</p></li>" % (e(a), e(b)) for a, b in h["steps"])
    terms = "".join("<div><dt>%s</dt><dd>%s</dd></div>" % (e(a), e(b)) for a, b in h["terms"])
    body = page_head(h["h1"], h["lead"], crumbs(("Home", "/"), ("How it works", None))) + f'''
<section class="section" style="padding-top:0"><div class="wrap"><ol class="process">{steps}</ol></div></section>
<section class="section tint"><div class="wrap"><div class="section-head"><h2>{e(h["terms_h"])}</h2></div><dl class="defs">{terms}</dl></div></section>
<section class="section"><div class="wrap prose"><h2>{e(h["length_h"])}</h2><p>{e(h["length"])}</p><p><a href="/engagements/">The four engagement formats</a></p></div></section>
{cta_band()}'''
    page("/how-it-works/", h["title"], h["desc"], body)

def build_challenges():
    hub = C.CHALLENGES_HUB
    lis = "".join('<li><h3><a href="/challenges/%s/">%s</a></h3><p>%s</p></li>' % (c["slug"], e(c["name"]), e(c["short"])) for c in C.CHALLENGES)
    body = page_head(hub["h1"], hub["lead"], crumbs(("Home", "/"), ("Challenges", None))) + f'''
<section class="section" style="padding-top:0"><div class="wrap"><ul class="index-list">{lis}</ul>
<p class="mt-3">Not on the list? Most problems that reach a chief executive are. <a href="/bring-a-challenge/">Describe yours</a> and the principal will tell you honestly whether AATTRL can take it on.</p></div></section>
{cta_band()}'''
    page("/challenges/", hub["title"], hub["desc"], body)
    by = {c["slug"]: c for c in C.CHALLENGES}
    for c in C.CHALLENGES:
        rel = "".join('<li><a href="/challenges/%s/">%s</a></li>' % (s, e(by[s]["name"])) for s in c["related"] if s in by)
        aside = f'''<aside class="aside"><h2>Related challenges</h2><ul style="list-style:none;padding:0">{rel}</ul>
<h2 class="mt-2">Engagement formats</h2><ul style="list-style:none;padding:0"><li><a href="/engagements/executive-problem-solving/">Executive problem-solving</a></li><li><a href="/engagements/independent-decision-review/">Independent decision review</a></li><li><a href="/engagements/execution-and-recovery/">Execution and recovery</a></li></ul>
<p class="meta">Situations described on this page are typical patterns, not accounts of named clients. Engagements are confidential.</p></aside>'''
        body = page_head(c["h1"], c["lead"], crumbs(("Home", "/"), ("Challenges", "/challenges/"), (c["name"], None))) + f'''
<section class="section" style="padding-top:0"><div class="wrap two-col"><div class="prose">{md(c["body"])}</div>{aside}</div></section>
{cta_band("Is this the problem on your desk?", "Describe it in a few lines. The principal replies personally, in confidence, usually within two working days.")}'''
        page(f'/challenges/{c["slug"]}/', c["title"], c["desc"], body)

def build_engagements():
    hub = C.ENGAGEMENTS_HUB
    lis = "".join('<li><h3><a href="/engagements/%s/">%s</a></h3><p>%s</p></li>' % (g["slug"], e(g["name"]), e(g["short"])) for g in C.ENGAGEMENTS)
    body = page_head(hub["h1"], hub["lead"], crumbs(("Home", "/"), ("Engagements", None))) + f'''
<section class="section" style="padding-top:0"><div class="wrap"><ul class="index-list">{lis}</ul>
<p class="mt-3">All four run on the same terms: fixed scope and fee per stage, senior people throughout, confidentiality by default and independence from any product or party. <a href="/how-it-works/">How an engagement runs.</a></p></div></section>
{cta_band()}'''
    page("/engagements/", hub["title"], hub["desc"], body)
    for g in C.ENGAGEMENTS:
        others = "".join('<li><a href="/engagements/%s/">%s</a></li>' % (o["slug"], e(o["name"])) for o in C.ENGAGEMENTS if o is not g)
        aside = f'<aside class="aside"><h2>Other formats</h2><ul style="list-style:none;padding:0">{others}</ul><h2 class="mt-2">Start</h2><p><a href="/bring-a-challenge/">Bring a challenge</a> and the principal will propose the format that fits.</p></aside>'
        body = page_head(g["h1"], g["lead"], crumbs(("Home", "/"), ("Engagements", "/engagements/"), (g["name"], None))) + f'''
<section class="section" style="padding-top:0"><div class="wrap two-col"><div class="prose">{md(g["body"])}</div>{aside}</div></section>
{cta_band()}'''
        page(f'/engagements/{g["slug"]}/', g["title"], g["desc"], body)

def build_serve():
    s = C.SERVE
    groups = "".join("<div><dt>%s</dt><dd>%s</dd></div>" % (e(a), e(b)) for a, b in s["groups"])
    body = page_head(s["h1"], s["lead"], crumbs(("Home", "/"), ("Who we serve", None))) + f'''
<section class="section" style="padding-top:0"><div class="wrap"><dl class="defs">{groups}</dl></div></section>
<section class="section tint"><div class="wrap grid c2">
  <div><h2>{e(s["sectors_h"])}</h2><p>{e(s["sectors_p"])}</p></div>
  <div><h2>{e(s["where_h"])}</h2><p>{e(s["where_p"])}</p></div>
</div></section>
{cta_band()}'''
    page("/who-we-serve/", s["title"], s["desc"], body)

def build_about():
    a = C.ABOUT; p = a["principal"]
    facts = "".join("<div><dt>%s</dt><dd>%s</dd></div>" % (e(k), e(v)) for k, v in p["facts"])
    person_ld = {"@context": "https://schema.org", "@type": "Person", "name": p["name"], "jobTitle": p["role"], "worksFor": {"@type": "Organization", "name": S["legal_name"]}, "email": S["email"]}
    body = page_head(a["h1"], a["lead"], crumbs(("Home", "/"), ("About", None))) + f'''
<section class="section" style="padding-top:0"><div class="wrap prose">{md(a["body"])}</div></section>
<section class="section tint" id="principal"><div class="wrap">
  <div class="section-head"><h2>{e(a["principal_h"])}</h2></div>
  <div class="principal">
    <div><h3 class="name">{e(p["name"])}</h3><p class="role">{e(p["role"])}</p><p>{e(p["bio"])}</p></div>
    <dl class="facts">{facts}</dl>
  </div>
</div></section>
<section class="section"><div class="wrap grid c2">
  <div><h2>{e(a["network_h"])}</h2>{md(a["network_p"])}</div>
  <div><h2>{e(a["enaivu_h"])}</h2>{md(a["enaivu_p"])}</div>
</div></section>
{cta_band()}'''
    page("/about/", a["title"], a["desc"], body, ld_extra=person_ld)

def build_network():
    n = C.NETWORK
    fields = [
        dict(name="name", label="Name", required=True, ac="name", half=True),
        dict(name="email", label="Email", type="email", required=True, ac="email", half=True, error="Please enter a valid email address."),
        dict(name="location", label="Where you are based", half=True),
        dict(name="linkedin", label="LinkedIn or CV link", hint="Optional", half=True),
        dict(name="roles", label="The most senior roles you have held", type="textarea", required=True, hint="Organisation, role, period and the scale of the accountability."),
        dict(name="problems", label="The executive problems you have carried yourself", type="textarea", hint="Turnarounds, programme recoveries, major decisions, leadership-team resets, crises."),
        dict(name="availability", label="Availability", type="select", options=["A few days a month", "Up to half my time", "Full time for a defined period"]),
    ]
    body = page_head(n["h1"], n["lead"], crumbs(("Home", "/"), ("The senior network", None))) + f'''
<section class="section" style="padding-top:0"><div class="wrap prose">{md(n["body"])}</div></section>
<section class="section tint" id="join"><div class="wrap two-col">
  <div><h2>{e(n["join_h"])}</h2><p>{e(n["join_p"])}</p>{form("join-network", fields, "Send application", "Senior network application")}</div>
  <aside class="aside"><h2>What to expect</h2><p>Applications are read by the principal. If there is a fit, you will be invited to a conversation. Nothing is shared outside AATTRL.</p><p>You can also write directly to <a href="mailto:{S["email"]}">{S["email"]}</a>.</p></aside>
</div></section>'''
    page("/network/", n["title"], n["desc"], body)

def build_insights():
    hub = C.INSIGHTS_HUB
    items = sorted(C.INSIGHTS, key=lambda i: i["date"], reverse=True)
    lis = "".join('<li><div><h3><a href="/insights/%s/">%s</a></h3><p class="meta">%s · %d min</p></div><p>%s</p></li>' % (i["slug"], e(i["name"]), nice_date(i["date"]), i["minutes"], e(i["desc"])) for i in items)
    body = page_head(hub["h1"], hub["lead"], crumbs(("Home", "/"), ("Insights", None))) + f'''
<section class="section" style="padding-top:0"><div class="wrap"><ul class="index-list">{lis}</ul></div></section>
{cta_band()}'''
    page("/insights/", hub["title"], hub["desc"], body)
    for i in items:
        art_ld = {"@context": "https://schema.org", "@type": "Article", "headline": i["name"], "datePublished": i["date"], "author": {"@type": "Person", "name": "Basheer Thasthakir"}, "publisher": {"@type": "Organization", "name": S["legal_name"]}, "description": i["desc"], "mainEntityOfPage": f'{S["url"]}/insights/{i["slug"]}/'}
        others = "".join('<li><a href="/insights/%s/">%s</a></li>' % (o["slug"], e(o["name"])) for o in items if o is not i)
        body = f'''<section class="page-head"><div class="wrap article">{crumbs(("Home", "/"), ("Insights", "/insights/"), (i["name"], None))}<h1>{e(i["name"])}</h1><p class="meta">Basheer Thasthakir · {nice_date(i["date"])} · {i["minutes"]} min read</p><div class="lead">{e(i["desc"])}</div></div></section>
<section class="section" style="padding-top:0"><div class="wrap"><div class="article prose">{md(i["body"])}</div>
<div class="related article"><h2>More for chief executives</h2><ul>{others}</ul></div></div></section>
{cta_band()}'''
        page(f'/insights/{i["slug"]}/', i["name"] + " | AATTRL", i["desc"], body, lastmod=i["date"], ld_extra=art_ld)

def nice_date(d):
    return datetime.date.fromisoformat(d).strftime("%-d %B %Y")

def build_bring():
    b = C.BRING
    fields = [
        dict(name="name", label="Name", required=True, ac="name", half=True),
        dict(name="role", label="Role and organisation", required=True, ac="organization-title", half=True, hint="For example, Managing Director, a mid-sized manufacturer"),
        dict(name="email", label="Email", type="email", required=True, ac="email", half=True, error="Please enter a valid email address."),
        dict(name="phone", label="Phone or WhatsApp", ac="tel", half=True, hint="Optional"),
        dict(name="location", label="Where the business is", half=True),
        dict(name="urgency", label="How urgent", type="select", half=True, options=["Immediate: weeks matter", "Soon: this quarter", "Important, not urgent", "Exploring"]),
        dict(name="challenge", label="The situation, as you see it", type="textarea", required=True, hint="A few lines is enough. What is happening, what has been tried, and what a good outcome would look like."),
    ]
    aside_lis = "".join("<li>%s</li>" % e(x) for x in b["aside"])
    body = page_head(b["h1"], b["lead"], crumbs(("Home", "/"), ("Bring a challenge", None))) + f'''
<section class="section" style="padding-top:0"><div class="wrap two-col">
  <div>{form("bring-a-challenge", fields, "Send to the principal", "Challenge brought via website")}</div>
  <aside class="aside"><h2>{e(b["aside_h"])}</h2><ul>{aside_lis}</ul>
  <h2 class="mt-2">{e(b["direct_h"])}</h2><p><a href="mailto:{S["email"]}">{S["email"]}</a><br><a href="https://wa.me/{S["wa_number"]}" rel="noopener">WhatsApp {e(S["phone_display"])}</a></p>
  <p class="meta">Read by the principal only. A non-disclosure agreement is available before the first conversation.</p></aside>
</div></section>'''
    page("/bring-a-challenge/", b["title"], b["desc"], body)

def build_contact():
    c = C.CONTACT
    fields = [
        dict(name="name", label="Name", required=True, ac="name", half=True),
        dict(name="email", label="Email", type="email", required=True, ac="email", half=True, error="Please enter a valid email address."),
        dict(name="message", label="Message", type="textarea", required=True),
    ]
    body = page_head(c["h1"], c["lead"], crumbs(("Home", "/"), ("Contact", None))) + f'''
<section class="section" style="padding-top:0"><div class="wrap two-col">
  <div>{form("contact", fields, "Send message", "Website enquiry")}</div>
  <aside class="aside"><h2>Directly</h2><p><a href="mailto:{S["email"]}">{S["email"]}</a><br><a href="https://wa.me/{S["wa_number"]}" rel="noopener">WhatsApp {e(S["phone_display"])}</a></p>
  <h2 class="mt-2">Where</h2><p>United Arab Emirates and India. Engagements are delivered where the problem is; see <a href="/who-we-serve/">where we work</a>.</p>
  <h2 class="mt-2">Senior people</h2><p>To be considered for the senior network, <a href="/network/#join">apply here</a>.</p></aside>
</div></section>'''
    page("/contact/", c["title"], c["desc"], body)

def build_misc():
    t = C.THANK_YOU
    body = page_head(t["h1"], t["lead"]) + '<section class="section" style="padding-top:0"><div class="wrap prose"><p>In the meantime: <a href="/how-it-works/">how an engagement runs</a>, <a href="/challenges/">the challenges we take on</a>, or <a href="/insights/">short pieces for chief executives</a>.</p></div></section>'
    page("/thank-you/", t["title"], t["desc"], body, noindex=True)
    p = C.PRIVACY
    page("/privacy/", p["title"], p["desc"], page_head(p["h1"], p["lead"], crumbs(("Home", "/"), ("Privacy", None))) + f'<section class="section" style="padding-top:0"><div class="wrap prose">{md(p["body"])}</div></section>')
    n = C.NOT_FOUND
    links = "".join('<li><a href="%s">%s</a></li>' % (path, e(label)) for label, path in [("Home", "/"), ("How it works", "/how-it-works/"), ("Challenges we take on", "/challenges/"), ("Engagements", "/engagements/"), ("About", "/about/"), ("Bring a challenge", "/bring-a-challenge/"), ("Contact", "/contact/")])
    page("/404.html", n["title"], n["lead"], page_head(n["h1"], n["lead"]) + f'<section class="section" style="padding-top:0"><div class="wrap prose"><ul>{links}</ul></div></section>', noindex=True)

def build_meta():
    urls = "".join(f'  <url><loc>{S["url"]}{p}</loc><lastmod>{lm}</lastmod></url>\n' for p, lm in GENERATED)
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /thank-you/\n\nSitemap: {S['url']}/sitemap.xml\n")
    (ROOT / "site.webmanifest").write_text('{"name":"AATTRL","short_name":"AATTRL","icons":[{"src":"/assets/images/apple-touch-icon.png","sizes":"180x180","type":"image/png"}],"theme_color":"#0F2A24","background_color":"#FFFFFF","display":"browser","start_url":"/"}\n')
    redirects = "".join(f'\n[[redirects]]\n  from = "{a}"\n  to = "{b}"\n  status = 301\n' for a, b in C.REDIRECTS)
    (ROOT / "netlify.toml").write_text(f'''# Netlify configuration for www.aattrl.com (AATTRL, executive problem-solving).
# Static site: no build step. Publish the repository root. Pages are generated
# from _build/content.py by `python3 _build/build.py` and committed.

[build]
  publish = "."
  command = ""

# --- Future: Zoho-style product path -----------------------------------------
# To serve Enaivu at aattrl.com/one instead of enaivu.com, uncomment the
# proxy below AFTER the Enaivu app has been rebuilt with basePath "/one".
# Doing it in the other order shows a broken page. See the enaivu-site repo,
# docs/DEPLOYMENT.md, "Path migration".
#
# [[redirects]]
#   from = "/one/*"
#   to = "https://enaivu.com/one/:splat"
#   status = 200
#   force = true

# --- Redirects from the previous (engineering advisory) site -------------------{redirects}
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
    build_home(); build_how(); build_challenges(); build_engagements(); build_serve()
    build_about(); build_network(); build_insights(); build_bring(); build_contact(); build_misc()
    build_meta()
    print("Generated %d indexable pages + thank-you, 404, sitemap, robots, manifest, netlify.toml" % len(GENERATED))

if __name__ == "__main__":
    main()
