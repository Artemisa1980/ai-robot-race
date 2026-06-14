# Relay Log — AI Robot Race Document

## 2026-06-14 — Opus 4.8 — Scaffolding
**Phase:** Phase 0 (environment & scaffolding)
**Completed:** Installed Quarto 1.9.38 (Pandoc 3.8.3, Typst 0.14.2, Dart Sass 1.87.0, LaTeX OK). Created README, framework, relay-log, claims-ledger; Quarto book project under `report/` with 13 chapter stubs, `_quarto.yml`, `apa.csl` (85 KB), empty `references.bib`, SanBlueDot theme.
**Render check (Task 7):** PASSED — `_output/` has the HTML site (index + 13 chapters + search.json) and `The-AI-Robot-Race-and-Its-Hidden-Cost.pdf` (Typst). Pipeline proven.
**Next step:** Task 6 — confirm with Sandy before moving drafts into `sources/`; then Phase 1 (Task 8: create the `peer-review` skill).
**Issues:** None. PDF engine = Typst.
**Files changed:** README.md, framework.md, relay-log.md, claims-ledger.md, report/* (config + stubs + theme)

## 2026-06-14 — Opus 4.8 — Sources moved + peer-review skill
**Phase:** Phase 0 (Task 6) + Phase 1 (Task 8) — complete
**Completed:** Moved the 12 research drafts into `sources/` (raw material, reversible). Created the `peer-review` skill at `~/.claude/skills/peer-review/SKILL.md` — constructive scholarly referee, 7-step method, verdict + numbered revisions, explicit boundary vs `brutal-critic`. Heavy eval/benchmark loop intentionally skipped (subjective skill, token cost, Solo Creator). Real test = use on Chapter 1.
**Next step:** Phase 2, Task 11 — research + verify + draft **Chapter 1 (The Superpower Duel)** via the Chapter Production Protocol (plan Task 9). Heavy/token-intensive research begins here.
**Issues:** None.
**Files changed:** sources/* (moved), ~/.claude/skills/peer-review/SKILL.md, relay-log.md

## 2026-06-14 — Opus 4.8 — Chapter 1 drafted + peer-reviewed
**Phase:** Phase 2, Task 11 — Chapter 1 (The Superpower Duel)
**Completed:** Researched + verified 11 claims via web (US vs China strategy, capital, EV/battery, state fund). Wrote chapter with 12 primary-grade sources in references.bib, all logged in claims-ledger.md. Rendered clean to PDF + HTML; APA citations resolve. Ran `peer-review` (first use) → verdict Minor Revisions → applied all 3: fixed "order of magnitude" overreach, added IFR primary source for the ¥1T fund, trimmed unsourced "already-commercial".
**Next step:** `brutal-critic` final pass on Chapter 1 (Sandy pre-authorized), then Task 12 — Chapter 2 (The Economics of a Humanoid / BOM).
**Issues:** None. Battery figure adjusted from drafts' loose "~$100/kWh" to BNEF $94/kWh (China).
**Files changed:** report/01-superpower-duel.qmd, report/references.bib, claims-ledger.md, relay-log.md

## 2026-06-14 — Opus 4.8 — Chapter 1 brutal-critic + fixes
**Phase:** Phase 2, Task 11 — Chapter 1, post-BC corrections
**Completed:** Ran `brutal-critic` (PROFESSIONAL stakes) → verdict FAIL (single-source pricing spine, ambiguous battery baseline, imprecise "half" claim, +7 weaknesses). Fixed all content/sourcing items: added Unitree primary source (G1 now $13,500 current / $16,000 launch — 14th ref... 13 total in bib), attributed the $3.4B to The Robot Report, clarified battery baseline ("31%/48% higher than China's"), replaced "barely half" with real-vs-target framing, scoped EV→robot claim to batteries, softened Digit + hyperbole, added US/China binary nuance + table asymmetry note. Re-rendered clean (13 refs, 0 stray cites).
**Next step:** Chapter 1 is CONDITIONAL PASS — only outstanding item is building the battery chart in Datawrapper (BC #11). Decide: re-run BC to confirm / build chart / start Chapter 2 (BOM — note Morgan Stanley Optimus teardown ~$55K found, verify there).
**Issues:** Figure $2.6B round pre/post-money unspecified by source — left faithful as "reported valuation" rather than guess.
**Files changed:** report/01-superpower-duel.qmd, report/references.bib, claims-ledger.md, relay-log.md
