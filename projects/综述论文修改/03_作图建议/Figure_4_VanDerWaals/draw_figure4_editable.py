"""Draw an editable Nature-style schematic of van der Waals forces.

Every label is emitted as SVG text (``svg.fonttype = 'none'``), and every
diagram element is a native vector artist. No raster image is embedded.
"""

from __future__ import annotations

from pathlib import Path
import re

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle, Ellipse, FancyArrowPatch, PathPatch, Polygon
from matplotlib.path import Path as MplPath


HERE = Path(__file__).resolve().parent
OUT = HERE / "Figure4_VanDerWaals_principle_v06_editable"

W, H = 1672, 941
NAVY = "#10254f"
TEAL = "#0d7776"
ORANGE = "#d94f19"
BLUE = "#4e86aa"
BLUE_LIGHT = "#b8d0df"
RED = "#e78972"
RED_LIGHT = "#f5c9bd"
GREY = "#70777f"
LIGHT = "#e8ecef"
BLACK = "#111111"

mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
    "font.size": 7,
    "svg.fonttype": "none",
    "pdf.fonttype": 42,
    "axes.linewidth": 0.8,
    "legend.frameon": False,
})


def txt(ax, x, y, text, size=22, color=BLACK, weight="normal", ha="center",
        va="center", rotation=0, style="normal", zorder=30):
    # Layout coordinates are pixel-like while matplotlib font sizes are points.
    # At the 160 dpi design canvas, 0.5 keeps the requested visual pixel size.
    ax.text(x, y, text, fontsize=size * 0.5, color=color, fontweight=weight,
            ha=ha, va=va, rotation=rotation, fontstyle=style, zorder=zorder)


def arrow(ax, p0, p1, color=NAVY, lw=2.0, ms=13, style="-|>", zorder=20):
    ax.add_patch(FancyArrowPatch(
        p0, p1, arrowstyle=style, mutation_scale=ms, linewidth=lw,
        color=color, shrinkA=0, shrinkB=0, capstyle="round",
        joinstyle="round", zorder=zorder,
    ))


def dash(ax, p0, p1, color=NAVY, lw=1.5, pattern=(2.5, 3.5), zorder=6):
    ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=color, lw=lw,
            dashes=pattern, solid_capstyle="round", zorder=zorder)


def ellipse_gradient(ax, cx, cy, width, height, left_color=BLUE, right_color=RED,
                     edge="#8d949b", layers=18, asymmetry=0.0):
    """Layered vector ellipses approximate a soft electron-density gradient."""
    from matplotlib.colors import to_rgb

    left = np.array(to_rgb(left_color))
    right = np.array(to_rgb(right_color))
    white = np.ones(3)
    for i in range(layers, 0, -1):
        frac = i / layers
        shift = asymmetry * (1.0 - frac) * width * 0.22
        if i > layers * 0.52:
            mix = (i - layers * 0.52) / (layers * 0.48)
            color = left * mix + white * (1 - mix)
            x = cx - width * 0.13 * mix + shift
        else:
            mix = 1 - i / (layers * 0.52)
            color = white * (1 - mix) + right * mix
            x = cx + width * 0.13 * mix + shift
        ax.add_patch(Ellipse((x, cy), width * frac, height * frac,
                             facecolor=color, edgecolor="none", zorder=2))
    ax.add_patch(Ellipse((cx + asymmetry * width * 0.05, cy), width, height,
                         fill=False, edgecolor=edge, lw=1.2, zorder=4))


def dipole(ax, cx, cy, width=155, height=88, reverse=False, transient=False):
    lc, rc = (RED, BLUE) if reverse else (BLUE, RED)
    asym = 0.28 if transient else 0.0
    ellipse_gradient(ax, cx, cy, width, height, lc, rc, asymmetry=asym)
    ax.add_patch(Circle((cx, cy), 4.3, facecolor=BLACK, edgecolor="none", zorder=8))
    direction = -1 if reverse else 1
    arrow(ax, (cx - 22 * direction, cy), (cx + 48 * direction, cy),
          color=BLACK, lw=1.7, ms=11)
    # Keep charge labels within each independent ellipse so editing or moving a
    # molecule never creates collisions in the intermolecular gap.
    txt(ax, cx - width * 0.37, cy, "δ−" if not reverse else "δ+", 16)
    txt(ax, cx + width * 0.37, cy, "δ+" if not reverse else "δ−", 16)


def induced_cloud(ax, cx, cy, width=144, height=84):
    for i, color in enumerate(("#f8f8f8", "#eceeef", "#d9dde0")):
        pad = i * 5
        ax.add_patch(Ellipse((cx, cy), width - pad, height - pad,
                             facecolor=color if i == 0 else "none",
                             edgecolor="#8b9197", lw=1.2,
                             linestyle=(0, (4, 4)) if i == 2 else "solid",
                             zorder=3 + i))
    ax.add_patch(Circle((cx, cy), 4.3, facecolor=BLACK, edgecolor="none", zorder=8))
    txt(ax, cx - width * 0.35, cy, "δ−", 17)
    txt(ax, cx + width * 0.35, cy, "δ+", 17)


def heading(ax, x, text):
    txt(ax, x, 100, text, 28, NAVY, "bold")


def draw_origins(ax):
    heading(ax, 275, "Physical origins")
    rows = [215, 425, 635]
    specs = [
        ("Keesom interaction", "permanent dipole–permanent dipole"),
        ("Debye interaction", "permanent dipole–induced dipole"),
        ("London dispersion", "instantaneous dipole–induced dipole"),
    ]
    for y, (title, subtitle) in zip(rows, specs):
        txt(ax, 275, y - 72, title, 22, NAVY, "bold")
        txt(ax, 275, y - 42, subtitle, 17, BLACK)

    dipole(ax, 145, rows[0], reverse=False)
    # Head-to-tail alignment: opposite partial charges face one another.
    dipole(ax, 400, rows[0], reverse=False)
    dash(ax, (227, rows[0]), (318, rows[0]), GREY, 1.2)

    dipole(ax, 145, rows[1], reverse=False)
    induced_cloud(ax, 400, rows[1])
    dash(ax, (227, rows[1]), (323, rows[1]), GREY, 1.2)
    txt(ax, 145, rows[1] + 65, "permanent dipole", 15)
    txt(ax, 400, rows[1] + 65, "induced dipole", 15)

    dipole(ax, 158, rows[2], transient=True)
    induced_cloud(ax, 400, rows[2])
    dash(ax, (244, rows[2]), (323, rows[2]), GREY, 1.2)
    txt(ax, 158, rows[2] + 65, "instantaneous dipole\n(transient)", 15)
    txt(ax, 400, rows[2] + 65, "induced dipole", 15)


def atom_cloud(ax, cx, cy):
    for r, alpha in [(58, .06), (48, .08), (38, .10), (27, .14)]:
        ax.add_patch(Circle((cx, cy), r, facecolor=NAVY, edgecolor="none",
                            alpha=alpha, zorder=2))
    ax.add_patch(Circle((cx, cy), 8, facecolor="#b8bbc0", edgecolor=NAVY,
                        lw=1.2, zorder=5))
    for angle in (30, 145, 245, 330):
        dx = 68 * np.cos(np.deg2rad(angle))
        dy = 68 * np.sin(np.deg2rad(angle))
        ax.add_patch(Arc((cx + dx * .85, cy + dy * .85), 20, 32,
                         angle=angle, theta1=30, theta2=140,
                         color=GREY, lw=1.0, zorder=3))


def draw_principle(ax):
    heading(ax, 860, "Interaction principle")
    atom_cloud(ax, 735, 210)
    atom_cloud(ax, 985, 210)
    ax.plot([720, 720], [120, 151], color=BLACK, lw=1.2)
    ax.plot([1000, 1000], [120, 151], color=BLACK, lw=1.2)
    arrow(ax, (720, 135), (1000, 135), BLACK, 1.1, 10, "<->")
    txt(ax, 860, 133, "r", 18, BLACK, style="italic")
    dash(ax, (815, 210), (905, 210), NAVY, 1.3)
    arrow(ax, (795, 210), (855, 210), NAVY, 2.4, 14)
    arrow(ax, (925, 210), (865, 210), NAVY, 2.4, 14)
    txt(ax, 810, 244, "FvdW", 18, NAVY, style="italic")
    txt(ax, 910, 244, "FvdW", 18, NAVY, style="italic")

    x0, y0 = 670, 565
    arrow(ax, (x0, 720), (x0, 335), BLACK, 1.5, 12)
    arrow(ax, (x0, y0), (1125, y0), BLACK, 1.5, 12)
    txt(ax, 647, 470, "Interaction\npotential, U(r)", 17, BLACK, ha="right")
    txt(ax, 1107, y0 + 32, "Separation, r", 17, BLACK, ha="right")
    txt(ax, 652, y0, "0", 15, BLACK, ha="right")

    x = np.linspace(0.89, 3.35, 500)
    u = 4 * ((1 / x) ** 12 - (1 / x) ** 6)
    u = np.clip(u, -1.05, 2.2)
    px = 695 + (x - x.min()) / (x.max() - x.min()) * 395
    py = y0 - u * 120
    ax.plot(px, py, color=NAVY, lw=2.5, solid_capstyle="round", zorder=10)
    r_min_x = px[np.argmin(u)]
    r_min_y = py[np.argmin(u)]
    ax.plot([r_min_x, r_min_x], [y0, r_min_y], color=GREY, lw=1.1,
            dashes=(4, 4))
    txt(ax, r_min_x - 4, y0 - 31, "r", 18, BLACK, style="italic")
    txt(ax, r_min_x + 5, y0 - 24, "0", 12, BLACK)
    txt(ax, 775, 430, "short-range\nrepulsion", 17, BLACK)
    txt(ax, r_min_x + 35, r_min_y + 42, "attractive well", 17, BLACK)
    txt(ax, 995, 645, "rapid decay\nwith distance", 17, BLACK)
    txt(ax, 860, 780,
        "Attraction stabilizes close contact; excessive overlap causes repulsion",
        16, BLACK)


def globe(ax, cx, cy):
    ax.add_patch(Circle((cx, cy), 34, fill=False, edgecolor=TEAL, lw=2))
    ax.add_patch(Ellipse((cx, cy), 30, 68, fill=False, edgecolor=TEAL, lw=1.5))
    for off in (-18, 0, 18):
        ax.plot([cx - 31, cx + 31], [cy + off, cy + off], color=TEAL, lw=1.3)
    ax.plot([cx, cx], [cy - 34, cy + 34], color=TEAL, lw=1.3)


def circular_check(ax, cx, cy):
    ax.add_patch(Arc((cx, cy), 62, 62, theta1=25, theta2=165, color=TEAL, lw=2))
    ax.add_patch(Arc((cx, cy), 62, 62, theta1=205, theta2=345, color=TEAL, lw=2))
    arrow(ax, (cx + 22, cy - 21), (cx + 31, cy - 3), TEAL, 1.7, 9)
    arrow(ax, (cx - 22, cy + 21), (cx - 31, cy + 3), TEAL, 1.7, 9)
    ax.plot([cx - 12, cx - 2, cx + 18], [cy + 2, cy + 13, cy - 16],
            color=TEAL, lw=3, solid_capstyle="round")


def dots(ax, cx, cy, color=TEAL):
    for j in range(3):
        for i in range(4):
            ax.add_patch(Circle((cx + i * 19, cy + j * 19), 4.6,
                                facecolor=color, edgecolor="none"))


def interface_icon(ax, cx, cy):
    xs = np.linspace(-28, 28, 70)
    ys = 6 * np.sin(xs / 10)
    ax.plot(cx + xs, cy + ys, color=TEAL, lw=2)
    for dx in (-24, -8, 8, 24):
        ax.add_patch(Circle((cx + dx, cy - 22), 4.3, facecolor=TEAL,
                            edgecolor="none"))
    dash(ax, (cx - 30, cy + 23), (cx + 30, cy + 23), TEAL, 1.2)


def gauge(ax, cx, cy):
    ax.add_patch(Arc((cx, cy + 12), 62, 62, theta1=180, theta2=360,
                     color=ORANGE, lw=2))
    for angle in np.linspace(180, 360, 7):
        x1 = cx + 25 * np.cos(np.deg2rad(angle))
        y1 = cy + 12 + 25 * np.sin(np.deg2rad(angle))
        x2 = cx + 31 * np.cos(np.deg2rad(angle))
        y2 = cy + 12 + 31 * np.sin(np.deg2rad(angle))
        ax.plot([x1, x2], [y1, y2], color=ORANGE, lw=1.2)
    arrow(ax, (cx, cy + 12), (cx + 20, cy - 10), ORANGE, 1.8, 8)
    ax.add_patch(Circle((cx, cy + 12), 3.5, facecolor="white",
                        edgecolor=ORANGE, lw=1.5))


def short_range(ax, cx, cy):
    ax.plot([cx - 31, cx - 31], [cy - 28, cy + 28], color=ORANGE, lw=2)
    ax.plot([cx + 31, cx + 31], [cy - 28, cy + 28], color=ORANGE, lw=2)
    arrow(ax, (cx - 25, cy), (cx + 25, cy), ORANGE, 1.8, 10, "<->")


def nondirectional(ax, cx, cy):
    ax.add_patch(Circle((cx, cy), 33, fill=False, edgecolor=ORANGE, lw=1.8))
    for angle in (0, 90, 180, 270):
        end = (cx + 24 * np.cos(np.deg2rad(angle)),
               cy + 24 * np.sin(np.deg2rad(angle)))
        arrow(ax, (cx, cy), end, ORANGE, 1.5, 8)


def flask(ax, cx, cy):
    verts = [(cx - 7, cy - 35), (cx + 7, cy - 35), (cx + 7, cy - 8),
             (cx + 25, cy + 28), (cx + 25, cy + 36), (cx - 25, cy + 36),
             (cx - 25, cy + 28), (cx - 7, cy - 8), (cx - 7, cy - 35)]
    codes = [MplPath.MOVETO] + [MplPath.LINETO] * 7 + [MplPath.CLOSEPOLY]
    ax.add_patch(PathPatch(MplPath(verts, codes), fill=False, edgecolor=ORANGE,
                           lw=1.8))
    ax.add_patch(Polygon([(cx - 19, cy + 17), (cx + 19, cy + 17),
                          (cx + 23, cy + 31), (cx - 23, cy + 31)],
                         closed=True, facecolor=ORANGE, edgecolor="none"))
    for dx, dy in ((42, 18), (52, 18), (62, 18), (42, 28), (52, 28), (62, 28)):
        ax.add_patch(Circle((cx + dx, cy + dy), 3.1, facecolor=ORANGE,
                            edgecolor="none"))


def draw_strengths_limitations(ax):
    heading(ax, 1405, "Strengths and limitations")
    cx = 1405
    # balance motif
    ax.plot([cx, cx], [145, 292], color=NAVY, lw=3)
    ax.add_patch(Circle((cx, 145), 10, facecolor="white", edgecolor=NAVY, lw=3))
    ax.plot([cx - 145, cx + 145], [145, 145], color=NAVY, lw=2.3)
    for side in (-1, 1):
        topx = cx + side * 145
        ax.plot([topx, topx - 44 * side], [145, 215], color=BLACK, lw=1.2)
        ax.plot([topx, topx + 44 * side], [145, 215], color=BLACK, lw=1.2)
        ax.add_patch(Arc((topx, 210), 88, 40, theta1=0, theta2=180,
                         color=NAVY, lw=2.3))
    ax.plot([cx, cx], [300, 745], color="#a8aeb3", lw=1.2, dashes=(2, 5))
    txt(ax, 1285, 303, "Strengths", 24, TEAL, "bold")
    txt(ax, 1530, 303, "Limitations", 24, ORANGE, "bold")

    ys = [390, 505, 620, 735]
    icons_left = (globe, circular_check, dots, interface_icon)
    labels_left = ("ubiquitous", "spontaneous", "additive across\nmany contacts",
                   "stabilizes\ninterfaces")
    icons_right = (gauge, short_range, nondirectional, flask)
    labels_right = ("weak per\ninteraction", "short-ranged", "non-directional",
                    "sensitive to\nmedium and\nsurface chemistry")
    for y, icon, label in zip(ys, icons_left, labels_left):
        icon(ax, 1235, y)
        txt(ax, 1285, y, label, 15, BLACK, ha="left")
    for y, icon, label in zip(ys, icons_right, labels_right):
        icon(ax, 1465, y)
        txt(ax, 1518, y, label, 15, BLACK, ha="left")


def draw():
    fig = plt.figure(figsize=(W / 160, H / 160), dpi=300, facecolor="white")
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(H, 0)
    ax.set_aspect("equal")
    ax.axis("off")

    txt(ax, W / 2, 42,
        "Van der Waals forces: physical origin, interaction principle, strengths and limitations",
        31, NAVY, "bold")
    draw_origins(ax)
    draw_principle(ax)
    draw_strengths_limitations(ax)
    ax.plot([65, W - 65], [842, 842], color=NAVY, lw=1.5)
    txt(ax, W / 2, 885,
        "Ubiquitous and additive, but weak, short-ranged and non-directional",
        25, NAVY, "bold")

    fig.savefig(OUT.with_suffix(".svg"), format="svg", facecolor="white",
                bbox_inches=None, pad_inches=0)
    fig.savefig(OUT.with_suffix(".pdf"), format="pdf", facecolor="white",
                bbox_inches=None, pad_inches=0)
    fig.savefig(OUT.with_suffix(".png"), format="png", dpi=300,
                facecolor="white", bbox_inches=None, pad_inches=0)
    fig.savefig(OUT.with_suffix(".tiff"), format="tiff", dpi=600,
                facecolor="white", bbox_inches=None, pad_inches=0)
    plt.close(fig)

    # Matplotlib writes physical pt dimensions. Replace only the root size with
    # explicit 2K pixel dimensions while preserving its internal viewBox; this
    # improves browser/Illustrator/Inkscape interoperability.
    svg_path = OUT.with_suffix(".svg")
    raw = svg_path.read_text(encoding="utf-8")
    raw = re.sub(
        r'width="[^"]+" height="[^"]+" viewBox="([^"]+)"',
        rf'width="2560" height="1441" viewBox="\1"',
        raw,
        count=1,
    )
    svg_path.write_text(raw, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    draw()
