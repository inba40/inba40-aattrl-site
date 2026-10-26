# www.aattrl.com — AATTRL, executive problem-solving

Static website for AATTRL, deployed on Netlify from this repository.

- Positioning (since 2026-10-26): an executive problem-solving firm. A chief executive brings one hard problem; AATTRL puts senior people around it and works it through to resolution. The previous engineering-advisory site (HAZOP, asset management and so on) has been retired; its URLs redirect (see `netlify.toml`).
- Hosting: Netlify, publish directory `.`, no build step. Every push to `main` deploys.
- Sister business: Enaivu (software) at https://enaivu.com, repository `inba40/enaivu-site`. Linked from the footer and the About page only; never sold inside an engagement.

## Editing content

All copy lives in `_build/content.py`. Page templates live in `_build/build.py`. After editing either:

    pip install markdown      # once
    python3 _build/build.py   # regenerates every page, sitemap, robots, manifest and netlify.toml redirects

Commit the generated HTML together with the source. The build has no other dependencies.

Site map: home, how-it-works, challenges (hub + 9), engagements (hub + 4), who-we-serve, about, network (with application form), insights (hub + 5), bring-a-challenge, contact, thank-you (noindex), privacy, 404.

## Forms

The three forms (bring a challenge, contact, join the network) use Netlify Forms. Netlify detects them at deploy time. Set the notification email (info@aattrl.com) under Site settings → Forms → Form notifications in Netlify; until that is done, submissions are visible only in the Netlify dashboard. A honeypot field and a minimum fill time are in place; enable Netlify's spam filtering for the rest.

## Design

Newsreader (serif, headings and long text) and Inter (interface), both self-hosted under `assets/fonts` with their OFL licences. One stylesheet, `assets/css/style.css`; one small script, `assets/js/main.js` (mobile menu and form checks). The site works with JavaScript off.

## Honesty rules for content

No invented clients, numbers, testimonials or named network members. Challenge pages describe typical situations and say so. The principal's biography states only what has been verified.

## Changelog

- 2026-10-26 — Full repositioning as an executive problem-solving firm. New design, new site map, generator in `_build/`, Netlify Forms, 301 redirects from all previous URLs.
- 2026-10-19 — Imported published site; added Enaivu link; added `netlify.toml` headers.
