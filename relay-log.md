# Relay Log — AI Robot Race Document

> Handoff baton. **To resume:** open a chat in this folder, say "continuemos el AI Robot Race"; read `core.md` + this log + `claims-ledger.md`. Full per-round review detail lives in git history; every figure's status + source lives in `claims-ledger.md`.

## Project state (2026-06-15)
**Deliverable:** Quarto book under `report/` → print PDF (Typst) + branded HTML site. 10 chapters + front matter (`index.qmd`) + conclusion. Build: `cd report && quarto render`. PDF engine = Typst.
**Done & committed (each: clean PASS through peer-review + brutal-critic):**
- **Ch1 — The Superpower Duel** ✅ — committed `e2c87d8`
- **Ch2 — The Economics of a Humanoid** (BOM; lifecycle: birth) ✅ — committed `c60df2d`
- **Ch3 — Capital & Investment Landscape** ✅ — committing now
**State:** `references.bib` = 20 entries, all resolve, 0 stray cites. `claims-ledger.md` logs every figure with status (✅/✏️/⚠️/❌) + verification path. Renders clean to PDF + HTML.

## Durable decisions / working patterns
- **Chapter Production Protocol** (plan Task 9): P1 gather (`sources/` = untrusted leads only) → P2 verify each figure to a PRIMARY/authoritative source, log in ledger + `references.bib` → P3 draft `.qmd` in the locked Ch1 style (magazine narrative, in-text `[@key]` APA, a table, one code-gen chart, escape all `$` as `\$`) → P4 render → P5 self-critique vs `framework.md` → P6 `peer-review` → P7 `brutal-critic` loop → P8 log.
- **Charts:** code-generated in-pipeline (matplotlib via `report/figstyle.py` = shared SanBlueDot identity; horizontal-bar house style, amber = the story). NOT Datawrapper. Always rasterize + visually inspect.
- **Sourcing:** primary/authoritative only; no blogs/Medium/Wikipedia. Conflicting figures → sourced range, never an invented midpoint. When a primary page 403s, verify via corroborated secondary and **document the verification path in the ledger** (precedent: Ch2 Goldman/MS, Ch1 $3.4B ⚠️).
- **Review gates:** `peer-review` (auto-OK) then `brutal-critic` (manual — needs Sandy's word for the FIRST launch on a new chapter; once greenlit, loop BC→fix→BC to a clean PASS without re-asking each round — see memory `brutal-critic-loop-to-pass`). **Always re-run BC after a correction round** — rounds 2–4 on Ch2/Ch3 caught defects *introduced by* earlier fixes. Never assume a fix is clean.
- **Commit:** one commit per chapter on `main`, after clean PASS, when Sandy asks.
- **Env:** `pypdf` installed (pip) to read source PDFs; `poppler` NOT installed (Read tool can't render PDF pages — use pypdf text extraction).

## Next step
**Task 14 — Chapter 4: The Reliability Gap** (lifecycle: working life). Verify: humanoid maintenance interval ~200–500 operating hours vs industrial-arm MTBF 50,000+ hours — the **50,000h must be sourced to a manufacturer/standard** (ISO / ABB / FANUC), not asserted; humanoid figure labeled ⚠️ Estimate if only analyst-grade. Chart: MTBF comparison bar (log scale), reuse `figstyle.py`. Run the full Chapter Production Protocol.
