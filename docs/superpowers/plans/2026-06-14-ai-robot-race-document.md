# The AI Robot Race and Its Hidden Cost — Document Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build Deliverable #1 — an exhaustive, source-verified English research report ("The AI Robot Race and Its Hidden Cost") as a Quarto **book** rendering to both print-quality PDF (Typst) and a clean branded HTML site.

**Architecture:** A Quarto book project under `report/`. Each chapter is its own `.qmd` (one responsibility per file). Every factual claim is logged in `claims-ledger.md` with a verification status and a primary source recorded in `references.bib`; Quarto generates APA-7 citations and the reference list. Production runs chapter-by-chapter through a fixed Chapter Production Protocol gated by `peer-review` + `brutal-critic`, with `relay-log.md` updated each phase for cross-session handoff.

**Tech Stack:** Quarto (book project), Typst (PDF engine), APA-7 CSL, Datawrapper (charts), custom SCSS (SanBlueDot brand). Optional: `git` for version history; `gemini-research` skill for source gathering.

**Adaptation note:** This is a research-document build, not a software build. The TDD "red→green→commit" loop is adapted to "define the acceptance gate (claims to source + render must pass) → produce → verify against sources and render." The per-chapter mechanical pipeline is identical across all 10 chapters, so it is defined ONCE as the **Chapter Production Protocol** (Task 9) and each chapter task (Tasks 10–21) supplies only its chapter-specific research targets and acceptance gate. This is deliberate DRY — the differing content per chapter is the research, not the mechanics.

---

## File Structure

```
ai-race/
├── README.md                       # What the project is (conductor.md per-project)
├── framework.md                    # The rubric peer-review + brutal-critic check against
├── relay-log.md                    # Handoff baton between sessions/models
├── claims-ledger.md                # Every key figure → status (✅/✏️/⚠️/❌) → source key
├── sources/                        # Existing drafts moved here = raw material, not truth
│   └── (the current .md / .pdf / .docx research files)
├── report/                         # The Quarto book (the document itself)
│   ├── _quarto.yml                 # Book config: HTML + Typst PDF, bib, csl
│   ├── index.qmd                   # Front matter: Abstract + Key Findings
│   ├── 01-superpower-duel.qmd
│   ├── 02-economics-of-a-humanoid.qmd
│   ├── 03-capital-investment.qmd
│   ├── 04-reliability-gap.qmd
│   ├── 05-trade-tariffs.qmd
│   ├── 06-adoption-generational.qmd
│   ├── 07-fast-hardware.qmd
│   ├── 08-ewaste-wave.qmd
│   ├── 09-circular-economy.qmd
│   ├── 10-net-reckoning.qmd
│   ├── conclusion.qmd
│   ├── references.qmd              # "References" chapter (auto-filled by Quarto)
│   ├── references.bib              # APA source ledger
│   ├── apa.csl                     # APA-7 citation style
│   ├── theme/
│   │   └── sanblue.scss            # SanBlueDot brand theme (HTML)
│   └── figures/                    # Exported Datawrapper charts + original diagrams
└── docs/superpowers/
    ├── specs/2026-06-14-ai-robot-race-document-design.md   # (exists)
    └── plans/2026-06-14-ai-robot-race-document.md          # (this file)
```

---

## PHASE 0 — Environment & Scaffolding

### Task 1: Verify the toolchain

**Files:** none (environment check).

- [ ] **Step 1: Check Quarto is installed**

Run: `quarto --version`
Expected: a version number `1.4` or higher (book + Typst support). If "command not found", stop and install Quarto from https://quarto.org/docs/get-started/ before continuing.

- [ ] **Step 2: Check Quarto's environment and Typst availability**

Run: `quarto check`
Expected: output shows `[✓] Checking Quarto installation` and a Typst version under the formats section. If Typst is missing, note it; Task 3 contingency covers the fallback.

- [ ] **Step 3: Record the result in relay-log (created in Task 2)**

No action yet — note the versions; they get written into `relay-log.md` in Task 2, Step 3.

- [ ] **Step 4: Confirm Datawrapper access**

Datawrapper is a web app (no install). Confirm a free account exists at https://www.datawrapper.de/ . Charts are created there and exported as SVG/PNG into `report/figures/`. No command to run.

---

### Task 2: Create the conductor.md project files

**Files:**
- Create: `README.md`
- Create: `framework.md`
- Create: `relay-log.md`

- [ ] **Step 1: Create `README.md`**

```markdown
# The AI Robot Race and Its Hidden Cost

SanBlueDot independent research. A 10-year outlook (2025–2035) on the US–China
race in embodied AI / humanoid robotics **and** its hidden cost (e-waste,
obsolescence, circular economy).

- **Design spec:** `docs/superpowers/specs/2026-06-14-ai-robot-race-document-design.md`
- **Plan:** `docs/superpowers/plans/2026-06-14-ai-robot-race-document.md`
- **The document:** `report/` (Quarto book → PDF + HTML)
- **Source ledger:** `claims-ledger.md` + `report/references.bib`
- **Raw material (unverified drafts):** `sources/`

Build: `cd report && quarto render`
```

- [ ] **Step 2: Create `framework.md` (the review rubric)**

```markdown
# Review Framework — what peer-review and brutal-critic check against

A chapter or the document is APPROVED only when ALL hold:

## Sourcing (hard gate)
- [ ] Every figure/claim is ✅ Verified (primary source in references.bib),
      ✏️ Adjusted to match source, or ⚠️ Estimate (labeled, method stated).
      ZERO ❌/unlabeled numbers remain.
- [ ] No blog / Medium / Stack Overflow / Wikipedia / marketing cited as a source.
- [ ] Conflicting figures shown as a sourced range, never an invented midpoint.

## Rigor (peer-review)
- [ ] Claims are supported by the evidence cited (no overreach).
- [ ] Methodology of any estimate/scenario is stated and reproducible.
- [ ] Citations are sufficient and current (prefer 2024–2026 where the topic moves fast).

## Craft (brutal-critic)
- [ ] No filler, no placeholder text, no hand-waving.
- [ ] Reads as coherent narrative; the lifecycle thread is visible.
- [ ] Tables/charts are accurate, labeled, and sourced.

## Consistency
- [ ] Units, currency (USD), and time horizon (2025–2035) consistent with siblings.
- [ ] No figure contradicts another chapter.

Verdict per review: **APPROVED** or **REVISIONS NEEDED** (list specific issues).
```

- [ ] **Step 3: Create `relay-log.md` with the first entry**

```markdown
# Relay Log — AI Robot Race Document

## 2026-06-14 — Opus 4.8 — Scaffolding
**Phase:** Phase 0 (environment & scaffolding)
**Completed:** Verified toolchain (record quarto/typst versions here); created README, framework, relay-log.
**Next step:** Task 3 — initialize the Quarto book project.
**Issues:** None.
**Files changed:** README.md, framework.md, relay-log.md
```

---

### Task 3: Initialize the Quarto book project

**Files:**
- Create: `report/_quarto.yml`
- Create: `report/apa.csl` (downloaded)
- Create: `report/references.bib` (empty starter)

- [ ] **Step 1: Create the chapter `.qmd` stubs**

Create `report/index.qmd` and the eleven chapter files (`01-superpower-duel.qmd` … `10-net-reckoning.qmd`, `conclusion.qmd`, `references.qmd`). Each stub is exactly one title line so the book renders; content comes in Phase 2. Example for `report/index.qmd`:

```markdown
# Abstract {.unnumbered}

_Front matter — Abstract and Key Findings. Written in Task 10._
```

And `report/references.qmd`:

```markdown
# References {.unnumbered}

::: {#refs}
:::
```

- [ ] **Step 2: Create `report/_quarto.yml`**

```yaml
project:
  type: book
  output-dir: ../_output

book:
  title: "The AI Robot Race and Its Hidden Cost"
  subtitle: "A 10-Year Outlook (2025–2035) — USA vs. China"
  author: "Sandy E. Quintero — SanBlueDot"
  date: "2026"
  chapters:
    - index.qmd
    - 01-superpower-duel.qmd
    - 02-economics-of-a-humanoid.qmd
    - 03-capital-investment.qmd
    - 04-reliability-gap.qmd
    - 05-trade-tariffs.qmd
    - 06-adoption-generational.qmd
    - 07-fast-hardware.qmd
    - 08-ewaste-wave.qmd
    - 09-circular-economy.qmd
    - 10-net-reckoning.qmd
    - conclusion.qmd
    - references.qmd

bibliography: references.bib
csl: apa.csl

format:
  html:
    theme:
      - cosmo
      - theme/sanblue.scss
    toc: true
    number-sections: true
  typst:
    toc: true
    number-sections: true
```

- [ ] **Step 3: Download the APA-7 CSL style**

Run: `curl -L -o report/apa.csl https://raw.githubusercontent.com/citation-style-language/styles/master/apa.csl`
Expected: `report/apa.csl` exists and is non-empty (`test -s report/apa.csl && echo OK` prints `OK`).

- [ ] **Step 4: Create an empty `report/references.bib`**

```bibtex
% APA source ledger — entries added per chapter during Phase 2.
```

- [ ] **Step 5: Contingency — if `quarto check` (Task 1) showed no Typst**

If Typst is unavailable and cannot be installed, change the `typst:` block in `_quarto.yml` to LaTeX PDF:
```yaml
  pdf:
    toc: true
    number-sections: true
    documentclass: scrreprt
```
and run `quarto install tinytex` to get a LaTeX engine. Record which PDF engine is in use in `relay-log.md`.

---

### Task 4: Create the SanBlueDot HTML theme

**Files:**
- Create: `report/theme/sanblue.scss`

- [ ] **Step 1: Write the brand theme**

Starter palette/typography (tune the exact hex from `sanblue-logo-m13.png` during execution; these are real working values, not placeholders):

```scss
/*-- scss:defaults --*/
$sanblue:       #1f4e8c;   // primary deep blue
$sanblue-dark:  #14223f;   // headings / cover
$sanblue-accent:#e8a13a;   // amber accent for pull-quotes/highlights
$gray-100:      #f6f8fb;

$font-family-sans-serif: "Inter", "Helvetica Neue", Arial, sans-serif;
$font-family-serif:      "Source Serif 4", Georgia, serif;
$body-color:    #1b1f24;
$link-color:    $sanblue;
$h1-font-size:  2.2rem;

/*-- scss:rules --*/
h1, h2, h3 { color: $sanblue-dark; font-family: $font-family-sans-serif; letter-spacing: -0.01em; }
body { font-family: $font-family-serif; line-height: 1.65; }
blockquote {
  border-left: 4px solid $sanblue-accent;
  background: $gray-100;
  font-size: 1.1rem; font-style: italic; padding: 0.75rem 1.25rem;
}
.lifecycle-tag { color: $sanblue; font-weight: 600; font-variant: small-caps; }
```

---

### Task 5: Create the source ledger

**Files:**
- Create: `claims-ledger.md`

- [ ] **Step 1: Write the ledger scaffold with its legend and column format**

```markdown
# Claims Ledger

Every key figure in the report lives here before it lives in a chapter.

**Status:** ✅ Verified · ✏️ Adjusted · ⚠️ Estimate (labeled) · ❌ Discarded

| Chapter | Claim / figure | Value used | Status | Source key (references.bib) | Notes |
|---------|----------------|-----------|--------|-----------------------------|-------|
| 02 | Humanoid BOM: actuators share of cost | 35–40% | ⬜ | — | to verify |

(Replace the example row as real claims are verified.)
```

---

### Task 6: Organize existing drafts as raw material

**Files:**
- Move: the current research files into `sources/`

- [ ] **Step 1: Create `sources/` and move the drafts (reversible)**

Run:
```bash
cd /Users/ahsokartemisa/Documents/Code-ai/research/ai-race
mkdir -p sources
mv AI_Robot_Race_10_Year_Outlook.md AI_Robot_Race_10_Year_Outlook.pdf \
   AI_Robotics_Hidden_Cost_Report.pdf AI-Robot-Analysis.md \
   deep-research-report.md g-ai-robotica.md \
   "Impacto económico y residuos de la robótica con IA (2024–2034).docx" \
   "Impacto económico y residuos de la robótica con IA (2024–2034).pdf" \
   Impacto_Economico_Residuos_Extracted.md \
   "The AI Robot Race_ A 10-Year Outlook (2025–2035) — USA vs. China.docx" \
   The_AI_Robot_Race_Extracted.md unified_report.md \
   sources/
```
Expected: `ls sources/` lists all moved files; the project root now holds only `README.md`, `framework.md`, `relay-log.md`, `claims-ledger.md`, the images/logos, `report/`, `docs/`, and `sources/`.

- [ ] **Step 2: Confirm with Sandy before moving** (her files — surface, don't assume). If she prefers to keep them in place, skip the move and have chapters reference them at the root instead.

---

### Task 7: Prove the pipeline — render the empty skeleton

**Files:** none (build verification — this is the Phase 0 "green" gate).

- [ ] **Step 1: Render the book**

Run: `cd report && quarto render`
Expected: completes without error; creates `_output/` with `index.html` (HTML site) and a `.pdf`.

- [ ] **Step 2: Confirm both outputs exist**

Run: `ls _output/*.pdf && ls _output/index.html`
Expected: both paths print. If the PDF step failed, apply Task 3 Step 5 contingency, then re-render.

- [ ] **Step 3: Update `relay-log.md`**

Add an entry: Phase 0 complete, pipeline renders to PDF + HTML, note PDF engine used. Next step: Task 8.

- [ ] **Step 4 (optional): Initialize git for version history**

Ask Sandy. If yes:
```bash
cd /Users/ahsokartemisa/Documents/Code-ai/research/ai-race
git init && printf "_output/\n.quarto/\n.DS_Store\n" > .gitignore
git add -A && git commit -m "scaffold: project structure, Quarto book, theme, ledger"
```

---

## PHASE 1 — Review Gate Ready

### Task 8: Create the `peer-review` skill (just-in-time)

**Files:**
- Create: `~/.claude/skills/peer-review/SKILL.md` (via skill-creator)

- [ ] **Step 1: Invoke skill-creator**

Use the `skill-creator` skill to scaffold a new skill named `peer-review`.

- [ ] **Step 2: Define it with a SHARP boundary from brutal-critic**

The skill MUST encode the academic-referee method and explicitly differ from `brutal-critic`:
- **Role:** constructive scholarly referee (not adversarial destroyer).
- **Method (in order):** (1) summarize the work's contribution; (2) assess significance/novelty; (3) test methodological soundness; (4) check each claim against its cited evidence; (5) judge citation adequacy and currency; (6) check reproducibility of estimates/scenarios; (7) give a verdict — *accept / minor revisions / major revisions / reject* — with a numbered list of required revisions.
- **Standard:** inherits `core.md` Source-or-Silence; checks against the project's `framework.md`.
- **Boundary line (write this into the skill):** "Use `brutal-critic` for the savage adversarial sweep. Use `peer-review` for structured scholarly rigor. They run in sequence, not instead of each other."

- [ ] **Step 3: Smoke-test the skill**

Invoke `peer-review` on `framework.md` itself and confirm it returns the 7-part structure and a verdict. If it just behaves like a generic critic, tighten the description until the boundary holds.

- [ ] **Step 4: Update `relay-log.md`** — Phase 1 done, review gate ready. Next: Task 9 protocol + Task 10 first chapter.

---

## PHASE 2 — Chapter Production

### Task 9: The Chapter Production Protocol (reference for Tasks 10–21)

This protocol runs for EVERY content task below. Do not skip steps.

- [ ] **P1 — Gather:** pull the relevant material from `sources/` as *leads only*. List every figure/claim the chapter needs.
- [ ] **P2 — Verify:** for each figure, find the **primary source** (web search / `gemini-research` to gather, then verify independently). Add a `references.bib` entry and a `claims-ledger.md` row with status ✅/✏️/⚠️; drop ❌ items. **No unsourced number proceeds.**
- [ ] **P3 — Draft:** write the chapter `.qmd` in English, hybrid register, with in-text citations `[@key]`, the lifecycle stage tagged, and any tables. Mark each chart with a placeholder note `<!-- chart: figures/NN-name.svg (Datawrapper) -->` and build the chart in Datawrapper, exporting to `report/figures/`.
- [ ] **P4 — Render check:** `cd report && quarto render` — Expected: no errors, citations resolve (no `[?]` in output), chapter appears in PDF + HTML.
- [ ] **P5 — Self-critique:** run the Working Loop (`core.md` §5) against `framework.md`.
- [ ] **P6 — peer-review:** run the `peer-review` skill on the chapter. Apply required revisions.
- [ ] **P7 — brutal-critic:** run `brutal-critic` on the chapter. Apply fixes until verdict is PASS.
- [ ] **P8 — Log:** mark the chapter APPROVED in `relay-log.md` with the figure count verified; update `claims-ledger.md`.

---

### Task 10: Front matter — Abstract & Key Findings

**Files:** Modify: `report/index.qmd`

- [ ] Run the full Chapter Production Protocol (Task 9) with these specifics:
  - **Content:** a ~250-word abstract stating the thesis (*who wins once the hidden cost is priced in?*) and a bulleted **Key Findings** list (5–7 findings, each tied to a verified figure).
  - **Acceptance gate:** every number in Key Findings already exists as ✅/✏️/⚠️ in `claims-ledger.md` (write this chapter LAST in practice if findings depend on later chapters — note that in relay-log).

---

### Task 11: Chapter 1 — The Superpower Duel

**Files:** Modify: `report/01-superpower-duel.qmd`

- [ ] Run the Chapter Production Protocol (Task 9) with these specifics:
  - **Claims to verify:** US "software-first/capital" vs China "hardware-first/state-subsidized" framing; China's EV-supply-chain leverage; existence of national strategies (e.g., China's robotics/AI plans; US federal robotics funding bodies).
  - **Target sources:** IFR World Robotics 2024/2025; official Chinese MIIT robotics guidance; US national strategy/agency documents; reputable analyst overviews (verified to primary).
  - **Charts:** one comparison graphic of the two strategic models.
  - **Acceptance gate:** strategy claims are sourced to official/primary documents, not journalism.

---

### Task 12: Chapter 2 — The Economics of a Humanoid

**Files:** Modify: `report/02-economics-of-a-humanoid.qmd`

- [ ] Run the Chapter Production Protocol (Task 9) with these specifics:
  - **Claims to verify:** BOM share by component (actuators 35–40%, batteries 15–20%, compute 10–15%); per-unit build cost US vs China. **The drafts conflict ($24.4k/$15.5k vs $71k/$46.1k) — neither is trusted.** Resolve to a sourced figure or present a sourced range with the spec assumption (robot class, year).
  - **Target sources:** analyst BOM teardowns (e.g., Morgan Stanley/Goldman humanoid notes), battery $/kWh from BNEF or equivalent, actuator/reducer supplier economics.
  - **Charts:** the component-level BOM comparison table + a stacked-bar chart (Datawrapper).
  - **Acceptance gate:** the per-unit total is reproducible from the line items shown; the conflicting-draft numbers are explicitly reconciled in `claims-ledger.md`. *(lifecycle: birth)*

---

### Task 13: Chapter 3 — Capital & Investment Landscape

**Files:** Modify: `report/03-capital-investment.qmd`

- [ ] Run the Chapter Production Protocol (Task 9) with these specifics:
  - **Claims to verify:** named funders/valuations on both sides (verify each company/fund and any valuation to a primary or filing-grade source; discard unverifiable ones).
  - **Target sources:** company announcements, funding databases traceable to primary, government budget lines.
  - **Charts:** capital-flow comparison (US private capital vs China state-backed).
  - **Acceptance gate:** no valuation/figure cited from a blog; each named investor is verified to exist in the stated role.

---

### Task 14: Chapter 4 — The Reliability Gap

**Files:** Modify: `report/04-reliability-gap.qmd`

- [ ] Run the Chapter Production Protocol (Task 9) with these specifics:
  - **Claims to verify:** humanoid maintenance interval (200–500 operating hours) vs industrial-arm MTBF (50,000+ hours).
  - **Target sources:** industrial-robot MTBF from manufacturer/standards data (e.g., ISO/manufacturer reliability specs); humanoid figures to the most authoritative available, labeled ⚠️ Estimate if only analyst-grade.
  - **Charts:** MTBF comparison bar (log scale).
  - **Acceptance gate:** the 50,000+ h industrial figure is sourced to a manufacturer/standard, not asserted. *(lifecycle: working life)*

---

### Task 15: Chapter 5 — Trade, Tariffs & Supply Chains

**Files:** Modify: `report/05-trade-tariffs.qmd`

- [ ] Run the Chapter Production Protocol (Task 9) with these specifics:
  - **Claims to verify:** specific tariff rates and export-control measures affecting robotics components/chips; any "125%/200–300% premium" claims (the drafts assert these — verify or relabel as estimate).
  - **Target sources:** USTR / official tariff schedules, BIS export-control rules, primary trade data.
  - **Charts:** tariff/supply-chain bottleneck map or table.
  - **Acceptance gate:** every tariff percentage traces to an official schedule or is dropped.

---

### Task 16: Chapter 6 — Adoption & Generational Dynamics

**Files:** Modify: `report/06-adoption-generational.qmd`

- [ ] Run the Chapter Production Protocol (Task 9) with these specifics:
  - **Claims to verify:** market-size forecasts — present as a **sourced range** (e.g., Goldman Sachs ~$38B by 2035 ↔ Roland Berger up to ~$750B), each tied to its original report; data-scarcity-for-training claim; generational-trust data.
  - **Target sources:** the original Goldman Sachs and Roland Berger humanoid reports; survey data for generational attitudes (Pew/Statista-to-primary).
  - **Charts:** forecast-range chart showing the spread across analysts.
  - **Acceptance gate:** no single invented market number — only the sourced range.

---

### Task 17: Chapter 7 — Fast Hardware

**Files:** Modify: `report/07-fast-hardware.qmd`

- [ ] Run the Chapter Production Protocol (Task 9) with these specifics:
  - **Claims to verify:** GPU/accelerator obsolescence window (12–18 months); industrial-robot service life (10+ yrs, ABB 35-yr machines) vs consumer-robot replacement (3–5 yrs).
  - **Target sources:** ABB/manufacturer lifecycle statements; data-center hardware refresh-cycle analyses traced to primary.
  - **Charts:** lifespan comparison (frontier compute vs industrial vs consumer).
  - **Acceptance gate:** the "Fast Hardware" thesis rests on at least two sourced lifecycle figures. *(lifecycle: obsolescence)*

---

### Task 18: Chapter 8 — The Coming Wave of Robotic E-Waste

**Files:** Modify: `report/08-ewaste-wave.qmd`

- [ ] Run the Chapter Production Protocol (Task 9) with these specifics:
  - **Claims to verify:** installed base & annual installs (IFR: 542k installed 2024, ~4.66M in operation, China 54%/295k, US 6%/34.2k — verify each to IFR); retired-unit volume scenarios; metal/material mass per unit (ABB IRB 6640 ≈ 1.4 t).
  - **Target sources:** IFR World Robotics; the Global E-waste Monitor; manufacturer material specs.
  - **Charts:** install base + projected retirement-wave scenarios (high/medium/low) chart and table.
  - **Acceptance gate:** all IFR figures match the IFR source exactly; scenario assumptions stated and labeled ⚠️. *(lifecycle: death)*

---

### Task 19: Chapter 9 — The Circular Economy Response

**Files:** Modify: `report/09-circular-economy.qmd`

- [ ] Run the Chapter Production Protocol (Task 9) with these specifics:
  - **Claims to verify:** reuse rate (ABB 60–80% reusable; remanufacture emissions savings); e-waste recycling market size/CAGR; RaaS/secondary-market existence; sustainable-materials research (e.g., DeepMind GNoME) verified to primary.
  - **Target sources:** ABB circularity reports; recycling-market reports traced to primary; the GNoME paper (Nature) directly.
  - **Charts:** circular-flow diagram (original) + recycling-market growth chart.
  - **Acceptance gate:** GNoME and any "X million" claims cited to the primary paper/report, not press. *(lifecycle: afterlife)*

---

### Task 20: Chapter 10 — The Net Reckoning & Solutions

**Files:** Modify: `report/10-net-reckoning.qmd`

- [ ] Run the Chapter Production Protocol (Task 9) with these specifics:
  - **Content:** synthesize Acts I–II into the economic–environmental balance; policy (extended producer responsibility); neuromorphic/sustainable-hardware outlook.
  - **Target sources:** EPR policy texts; neuromorphic-computing efficiency claims to primary research.
  - **Acceptance gate:** every solution claim is sourced; speculative futures are labeled as such, not stated as fact.

---

### Task 21: Conclusion

**Files:** Modify: `report/conclusion.qmd`

- [ ] Run the Chapter Production Protocol (Task 9) with these specifics:
  - **Content:** answer the thesis — *who really wins once the hidden cost is priced in?* — drawing only on figures already verified in earlier chapters. No new unsourced claims.
  - **Acceptance gate:** zero new figures that aren't already ✅/✏️/⚠️ in `claims-ledger.md`.

---

## PHASE 3 — Integration & Final Gates

### Task 22: Cross-chapter consistency pass

**Files:** Modify: any `report/*.qmd` with inconsistencies; Modify: `claims-ledger.md`

- [ ] **Step 1:** Read all chapters; list every figure that appears in more than one chapter.
- [ ] **Step 2:** Confirm each repeated figure uses the same value, unit (USD), and 2025–2035 horizon. Fix mismatches.
- [ ] **Step 3:** Confirm `claims-ledger.md` has no ⬜ (unreviewed) or ❌ rows remaining in used claims.
- [ ] **Step 4:** `cd report && quarto render` — Expected: no errors, no `[?]` unresolved citations anywhere.

---

### Task 23: Reference & citation integrity

**Files:** Modify: `report/references.bib`

- [ ] **Step 1:** Confirm every `[@key]` used in chapters has a matching `references.bib` entry.

Run: `grep -ohR "@[A-Za-z0-9_-]\+" report/*.qmd | sort -u` and confirm each key exists in `references.bib`.

- [ ] **Step 2:** Render and visually confirm the **References** chapter lists all sources in APA-7 format, alphabetized.
- [ ] **Step 3:** Spot-check 5 random references against their primary source URLs.

---

### Task 24: Brand & visual QA

**Files:** Modify: `report/theme/sanblue.scss`, `report/figures/*` as needed

- [ ] **Step 1:** Render HTML; confirm SanBlueDot theme (colors from `sanblue-logo-m13.png`, fonts, pull-quotes) applies and charts display.
- [ ] **Step 2:** Open the PDF; confirm cover, TOC, headings, tables, and chart images render at print quality.
- [ ] **Step 3:** Confirm every chart in `report/figures/` is labeled and sourced in its caption.

---

### Task 25: Final review gates on the whole document

**Files:** none (review); then Modify chapters per findings.

- [ ] **Step 1:** Run `peer-review` on the assembled document (not just chapters). Apply required revisions.
- [ ] **Step 2:** Run `brutal-critic` on the assembled document. Fix until PASS.
- [ ] **Step 3:** Re-render; confirm clean PDF + HTML.
- [ ] **Step 4:** Update `relay-log.md`: **Document APPROVED**. Record final figure count, source count, page count.
- [ ] **Step 5 (if git):** `git add -A && git commit -m "feat: complete AI Robot Race document (verified)"`

---

## Self-Review (completed by author of this plan)

**1. Spec coverage:** Goal ✓(T1–25) · two-thread merge ✓(chapters T11–21) · hybrid+APA ✓(T3,T23) · verify+expand ✓(T9 P2, per-chapter sources) · structure-driven length ✓(chapter tasks, flex noted) · two-act spine ✓(chapter order) · lifecycle thread ✓(tagged T12,14,17,18,19) · Quarto→PDF+HTML ✓(T3,T7) · Datawrapper ✓(T9 P3,T24) · SanBlueDot theme ✓(T4,T24) · sourcing protocol ✓(T5,T9,framework) · per-figure status ✓(T5) · drafts=raw material ✓(T6,T9 P1) · conflict=range ✓(T12,T16) · workflow+relay-log ✓(T9,every phase) · peer-review skill ✓(T8) · success criteria ✓(T22–25). No gaps found.

**2. Placeholder scan:** No "TBD/TODO/implement later". The chart marker `<!-- chart: ... -->` is an intentional in-draft pointer paired with an immediate Datawrapper build step, not a deferred placeholder. Theme hex values are real working defaults to be tuned, not placeholders.

**3. Consistency:** File names match between the File Structure map, `_quarto.yml` (Task 3), and chapter tasks (T10–21). Status symbols (✅/✏️/⚠️/❌) consistent across `framework.md`, `claims-ledger.md`, and Task 9. PDF engine (Typst, with LaTeX contingency) consistent between Task 3 and Task 7.

**Out of scope (own future plans):** web experience (#3), video (#4); the `peer-review` skill gets a deeper cycle later but a working version is built in Task 8.
