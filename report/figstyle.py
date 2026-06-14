"""SanBlueDot chart identity — shared by every figure in the book.

One source of truth for palette and matplotlib styling so all 10 chapters
look like one publication. Import from any chapter code cell:

    import figstyle as fs
    fs.apply()
    fig, ax = fs.new(height=2.6)
    ...
    fs.source(ax, "BloombergNEF (2024)")

Charts are rendered by Quarto (jupyter engine) into both HTML and PDF.
Text is emitted as SVG paths (svg.fonttype='path'), so figures are
portable and crisp regardless of which fonts a reader's machine has.
"""

import matplotlib as mpl
import matplotlib.pyplot as plt

# --- Brand palette (mirrors report/theme/sanblue.scss) -----------------
SANBLUE = "#1f4e8c"   # primary deep blue — default series
DARK = "#14223f"      # headings / titles / text
ACCENT = "#e8a13a"    # amber — the figure's "story" highlight
GRAY = "#8a94a6"      # muted series / reference lines
GRID = "#e4e9f0"      # faint gridlines
PANEL = "#f6f8fb"     # light panel fill (matches $gray-100)
TEXT = "#1b1f24"      # body text

# Ordered cycle for multi-series charts (story-first).
CYCLE = [SANBLUE, ACCENT, DARK, GRAY]


def apply():
    """Set global rcParams to the SanBlueDot identity. Call once per cell."""
    mpl.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Inter", "Helvetica Neue", "Arial", "DejaVu Sans"],
        "svg.fonttype": "path",          # embed text as paths -> portable PDF/HTML
        "figure.dpi": 140,
        "savefig.bbox": "tight",
        "text.color": TEXT,
        "axes.edgecolor": GRAY,
        "axes.labelcolor": DARK,
        "axes.titlecolor": DARK,
        "axes.titlesize": 13,
        "axes.titleweight": "bold",
        "axes.labelsize": 10,
        "axes.grid": False,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "xtick.color": DARK,
        "ytick.color": DARK,
        "xtick.labelsize": 9.5,
        "ytick.labelsize": 10,
        "axes.prop_cycle": mpl.cycler(color=CYCLE),
        "figure.facecolor": "white",
        "axes.facecolor": "white",
    })


def new(width=6.4, height=3.0):
    """A correctly proportioned figure+axes for a single-column chart."""
    fig, ax = plt.subplots(figsize=(width, height))
    return fig, ax


def title(ax, title, subtitle=None):
    """Magazine-style left-aligned title (+ optional subtitle) above the plot."""
    ax.set_title(title, loc="left", pad=22 if subtitle else 10)
    if subtitle:
        ax.text(0.0, 1.045, subtitle, transform=ax.transAxes,
                fontsize=10, color=GRAY, ha="left", va="bottom")


def source(ax, text):
    """Small source attribution beneath the axes (data-journalism convention)."""
    ax.annotate(f"Source: {text}", xy=(0, 0), xytext=(0, -32),
                xycoords="axes fraction", textcoords="offset points",
                fontsize=8, color=GRAY, ha="left", va="top")
