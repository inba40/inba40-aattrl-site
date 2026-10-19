# www.aattrl.com — AATTRL Global Expert Advisory

Static website for AATTRL Global Expert Advisory, deployed on Netlify from this repository.

- Source of record: this repository (`main`). Previously deployed by drag-and-drop; imported from the published site on 2026-10-19.
- Hosting: Netlify, publish directory `.` (no build step). Config in `netlify.toml`.
- Every push to `main` deploys automatically once Netlify is linked to this repository.
- Sister site: AATTRL One (software product) at https://one.aattrl.com, repository `inba40/aattrl-one-site`.

## Editing

Pages are plain HTML under their URL path (`services/hazop/index.html` → `/services/hazop/`). Shared header and footer markup is repeated in every file; change it with a careful find-and-replace across all `*.html` files, as done for the "AATTRL One" menu link.

## Changelog

- 2026-10-19 — Imported published site; added "AATTRL One" link to the main navigation (before About) and the footer Company column; added `netlify.toml` with security and cache headers.
