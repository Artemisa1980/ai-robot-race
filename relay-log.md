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

## 2026-06-14 — Opus 4.8 — Chapter 1 battery chart built (BC #11 CLOSED)
**Phase:** Phase 2, Task 11 — Chapter 1, final outstanding item
**Decision (book-wide):** Charts are **code-generated in-pipeline** (matplotlib via Quarto jupyter engine), NOT Datawrapper. Datawrapper is a hosted GUI — not operable from terminal, manual per chart, breaks single-source. Code cells are reproducible, data version-controlled, auto-embedded in HTML + PDF. Sandy approved.
**Completed:** Created `report/figstyle.py` (shared SanBlueDot chart identity — palette mirrors sanblue.scss, `apply()`/`new()`/`title()`/`source()` helpers; SVG path-text for portable PDF). Added `fig-battery` code cell to Ch1 (China $94 amber / global-avg $115 gray / US $123 / Europe $139 blue — US/EU $ derived from BNEF %, logged in ledger). `_quarto.yml`: added `execute: {echo:false, warning:false, freeze:auto}` + `fig-format: svg`; fixed `output-dir` from `../_output` (outside project, Quarto-warned) to `_output`. Removed stale root `_output`.
**Verification:** Rendered full book clean — HTML + PDF (331k) both built, no output-dir warning. `fig-battery` SVG generated for figure-html + figure-typst and referenced via `<img>`; 13 csl-entries resolve, 0 stray cites. Rasterized chart to PNG and visually inspected — magazine-grade, narrative legible. Chapter 1 = CLEAN PASS on all BC content items; chart no longer pending.
**Next step:** Sandy's call — (A) re-run `brutal-critic` to formally close Ch1 [manual-only skill, needs her explicit word], or (B) advance to Chapter 2 (BOM, Morgan Stanley ~$55K teardown to verify). Uncommitted changes ready when she asks to commit.
**Issues:** None. `_freeze/` intentionally NOT gitignored (Quarto best practice — commit for reproducible render).
**Files changed:** report/figstyle.py (new), report/01-superpower-duel.qmd, report/_quarto.yml, claims-ledger.md, relay-log.md, report/_freeze/* (generated)

## 2026-06-14 — Opus 4.8 — Chapter 1 brutal-critic round 2 + all fixes
**Phase:** Phase 2, Task 11 — Chapter 1, second BC pass + corrections
**Completed:** Re-ran `brutal-critic` (PROFESSIONAL) → FAIL: 1 Critical (CF1) + 7 weaknesses. Web-verified before fixing. Corrected ALL, step by step:
- **CF1** (cross-class price comparison): added honest caveat — G1 is 1.32 m / ~35 kg, smaller/lighter than full-size Optimus/Digit, "not a like-for-like substitute" — while preserving the thesis ("gap far too wide to be explained by size alone").
- **W1** (Tesla target single-trade-sourced): re-sourced to Tesla's own *We, Robot* statement (Oct 2024, $20,000–$30,000) via TechCrunch [techcrunch2024optimus, new 14th ref]; replaced loose "<$30,000".
- **W2** (G1 price-drop config ambiguity): verified unitree.com base = $13,500; clarified both $16K launch and $13.5K now are the **base/standard config**.
- **W3** (chart derived values): caption now states US $123 / EU $139 are derived from BNEF's percentages.
- **W4** (British spelling): centre→center, mobilisation→mobilization (×2, incl. lowercase in footnote that a capitalized replace_all missed), marshalled→marshaled. Verified 0 British spellings remain.
- **W5** ($3.4B single-source): corroboration attempted, none at same scope found — documented honestly in ledger, did NOT fabricate; in-text attribution + "estimated" = mitigation. Status downgraded ✅→⚠️.
- **W6** ("eighteen months"): replaced with exact "By September 2025".
- **W7** (chart "Global avg" as peer bar): converted to a dashed reference line at $115 with white-backed label (clean line break).
**Verification:** Full render clean — HTML + PDF (356k). 14 csl-entries resolve, 0 stray cites, 0 British spellings. Chart re-rasterized + visually inspected twice (reference-line version, then bbox label) — magazine-grade.
**Next step:** Sandy's call — re-run `brutal-critic` to formally confirm PASS (manual-only skill, needs her word), or advance to Chapter 2 (BOM). Uncommitted changes ready to commit when she asks.
**Issues:** None outstanding. All BC findings closed.
**Files changed:** report/01-superpower-duel.qmd, report/references.bib, claims-ledger.md, relay-log.md, report/_freeze/* (regenerated)

## 2026-06-14 — Opus 4.8 — Chapter 1 brutal-critic round 3 → CLEAN PASS + committed
**Phase:** Phase 2, Task 11 — Chapter 1 CLOSED ✅
**Completed:** Re-ran `brutal-critic` (confirmation pass) → CONDITIONAL PASS: all 8 prior findings (CF1, W1–W7) verified genuinely closed; one new minor imprecision found — **N1**: "consumer-electronics prices" overstated $13,500. Fixed → "for the price of a used car" (accurate, and echoes Musk's "less than a car"). Re-rendered clean: HTML + PDF (356k), 14 refs resolve, 0 stray cites, 0 British spellings, chart magazine-grade. **Chapter 1 is now a clean PASS and the locked template for Chapters 2–10.** Committed everything to git on `main`.
**Working pattern established (Sandy's instruction):** always re-run `brutal-critic` after a correction round to confirm closure — never assume fixes are clean.
**Next step (LATER — paused by Sandy):** Chapter 2 — *The Economics of a Humanoid* (BOM). Lead to verify: Morgan Stanley Optimus Gen-2 teardown ≈ $55K BOM (legs ~$21K/38.6%, hands ~$9.5K/17.2%) — must verify against a non-blog source before drafting. Apply the Chapter Production Protocol (P1 Gather → P8 Log). Reuse `figstyle.py` for the BOM cost-breakdown chart.
**To resume:** open a chat in this folder, say "continuemos el AI Robot Race"; read core.md + this relay-log + claims-ledger; start Chapter 2.
**Issues:** None. Working tree clean after commit.
**Files changed:** report/01-superpower-duel.qmd, relay-log.md, report/_freeze/* (regenerated), + git commit
