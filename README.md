# www.aattrl.com — AATTRL, the platform for industry within nature's limits

Static website for AATTRL, deployed on Netlify from this repository.

- Positioning (since 2026-10-31): a global platform bringing every stakeholder of industry (operators, providers, investors, governments, universities, professionals, workers and communities, innovators) together on three horizons: net zero, close to nature, zero impact. Movement site with join and pledge forms; no accounts. The two previous sites (engineering advisory to 2026-10-26; executive problem-solving to 2026-10-31) are retired and their URLs redirect (see `netlify.toml`).
- Hosting: Netlify, publish directory `.`, no build step. Every push to `main` deploys.
- Sister business: Enaivu (software) at https://enaivu.com, repository `inba40/enaivu-site`. Linked from the footer and the About page only; never sold inside an engagement.

## Editing content

All copy lives in `_build/content.py`. Page templates live in `_build/build.py`. After editing either:

    pip install markdown      # once
    python3 _build/build.py   # regenerates every page, sitemap, robots, manifest and netlify.toml redirects

Commit the generated HTML together with the source. The build has no other dependencies.

Site map: home, mission, stakeholders (hub + 8), pathways (hub + 6), programmes, pledge (with form), events, knowledge (hub + 5), about, join (form), contact (form), thank-you (noindex), privacy, 404.

## Forms

The three forms (join, pledge, contact) use Netlify Forms. Netlify detects them at deploy time. Set the notification email (info@aattrl.com) under Site settings → Forms → Form notifications in Netlify; until that is done, submissions are visible only in the Netlify dashboard. A honeypot field and a minimum fill time are in place; enable Netlify's spam filtering for the rest.

## Design

Archivo (headings and interface) and Source Serif 4 (reading text), both self-hosted under `assets/fonts` with their OFL licences. One stylesheet, `assets/css/style.css`; one small script, `assets/js/main.js` (mobile menu and form checks). The site works with JavaScript off.

## Honesty rules for content

No invented members, signatories, numbers or quotes. The platform is in its founding phase and every page says so. External figures carry a source link. The founder's biography states only what has been verified.

## Changelog

- 2026-10-31 — Repositioned as a global sustainability platform for all industry stakeholders. New design (Archivo, Source Serif 4, verdigris accent, the 'curve to zero' hero), new site map, pledge and join forms, 301 redirects from both previous sites.

- 2026-10-26 — Full repositioning as an executive problem-solving firm. New design, new site map, generator in `_build/`, Netlify Forms, 301 redirects from all previous URLs.
- 2026-10-19 — Imported published site; added Enaivu link; added `netlify.toml` headers.
