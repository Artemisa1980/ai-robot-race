# The AI Robot Race and Its Hidden Cost — Document Design Spec

> **Project:** SanBlueDot independent research — *The AI Robot Race and Its Hidden Cost: A 10-Year Outlook (2025–2035), USA vs. China*
> **This spec covers Deliverable #1 only: THE DOCUMENT.** Deliverables #2 (peer-review skill), #3 (immersive web experience), #4 (video) each get their own spec/plan cycle later.
> **Date:** 2026-06-14 · **Author team:** Sandy (decision-maker) + Clodi (Conductor)
> **Governs:** inherits `core.md` (constitution) and `conductor.md` (project mode). This file will seed the project's `framework.md` (the rubric Brutal Critic + peer-review check against).

---

## 1. Goal

Produce ONE exhaustive, source-verified English research report that merges Sandy's two existing research threads into a single narrative:

1. **The race** — the US–China contest in embodied AI / humanoid robotics (cost, capital, reliability, trade, adoption).
2. **The hidden cost** — the e-waste, obsolescence, and economic-loss reckoning that the race generates (the circular-economy response).

**Central question (thesis spine):** *Who really wins the AI robot race once you price in its hidden cost?*

## 2. Decisions locked during brainstorming

| # | Decision | Choice |
|---|----------|--------|
| Spine | How the two threads combine | **Merged into one story** — race + hidden cost |
| Type | Register / format | **Hybrid** — academic rigor + formal APA 7 references + report readability & design |
| Depth | Research effort | **Verify existing + expand** with new primary research and 2025–2026 data |
| Length | Size target | **Structure-driven** — length follows what the argument needs (no fixed page count) |
| Narrative | Document spine | **Two acts** (The Race → The Reckoning) |
| Narrative | Video/web spine | **Lifecycle of a robot** (birth → work → obsolescence → death → afterlife) — cross-deliverable decision, applies to #3 and #4 |
| Delivery | Tooling | **Quarto** (single source → PDF + clean HTML), **Datawrapper** charts, **SanBlueDot** CSS/SCSS theme, PDF via **Typst** |
| Sequencing | Build order | Document first (this spec) → then web experience (#3) and video (#4) as derivatives of the verified document |

## 3. Scope

- **Geography:** USA vs. China as the primary axis. EU / Japan referenced only as context where they sharpen the comparison.
- **Time horizon:** 2025–2035 (normalize the e-waste thread's 2024–2034 figures onto this horizon, or state the offset explicitly where a source uses a different window).
- **Audience:** informed readers — business, technology, policy — not only academics. Public-facing flagship under the SanBlueDot brand; also the foundation for the web experience and video.
- **Language:** English output. (Spanish-source material — `deep-research-report.md`, `g-ai-robotica.md`, the `Impacto…` extraction — is translated/synthesized into English, not pasted.)
- **Citations:** APA 7, managed by Quarto from a `.bib` source ledger.

## 4. Architecture — chapter structure

Working title: *The AI Robot Race and Its Hidden Cost: A 10-Year Outlook (2025–2035) — USA vs. China*.
The robot **lifecycle** thread runs through every chapter (stages marked) so the document doubles as the skeleton for the video/web spine.

**Front matter:** Abstract / Executive Summary + Key Findings.

**ACT I — The Race** *(who is winning, and what it costs to win)*
1. **The Superpower Duel** — strategic divergence: US software-first / capital vs. China hardware-first / state-subsidized.
2. **The Economics of a Humanoid** — granular BOM breakdown, US vs. China, and the cost drivers. *(lifecycle: birth — design + manufacturing)*
3. **Capital & Investment Landscape** — who funds it, valuations, capital flows.
4. **The Reliability Gap** — MTBF 200–500 h vs. 50,000+ h; the physical constraint. *(lifecycle: working life)*
5. **Trade, Tariffs & Supply Chains** — export controls, the tariff trap, bottlenecks.
6. **Adoption & Generational Dynamics** — market forecasts (range, e.g. Goldman vs. Roland Berger), data scarcity, generational trust divides.

**ACT II — The Reckoning** *(the hidden cost the race generates)*
7. **Fast Hardware** — the obsolescence engine: 12–18 month cycles; industrial (10+ yr) vs. consumer (3–5 yr) replacement. *(lifecycle: obsolescence)*
8. **The Coming Wave of Robotic E-Waste** — retired-unit volumes, value destroyed, China's obsolescence lead, metals & rare earths lost. *(lifecycle: death)*
9. **The Circular Economy Response** — RaaS, remanufacture/resale, e-waste recycling market, robotic recycling, sustainable-materials research. *(lifecycle: afterlife)*
10. **The Net Reckoning & Solutions** — economic–environmental balance, policy (extended producer responsibility), neuromorphic / sustainable-hardware futures.

**Conclusion** — who really wins once the hidden cost is priced in.
**References (APA 7) + Appendices** — data tables, high/medium/low scenarios.

*Chapter count may flex by ±1–2 during the build if the argument demands it; any change is logged in `relay-log.md`.*

## 5. Delivery format & visuals

- **Source of truth:** Quarto project (`.qmd`), one source rendering to **HTML** (web, interactive charts) and **PDF** (Typst engine, print-quality).
- **Citations:** CSL APA 7 + `references.bib`. Quarto auto-generates in-text cites and the reference list.
- **Charts:** Datawrapper (newsroom-grade, low-code) exported for PDF and embedded in HTML; D3 / Observable Plot only where interactivity adds genuine value. **Three.js is NOT used in the document** — it is reserved for the 3D hero of the web experience (#3).
- **Brand:** SanBlueDot theme via custom SCSS/CSS (typography, palette, pull-quotes, cover) applied to both outputs.
- **Imagery:** original diagrams + data-viz + clearly-labeled conceptual imagery (AI-generated, labeled) or licensed stock. **No fabricated photos of real robots/companies; no unlicensed product photos.**

## 6. Sourcing & verification protocol (the rigor gate)

- **Source standard:** primary / authoritative only — IFR, OECD, original analyst reports (Goldman Sachs, Roland Berger, Morgan Stanley, etc.), company filings, peer-reviewed papers, official bodies. Blogs, Medium, Stack Overflow, Wikipedia, social, marketing = **leads only, never cited** (per `core.md` Source-or-Silence).
- **Per-figure status:** every number is tagged
  - ✅ **Verified** — primary source found; cited.
  - ✏️ **Adjusted** — corrected to match the real source.
  - ⚠️ **Estimate** — our assumption, explicitly labeled as such, method stated.
  - ❌ **Discarded** — unverifiable; removed.
- **Existing drafts = raw material, not truth.** The `【NN†Lxx】`, footnote-number, and `[cite: N]` markers in the extraction files are extraction artifacts, not citations. Treat every inherited figure as a lead to verify; expect to discard AI-confabulated numbers (e.g., the per-unit cost diverges $24.4k/$15.5k vs. $71k/$46.1k across drafts — neither is trusted until sourced).
- **Conflict resolution:** when figures disagree, present the **range with both sources** (do not invent a midpoint), and state the assumption used in any calculation.
- **Research method:** WebSearch / WebFetch and the `gemini-research` skill may *gather* sources quickly, but Clodi **verifies every claim independently** and cites the primary source, not the search result.
- **Source ledger:** `references.bib` (Quarto bibliography) + a `claims-ledger.md` table mapping each key figure → status → source. The peer-review skill and Brutal Critic check the document against this ledger.

## 7. Production & review workflow (data flow + testing)

Built **chapter by chapter, in phases** (Sandy's token constraint). For each chapter:

1. **Research + verify** sources (protocol §6).
2. **Draft** the chapter in Quarto.
3. **Self-critique** against the framework (Working Loop, `core.md` §5).
4. **`peer-review`** pass — scholarly rigor: contribution, methodology, evidence, citation adequacy, reproducibility; verdict + required revisions. *(Skill #2 is created just-in-time before the first review.)*
5. **`brutal-critic`** pass — the savage adversarial sweep for whatever survived.
6. **Fix** → **APPROVED** before moving to the next chapter.
7. **Update `relay-log.md`** each phase so any model/session can resume.

**Mode (conductor.md):** primarily Solo Creator for the synthesis/narrative voice (one mind owns the through-line), with research gathering optionally parallelized. The unifying prose stays single-voiced.

## 8. Success criteria

- Every claim, figure, and table is either sourced to a primary reference or explicitly labeled an estimate. Zero silent unverified numbers.
- Internal consistency: no figure contradicts another across chapters; one consistent time horizon and units.
- Both outputs render cleanly: PDF (Typst) and HTML, with working APA references and charts.
- Passes the `peer-review` gate and the `brutal-critic` gate.
- Reads as a coherent two-act narrative that a non-academic informed reader can follow, while standing up to academic scrutiny.

## 9. Out of scope (separate specs later)

- **#2** Creating the `peer-review` skill (built just-in-time as the review gate; its own skill-creation cycle).
- **#3** The immersive web experience (HTML + GSAP + Three.js 3D robot hero).
- **#4** The video (lifecycle spine; script + storyboard by Clodi, production via external tool).

## 10. Assumptions & open items

- **Git:** this folder is not a git repository, so this spec is saved but not committed. Version history is optional — offer `git init` if Sandy wants it.
- **Imagery sourcing** (AI-generated vs. licensed stock) is decided per-figure during the build, under the §5 rule.
- **Quarto / Datawrapper / Typst** are assumed installable in Sandy's environment; verify availability at build start and flag if any is missing before relying on it.
- **Exact chapter count** may shift ±1–2; logged in `relay-log.md`.
- **Project scaffolding** (`README.md`, `framework.md`, `relay-log.md`, Quarto project files) is created at the start of implementation, not in this spec.
