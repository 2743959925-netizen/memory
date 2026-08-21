"""Draw Figure 3 as an editable, text-free vector schematic.

The figure is conceptual and not to scale. All labels are intentionally omitted
so that manuscript typography can be added later in PowerPoint or Illustrator.
"""

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, PathPatch, Rectangle
from matplotlib.path import Path as MplPath


mpl.rcParams.update(
    {
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
        "svg.fonttype": "none",
        "pdf.fonttype": 42,
        "axes.linewidth": 0.8,
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
    }
)


OUT_DIR = Path(__file__).resolve().parent
BASE = OUT_DIR / "Figure3_FreeEnergyLandscape_vector_v01"

NAVY = "#15345B"
BLUE = "#2F6FAE"
BLUE_LIGHT = "#83AED2"
GREEN = "#2F7F4F"
GREEN_LIGHT = "#85B991"
AMBER = "#D89A35"
AMBER_LIGHT = "#E6C176"
CORAL = "#C9705A"
CORAL_LIGHT = "#E1A08E"
RED = "#D85C43"
GREY = "#AAB5BF"
PALE_BLUE = "#EAF3F8"


def clean_axis(ax, xlim=(0, 1), ylim=(0, 1)):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_facecolor("white")


def arrow(ax, start, end, color=NAVY, lw=1.5, style="-|>", ls="-", scale=11, z=5):
    patch = FancyArrowPatch(
        start,
        end,
        arrowstyle=style,
        mutation_scale=scale,
        linewidth=lw,
        linestyle=ls,
        color=color,
        shrinkA=0,
        shrinkB=0,
        connectionstyle="arc3",
        zorder=z,
    )
    ax.add_patch(patch)
    return patch


def curved_arrow(ax, start, end, rad, color, lw=1.7, ls="-", scale=11, z=5):
    patch = FancyArrowPatch(
        start,
        end,
        arrowstyle="-|>",
        mutation_scale=scale,
        linewidth=lw,
        linestyle=ls,
        color=color,
        shrinkA=0,
        shrinkB=0,
        connectionstyle=f"arc3,rad={rad}",
        zorder=z,
    )
    ax.add_patch(patch)
    return patch


def draw_nodes(ax, center, pattern, color, scale=1.0, ordered=False, z=4):
    """Draw a small abstract assembly without embedding chemical meaning."""
    cx, cy = center
    points = np.asarray(pattern, dtype=float) * scale + np.array([cx, cy])
    if ordered:
        distances = np.linalg.norm(points[:, None, :] - points[None, :, :], axis=2)
        links = np.argwhere((distances > 0) & (distances < 0.075 * scale / 0.06))
        for i, j in links:
            if i < j:
                ax.plot(
                    [points[i, 0], points[j, 0]],
                    [points[i, 1], points[j, 1]],
                    color=color,
                    lw=1.0,
                    alpha=0.9,
                    zorder=z,
                )
    for x, y in points:
        ax.add_patch(Circle((x, y), 0.0105 * scale / 0.06, facecolor=color, edgecolor=NAVY, lw=0.55, zorder=z + 1))


def lattice_icon(ax, origin, color=GREEN):
    ox, oy = origin
    dx, dy = 0.035, 0.038
    for i in range(4):
        for j in range(4):
            if i < 3:
                ax.plot([ox + i * dx, ox + (i + 1) * dx], [oy + j * dy] * 2, color=color, lw=1.0, zorder=3)
            if j < 3:
                ax.plot([ox + i * dx] * 2, [oy + j * dy, oy + (j + 1) * dy], color=color, lw=1.0, zorder=3)
            ax.add_patch(Circle((ox + i * dx, oy + j * dy), 0.007, facecolor=GREEN_LIGHT, edgecolor=color, lw=0.65, zorder=4))


def irregular_network(ax, center, color, seed=0, radius=(0.08, 0.065), n=15):
    rng = np.random.default_rng(seed)
    angles = rng.uniform(0, 2 * np.pi, n)
    radii = np.sqrt(rng.uniform(0.06, 1.0, n))
    pts = np.column_stack(
        [center[0] + radius[0] * radii * np.cos(angles), center[1] + radius[1] * radii * np.sin(angles)]
    )
    d = np.linalg.norm(pts[:, None, :] - pts[None, :, :], axis=2)
    for i in range(n):
        neighbors = np.argsort(d[i])[1:4]
        for j in neighbors:
            if i < j and d[i, j] < 0.075:
                ax.plot([pts[i, 0], pts[j, 0]], [pts[i, 1], pts[j, 1]], color=color, lw=0.8, alpha=0.9, zorder=2)
    for x, y in pts:
        ax.add_patch(Circle((x, y), 0.0065, facecolor=color, edgecolor=NAVY, lw=0.45, zorder=3))


def dispersed(ax, center, color=BLUE, scale=1.0, n=8, seed=1):
    rng = np.random.default_rng(seed)
    cx, cy = center
    for i in range(n):
        x = cx + rng.uniform(-0.065, 0.065) * scale
        y = cy + rng.uniform(-0.045, 0.045) * scale
        if i % 3 == 0:
            ax.add_patch(Rectangle((x - 0.007, y - 0.004), 0.014, 0.008, angle=20, facecolor=BLUE_LIGHT, edgecolor=NAVY, lw=0.55, zorder=4))
        else:
            ax.add_patch(Circle((x, y), 0.0065, facecolor=BLUE_LIGHT, edgecolor=NAVY, lw=0.55, zorder=4))


def transient_network(ax, center, color=BLUE):
    cx, cy = center
    pattern = np.array(
        [
            [-0.065, 0.02], [-0.04, 0.06], [-0.01, 0.03], [0.02, 0.065], [0.05, 0.025],
            [-0.05, -0.03], [-0.015, -0.015], [0.02, -0.035], [0.06, -0.025], [0.0, 0.005],
        ]
    )
    pts = pattern + np.array([cx, cy])
    links = [(0, 1), (0, 5), (1, 2), (2, 3), (2, 9), (3, 4), (4, 8), (5, 6), (6, 9), (6, 7), (7, 8), (7, 9)]
    for i, j in links:
        ax.plot([pts[i, 0], pts[j, 0]], [pts[i, 1], pts[j, 1]], color=color, lw=1.25, zorder=3)
    for x, y in pts:
        ax.add_patch(Circle((x, y), 0.007, facecolor=BLUE_LIGHT, edgecolor=NAVY, lw=0.6, zorder=4))


def energy_panel(ax):
    clean_axis(ax)

    # Axes without text.
    arrow(ax, (0.055, 0.105), (0.955, 0.105), color=NAVY, lw=1.3, scale=10)
    arrow(ax, (0.055, 0.105), (0.055, 0.94), color=NAVY, lw=1.3, scale=10)

    # Smooth qualitative energy landscape.
    xk = np.array([0.09, 0.18, 0.32, 0.48, 0.68, 0.84, 0.94])
    yk = np.array([0.86, 0.31, 0.62, 0.43, 0.82, 0.39, 0.72])
    # Cosine interpolation gives a smooth conceptual landscape without SciPy.
    xs_parts = []
    ys_parts = []
    for i in range(len(xk) - 1):
        t = np.linspace(0, 1, 90, endpoint=i == len(xk) - 2)
        eased = (1 - np.cos(np.pi * t)) / 2
        xs_parts.append(xk[i] + (xk[i + 1] - xk[i]) * t)
        ys_parts.append(yk[i] + (yk[i + 1] - yk[i]) * eased)
    xs = np.concatenate(xs_parts)
    ys = np.concatenate(ys_parts)
    ax.plot(xs, ys, color=NAVY, lw=1.7, solid_capstyle="round", zorder=2)

    # Barrier measures (unlabelled); spaces beside them are reserved for formulas.
    ax.plot([0.32, 0.32], [0.43, 0.62], color=NAVY, lw=0.95, ls=(0, (4, 3)), zorder=1)
    arrow(ax, (0.32, 0.61), (0.32, 0.44), color=NAVY, lw=0.95, scale=7)
    ax.plot([0.68, 0.68], [0.39, 0.82], color=NAVY, lw=0.95, ls=(0, (4, 3)), zorder=1)
    arrow(ax, (0.68, 0.81), (0.68, 0.40), color=NAVY, lw=0.95, scale=7)

    # Metastable relaxation path.
    curved_arrow(ax, (0.47, 0.45), (0.22, 0.30), rad=0.35, color=GREEN, lw=1.25, ls=(0, (4, 3)), scale=9)

    # State icons placed below their corresponding minima.
    lattice_icon(ax, (0.14, 0.17), color=GREEN)
    irregular_network(ax, (0.45, 0.20), AMBER, seed=12, radius=(0.075, 0.055), n=14)
    irregular_network(ax, (0.82, 0.20), CORAL, seed=9, radius=(0.075, 0.055), n=15)


def dissipative_panel(ax):
    clean_axis(ax)

    # Four states of a flux-maintained cycle.
    dispersed(ax, (0.15, 0.58), scale=1.0, seed=2)
    dispersed(ax, (0.49, 0.80), color=BLUE, scale=0.85, seed=4)
    transient_network(ax, (0.79, 0.61))
    dispersed(ax, (0.48, 0.28), color=GREY, scale=0.85, seed=7)

    # Activation, assembly, deactivation and replenishment.
    curved_arrow(ax, (0.19, 0.63), (0.42, 0.78), rad=-0.22, color=BLUE, lw=1.7, scale=11)
    curved_arrow(ax, (0.55, 0.79), (0.70, 0.66), rad=-0.12, color=GREEN, lw=1.7, scale=11)
    curved_arrow(ax, (0.76, 0.52), (0.57, 0.30), rad=-0.18, color=RED, lw=1.7, scale=11)
    curved_arrow(ax, (0.39, 0.28), (0.17, 0.51), rad=-0.20, color=BLUE, lw=1.45, scale=10)

    # Waste by-products at the end of deactivation.
    for dx, dy, fc in [(0.02, 0.01, CORAL_LIGHT), (0.052, -0.004, AMBER_LIGHT), (0.036, -0.03, CORAL_LIGHT)]:
        ax.add_patch(Circle((0.58 + dx, 0.27 + dy), 0.006, facecolor=fc, edgecolor=RED, lw=0.5, zorder=4))

    # Conditional loss of the transient structure after removing input.
    dispersed(ax, (0.82, 0.25), color=GREY, scale=0.75, seed=13)
    arrow(ax, (0.79, 0.49), (0.81, 0.32), color=BLUE, lw=1.25, ls=(0, (4, 3)), scale=9)


def miniature_growth(ax, left, mode):
    """Draw rate-balance icons without text."""
    x0, y0 = left
    if mode == "grow":
        dispersed(ax, (x0, y0), scale=0.5, seed=21)
        transient_network(ax, (x0 + 0.13, y0))
        arrow(ax, (x0 + 0.04, y0), (x0 + 0.08, y0), color=GREEN, lw=1.4, scale=9)
    elif mode == "steady":
        transient_network(ax, (x0 + 0.075, y0))
        ax.add_patch(Circle((x0 - 0.005, y0 + 0.015), 0.006, facecolor=BLUE_LIGHT, edgecolor=NAVY, lw=0.5))
        ax.add_patch(Circle((x0 + 0.16, y0 - 0.012), 0.006, facecolor=BLUE_LIGHT, edgecolor=NAVY, lw=0.5))
        arrow(ax, (x0 + 0.01, y0 + 0.015), (x0 + 0.035, y0 + 0.015), color=GREEN, lw=1.2, scale=8)
        arrow(ax, (x0 + 0.145, y0 - 0.012), (x0 + 0.12, y0 - 0.012), color=RED, lw=1.2, scale=8)
    else:
        transient_network(ax, (x0 + 0.03, y0))
        dispersed(ax, (x0 + 0.17, y0), scale=0.52, seed=27)
        arrow(ax, (x0 + 0.09, y0), (x0 + 0.13, y0), color=RED, lw=1.4, scale=9)


def battery_test(ax):
    # Generic cell frame, deliberately schematic and data-free.
    x0, y0, w, h = 0.04, 0.06, 0.18, 0.30
    ax.add_patch(Rectangle((x0, y0), w, h, facecolor=PALE_BLUE, edgecolor=NAVY, lw=0.9, zorder=1))
    ax.add_patch(Rectangle((x0 + 0.018, y0 + 0.02), 0.023, h - 0.04, facecolor="#C7D9E5", edgecolor=NAVY, lw=0.55))
    ax.add_patch(Rectangle((x0 + w - 0.041, y0 + 0.02), 0.023, h - 0.04, facecolor="#E7C1B6", edgecolor=NAVY, lw=0.55))
    transient_network(ax, (x0 + 0.09, y0 + 0.15))

    # Removal followed by three conditional outcomes.
    arrow(ax, (0.24, 0.21), (0.38, 0.21), color=BLUE, lw=1.25, ls=(0, (4, 3)), scale=9)
    centers = [0.51, 0.71, 0.90]
    transient_network(ax, (centers[0], 0.20))
    irregular_network(ax, (centers[1], 0.20), BLUE, seed=33, radius=(0.055, 0.045), n=10)
    dispersed(ax, (centers[2], 0.20), scale=0.55, seed=35)
    for x, c in zip(centers, [GREEN, AMBER, RED]):
        arrow(ax, (x, 0.39), (x, 0.31), color=c, lw=1.15, ls=(0, (3, 3)), scale=8)
    for x in [0.615, 0.805]:
        ax.plot([x, x], [0.08, 0.32], color=GREY, lw=0.75, ls=(0, (2, 3)))


def rate_panel(ax):
    clean_axis(ax)

    # Upper row: the three rate-balance regimes.
    miniature_growth(ax, (0.10, 0.74), "grow")
    miniature_growth(ax, (0.40, 0.74), "steady")
    miniature_growth(ax, (0.69, 0.74), "shrink")
    for x in [0.335, 0.665]:
        ax.plot([x, x], [0.57, 0.92], color=GREY, lw=0.75, ls=(0, (2, 3)))
    ax.plot([0.02, 0.98], [0.52, 0.52], color=NAVY, lw=0.8)

    battery_test(ax)


def build_figure():
    width_in = 183 / 25.4
    height_in = 112 / 25.4
    fig = plt.figure(figsize=(width_in, height_in))
    gs = fig.add_gridspec(
        2,
        2,
        width_ratios=[1.17, 1.0],
        height_ratios=[1.0, 0.88],
        left=0.025,
        right=0.99,
        top=0.985,
        bottom=0.03,
        wspace=0.025,
        hspace=0.035,
    )
    ax_a = fig.add_subplot(gs[:, 0])
    ax_b = fig.add_subplot(gs[0, 1])
    ax_c = fig.add_subplot(gs[1, 1])

    energy_panel(ax_a)
    dissipative_panel(ax_b)
    rate_panel(ax_c)

    # Panel dividers; no textual panel labels by user request.
    for ax in [ax_b, ax_c]:
        ax.plot([0, 0], [0, 1], color=NAVY, lw=1.0, clip_on=False)
    ax_c.plot([0, 1], [1, 1], color=NAVY, lw=1.0, clip_on=False)

    fig.savefig(BASE.with_suffix(".svg"), bbox_inches="tight", pad_inches=0.02)
    fig.savefig(BASE.with_suffix(".pdf"), bbox_inches="tight", pad_inches=0.02)
    fig.savefig(BASE.with_suffix(".png"), dpi=300, bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)


if __name__ == "__main__":
    build_figure()
