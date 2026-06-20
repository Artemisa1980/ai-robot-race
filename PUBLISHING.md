# Publishing Workflow

How to update and (re)publish *The AI Robot Race and Its Hidden Cost*.
Keep this routine and you can publish confidently every time.

## TL;DR — the routine

```bash
# 1. edit content in report/ (.qmd, _quarto.yml, theme/)
# 2. render + preview locally
cd report && quarto render

# 3. save the source
git add -A && git commit -m "your message" && git push origin main

# 4. publish the live HTML site (re-renders + pushes to gh-pages)
cd report && quarto publish gh-pages --no-prompt

# 5. decide on Zenodo  →  see "The Zenodo rule" below
```

## The three destinations (they are independent)

| Destination | What it is | When to update |
|---|---|---|
| GitHub `main` | Source: `.qmd`, `theme/`, `README.md` | Every change → commit + push |
| GitHub Pages (`gh-pages`) | Live HTML book → <https://artemisa1980.github.io/ai-robot-race/> | `quarto publish gh-pages` |
| Zenodo DOI `10.5281/zenodo.20754384` | Frozen, **citable** PDF archive | ONLY for substantive new versions |

> The README and the live site live on GitHub and are **fully editable** anytime.
> They only *link* to Zenodo — editing them does **not** touch the frozen DOI record.

## The Zenodo rule (important)

Zenodo holds a frozen, citable snapshot (the deposited PDF). Decide by the *kind* of change:

- **Cosmetic / branding / typo / styling** → update **site + source only**.
  Do **NOT** mint a new Zenodo version. A new DOI for a footer or a typo is noise in the
  citation record and looks unserious.
- **Substantive** (data changed, a new chapter, a corrected figure or conclusion) → **upload a
  new version to Zenodo**. It mints a new *version DOI* under the same *concept DOI*, with a
  changelog. Then update the README badge/citation if needed.

## Brand signature

- The footer / colophon is the **wordmark `sanblueᵈᵒᵗ`** — not the logo graphic, no sprout, no tagline.
- **Display contexts** (colophon page, README) → stylized `sanblue<sup>dot</sup>` (`dot` in `#7CB3E8`).
- **Metadata / plain-text** (`_quarto.yml` `affiliation`, citations, YAML) → plain lowercase `sanbluedot`
  (no superscript — it breaks in non-HTML formats).

### Known limitation — PDF colophon
The colophon styling (blue `dot`, centering) lives in `theme/sanblue.scss`, which is **CSS → HTML only**.
In the **PDF** the colophon renders as plain left-aligned text (the `^dot^` superscript survives, the
color/centering do not), and it sits just before the bibliography. This is **accepted on purpose**: the
HTML is the primary artifact and the citable PDF is the Zenodo one. Fixing it would require Typst-native
styling — not worth the risk to a published, working book for a cosmetic detail.
