# Relay Log — AI Robot Race Document

> Handoff baton. **To resume:** open a chat in this folder, say "continuemos el AI Robot Race"; read `core.md` + this log + `claims-ledger.md`. Full per-round review detail lives in git history; every figure's status + source lives in `claims-ledger.md`.

## Project state (2026-06-15)
**Deliverable:** Quarto book under `report/` → print PDF (Typst) + branded HTML site. 10 chapters + front matter (`index.qmd`) + conclusion. Build: `cd report && quarto render`. PDF engine = Typst.
**Done & committed (each: clean PASS through peer-review + brutal-critic):**
- **Ch1 — The Superpower Duel** ✅ — committed `e2c87d8`
- **Ch2 — The Economics of a Humanoid** (BOM; lifecycle: birth) ✅ — committed `c60df2d`
- **Ch3 — Capital & Investment Landscape** ✅ — committed `168ab4d`
- **Ch4 — The Reliability Gap** (lifecycle: working life) ✅ — **brutal-critic CLEAN PASS** (2026-06-15). R1 = FAIL: caught CF1 — the 88%/2.5% stat had the wrong denominator *and* wrong attribution vs the primary (The Robot Report 2019, read verbatim this session); 2.5% is *all robot problems as a share of total available time*, not "2.5% of downtime" and not the arm alone (arm physically breaking ≈0.6% of total time). Also W1 (4%-BOM unqualified), W3 (chart metric mismatch), W4 (unsourced disposal claim), + n.d.→2019 date fix. All fixed; confirmation round caught 2 residual faithfulness nits (denominator term, unsourced "programming") and closed them → PASS. **Uncommitted — awaiting Sandy's word to commit.**
**State:** `references.bib` = 20 entries, all resolve, 0 stray cites. `claims-ledger.md` logs every figure with status (✅/✏️/⚠️/❌) + verification path. Renders clean to PDF + HTML.

## Durable decisions / working patterns
- **Chapter Production Protocol** (plan Task 9): P1 gather (`sources/` = untrusted leads only) → P2 verify each figure to a PRIMARY/authoritative source, log in ledger + `references.bib` → P3 draft `.qmd` in the locked Ch1 style (magazine narrative, in-text `[@key]` APA, a table, one code-gen chart, escape all `$` as `\$`) → P4 render → P5 self-critique vs `framework.md` → P6 `peer-review` → P7 `brutal-critic` loop → P8 log.
- **Charts:** code-generated in-pipeline (matplotlib via `report/figstyle.py` = shared SanBlueDot identity; horizontal-bar house style, amber = the story). NOT Datawrapper. Always rasterize + visually inspect.
- **Sourcing:** primary/authoritative only; no blogs/Medium/Wikipedia. Conflicting figures → sourced range, never an invented midpoint. When a primary page 403s, verify via corroborated secondary and **document the verification path in the ledger** (precedent: Ch2 Goldman/MS, Ch1 $3.4B ⚠️).
- **Review gates:** `peer-review` (auto-OK) then `brutal-critic` (manual — needs Sandy's word for the FIRST launch on a new chapter; once greenlit, loop BC→fix→BC to a clean PASS without re-asking each round — see memory `brutal-critic-loop-to-pass`). **Always re-run BC after a correction round** — rounds 2–4 on Ch2/Ch3 caught defects *introduced by* earlier fixes. Never assume a fix is clean.
- **Commit:** one commit per chapter on `main`, after clean PASS, when Sandy asks.
- **Env:** `pypdf` installed (pip) to read source PDFs; `poppler` NOT installed (Read tool can't render PDF pages — use pypdf text extraction).

## Next step
**Commit Ch4** (clean PASS reached — commit on `main` when Sandy gives the word). Ch4 note: the drafts' "200–500 h humanoid MTBF" was DROPPED (unsourced, model-derived) — chapter argues honestly that humanoid reliability data does not exist; industrial side = FANUC advertised MTBF up to 100,000h (⚠️) + the 88% real-world study (The Robot Report 2019: 80% of stoppages non-robot, robot problems = 2.5% of total available time, arm physically breaking a tiny slice); humanoid = ~2h battery runtime (Bain). `fig-reliability` = log-scale MTBF-vs-runtime, both caption AND on-chart "no MTBF disclosed" own the metric mismatch.
**Then Task 15 — Chapter 5: Trade, Tariffs & Supply Chains.** Verify specific tariff rates + export-control measures to official schedules (USTR / BIS); any "125%/200–300% premium" claims to official source or relabel as estimate. Chart: tariff/bottleneck table or map.
