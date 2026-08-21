"""Text-free vector reconstruction of the approved Figure 3 reference.

The canvas, panel splits, curves, arrows, and schematic object anchors are
defined in the reference image's native 1536 x 1024 coordinate system.
"""

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, PathPatch, Rectangle
from matplotlib.path import Path as MplPath
import numpy as np


W, H = 1536, 1024
OUT = Path(__file__).resolve().parent / "Figure3_FreeEnergyLandscape_vector_v02"

NAVY = "#071d5d"
BLUE = "#075fca"
BLUE_FILL = "#5f9fe0"
PALE_BLUE = "#e8f4f9"
GREEN = "#078224"
GREEN_FILL = "#63b477"
ORANGE = "#e78413"
ORANGE_FILL = "#e99b2d"
RED = "#f02e18"
CORAL = "#d96049"
CORAL_FILL = "#dc7a63"
GREY_BLUE = "#8eb9d6"

mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
    "font.size": 7,
    "svg.fonttype": "none",
    "pdf.fonttype": 42,
    "path.snap": False,
})


def line(ax, x1, y1, x2, y2, color=NAVY, lw=2.2, ls="-", z=2):
    ax.plot([x1, x2], [y1, y2], color=color, lw=lw, ls=ls,
            solid_capstyle="round", dash_capstyle="round", zorder=z)


def arrow(ax, start, end, color=NAVY, lw=2.3, scale=16, ls="-", rad=0.0, z=5):
    patch = FancyArrowPatch(
        start, end, arrowstyle="-|>", mutation_scale=scale,
        linewidth=lw, color=color, linestyle=ls,
        connectionstyle=f"arc3,rad={rad}", shrinkA=0, shrinkB=0,
        capstyle="round", joinstyle="round", zorder=z,
    )
    ax.add_patch(patch)
    return patch


def bezier(ax, verts, color=NAVY, lw=3.0, ls="-", z=3):
    codes = [MplPath.MOVETO]
    for i in range(1, len(verts)):
        codes.append(MplPath.CURVE4 if (i % 3) else MplPath.CURVE4)
    patch = PathPatch(MplPath(verts, codes), fill=False, color=color,
                      lw=lw, ls=ls, capstyle="round", joinstyle="round", zorder=z)
    ax.add_patch(patch)
    return patch


def particle(ax, x, y, kind="circle", color=BLUE_FILL, edge=NAVY,
             size=7, angle=0, z=5):
    if kind == "circle":
        ax.add_patch(Circle((x, y), size, facecolor=color, edgecolor=edge,
                            lw=1.25, zorder=z))
    elif kind == "square":
        ax.add_patch(Rectangle((x-size, y-size), 2*size, 2*size,
                               facecolor=color, edgecolor=edge, lw=1.25,
                               zorder=z))
    else:
        rect = Rectangle((x-1.6*size, y-0.48*size), 3.2*size, 0.96*size,
                         angle=angle, rotation_point="center", facecolor=color,
                         edgecolor=edge, lw=1.25, zorder=z)
        ax.add_patch(rect)


def dispersed(ax, cx, cy, scale=1.0, warm=False):
    pts = [(-42,-14,"circle",0),(-15,-30,"square",0),(25,-17,"circle",0),
           (53,-4,"square",0),(-10,9,"bar",0),(25,17,"circle",0),
           (-46,25,"bar",-28),(5,31,"circle",0),(51,33,"circle",0)]
    fills = [CORAL_FILL, "#a9a0b4", CORAL_FILL, CORAL_FILL,
             GREY_BLUE, CORAL_FILL, CORAL_FILL, GREY_BLUE, CORAL_FILL] if warm else [BLUE_FILL]*9
    edge = RED if warm else NAVY
    for (dx,dy,k,a), fc in zip(pts, fills):
        particle(ax, cx+dx*scale, cy+dy*scale, k, fc, edge,
                 size=6.2*scale, angle=a)


def activated_particles(ax, cx, cy, scale=1.0):
    pts = [(-20,-33,"bar",25),(20,-35,"bar",-28),(0,-7,"circle",0),
           (42,-4,"square",0),(-7,27,"circle",0)]
    for dx,dy,k,a in pts:
        particle(ax, cx+dx*scale, cy+dy*scale, k, BLUE_FILL, NAVY,
                 size=7*scale, angle=a)
    rays = [(-33,-42,-44,-53),(-9,-51,-10,-66),(13,-49,17,-65),
            (38,-38,50,-48),(53,-15,67,-17),(42,16,55,25),
            (10,38,13,54),(-17,40,-24,53),(-36,24,-49,34),
            (-43,-4,-58,-7)]
    for x1,y1,x2,y2 in rays:
        line(ax, cx+x1*scale, cy+y1*scale, cx+x2*scale, cy+y2*scale,
             BLUE, 1.8, z=3)


def network(ax, cx, cy, scale=1.0, color=BLUE, fill=BLUE_FILL,
            dense=True, seed=0, warm=False):
    rng = np.random.default_rng(seed)
    if dense:
        pts = np.array([
            [-55,-13],[-39,-43],[-13,-56],[13,-37],[39,-48],[59,-21],
            [46,7],[61,29],[25,25],[7,47],[-20,39],[-43,25],[-20,5],
            [8,-5],[30,-12],[-2,20],
        ], dtype=float)
        edges = [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9),
                 (9,10),(10,11),(11,0),(0,12),(12,2),(12,13),(13,3),
                 (13,14),(14,5),(14,8),(13,15),(15,8),(15,10),(12,15)]
    else:
        pts = np.array([[-46,-13],[-30,-37],[-1,-47],[23,-28],[49,-35],
                        [43,-3],[55,27],[17,31],[-9,47],[-37,27],[-18,3],
                        [13,1]], dtype=float)
        edges = [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9),
                 (9,0),(0,10),(10,2),(10,11),(11,3),(11,7),(7,8)]
    pts *= scale
    if warm:
        pts += rng.normal(0, 5*scale, pts.shape)
    for i,j in edges:
        line(ax, cx+pts[i,0], cy+pts[i,1], cx+pts[j,0], cy+pts[j,1],
             color, 2.0*scale, z=3)
    for i,(x,y) in enumerate(pts):
        fc = fill
        particle(ax, cx+x, cy+y, "circle", fc, NAVY if not warm else CORAL,
                 size=6.0*scale, z=5)
    # short dangling motifs match the reference network vocabulary
    arms = [(-55,-13,-74,-28),(-39,-43,-51,-65),(-13,-56,-13,-77),
            (39,-48,55,-68),(59,-21,78,-31),(61,29,78,42),
            (25,25,30,49),(-43,25,-60,42),(-20,39,-29,61)]
    for x1,y1,x2,y2 in arms:
        line(ax, cx+x1*scale, cy+y1*scale, cx+x2*scale, cy+y2*scale,
             color, 2.0*scale, z=3)
        line(ax, cx+(x2-4)*scale, cy+(y2-4)*scale,
             cx+(x2+4)*scale, cy+(y2+4)*scale, color, 1.6*scale, z=4)


def lattice(ax, x0, y0, dx=24, dy=24):
    for r in range(4):
        for c in range(5):
            if c < 4:
                line(ax, x0+c*dx, y0+r*dy, x0+(c+1)*dx, y0+r*dy, GREEN, 2.4)
            if r < 3:
                line(ax, x0+c*dx, y0+r*dy, x0+c*dx, y0+(r+1)*dy, GREEN, 2.4)
    for r in range(4):
        for c in range(5):
            particle(ax, x0+c*dx, y0+r*dy, "circle", GREEN_FILL, GREEN,
                     size=5.5)


def irregular_warm_network(ax, cx, cy, scale=1.0, seed=3, coral=False):
    color = CORAL if coral else ORANGE
    fill = CORAL_FILL if coral else ORANGE_FILL
    rng = np.random.default_rng(seed)
    theta = np.linspace(0, 2*np.pi, 15, endpoint=False)
    rad = rng.uniform(31, 58, 15)
    pts = np.c_[np.cos(theta)*rad, np.sin(theta)*rad*0.72] * scale
    pts += rng.normal(0, 7*scale, pts.shape)
    edges = [(i,(i+1)%15) for i in range(15)] + [(0,5),(2,7),(4,10),(6,12),(9,14)]
    for i,j in edges:
        line(ax, cx+pts[i,0], cy+pts[i,1], cx+pts[j,0], cy+pts[j,1],
             color, 1.8, z=3)
    for x,y in pts:
        particle(ax, cx+x, cy+y, "circle", fill, color, size=5.2)
    for i in (1,5,9,12):
        x,y = pts[i]
        line(ax, cx+x, cy+y, cx+x+rng.uniform(-22,22), cy+y+rng.uniform(12,28),
             color, 1.7, z=3)


def battery(ax):
    ax.add_patch(Rectangle((856,849), 143, 132, facecolor="#f1f9fb",
                           edgecolor=NAVY, lw=1.8, zorder=1))
    ax.add_patch(Rectangle((873,837), 121, 145, fill=False, edgecolor=NAVY,
                           lw=1.8, zorder=2))
    line(ax, 932, 854, 932, 973, "#96afba", 1.2, z=2)
    ax.add_patch(Rectangle((875,858), 19, 104, facecolor="#d9eef2",
                           edgecolor=NAVY, lw=1.2, zorder=2))
    ax.add_patch(Rectangle((974,858), 18, 104, facecolor="#f6d6cd",
                           edgecolor=NAVY, lw=1.2, zorder=2))
    for yy in [890,906,922,938,954]:
        line(ax, 899, yy, 905, yy-4, BLUE, 1.0)
        line(ax, 905, yy-4, 911, yy, BLUE, 1.0)
        line(ax, 957, yy, 963, yy+4, RED, 1.0)
        line(ax, 963, yy+4, 969, yy, RED, 1.0)
    network(ax, 936, 917, 0.48, dense=False, seed=2)


def draw_panel_a(ax):
    # Axes and free-energy landscape.
    arrow(ax, (50,757), (50,108), NAVY, 2.5, 18)
    arrow(ax, (50,757), (808,757), NAVY, 2.5, 18)
    verts = [
        (79,159),(117,188),(123,514),(188,595),
        (231,649),(269,566),(294,474),
        (321,374),(356,377),(374,431),
        (392,486),(455,513),(487,424),
        (519,335),(527,207),(563,217),
        (601,225),(608,456),(650,516),
        (687,560),(738,546),(754,444),
        (770,343),(780,282),(808,254),
    ]
    bezier(ax, verts, NAVY, 3.0)

    # Barrier indicators and relaxation arrow.
    line(ax, 351,311,401,311,NAVY,1.7,(0,(4,3)))
    line(ax, 377,311,377,412,NAVY,1.7,(0,(4,3)))
    arrow(ax,(377,319),(377,409),NAVY,1.6,13,ls=(0,(4,3)))
    line(ax, 636,188,694,188,NAVY,1.7,(0,(4,3)))
    line(ax, 665,188,665,531,NAVY,1.7,(0,(4,3)))
    arrow(ax,(665,196),(665,528),NAVY,1.6,13,ls=(0,(4,3)))
    arrow(ax,(339,516),(196,574),GREEN,1.9,14,ls=(0,(4,3)),rad=0.38)

    lattice(ax,147,621,23,23)
    irregular_warm_network(ax,429,596,0.88,seed=8,coral=False)
    irregular_warm_network(ax,685,619,1.02,seed=11,coral=True)


def draw_panel_b(ax):
    dispersed(ax, 924, 248, 0.90)
    activated_particles(ax, 1172, 143, 0.90)
    network(ax, 1380, 254, 1.02, dense=True, seed=4)
    dispersed(ax, 1080, 470, 0.88, warm=True)
    dispersed(ax, 1388, 495, 0.92)

    arrow(ax,(924,182),(1105,108),BLUE,2.8,18,rad=-0.38)
    arrow(ax,(1235,142),(1330,195),GREEN,2.6,17,rad=-0.15)
    arrow(ax,(1337,313),(1142,466),RED,2.8,18,rad=-0.36)
    arrow(ax,(964,282),(1060,410),RED,2.4,17,rad=-0.25)
    arrow(ax,(1015,504),(905,312),BLUE,2.5,18,rad=0.38)
    arrow(ax,(1386,346),(1386,444),BLUE,2.3,16,ls=(0,(4,3)))


def mini_state(ax, cx, cy, mode):
    if mode == "assembly":
        dispersed(ax,cx-62,cy,0.46)
        network(ax,cx+52,cy,0.48,dense=False,seed=1)
        arrow(ax,(cx-28,cy),(cx+5,cy),GREEN,2.0,14)
    elif mode == "steady":
        dispersed(ax,cx-67,cy,0.36)
        network(ax,cx,cy,0.50,dense=False,seed=2)
        particle(ax,cx+72,cy-15,"square",BLUE_FILL,NAVY,4.0)
        particle(ax,cx+76,cy+18,"circle",BLUE_FILL,NAVY,4.0)
        arrow(ax,(cx-44,cy),(cx-22,cy),GREEN,1.8,12)
        arrow(ax,(cx+49,cy+5),(cx+22,cy+5),RED,1.8,12)
    else:
        network(ax,cx-50,cy,0.46,dense=False,seed=3)
        dispersed(ax,cx+65,cy,0.46)
        arrow(ax,(cx-10,cy),(cx+22,cy),RED,2.0,14)


def draw_panel_c(ax):
    line(ax,1054,598,1054,790,"#9aa9b8",1.2,(0,(3,4)))
    line(ax,1290,598,1290,790,"#9aa9b8",1.2,(0,(3,4)))
    mini_state(ax,947,739,"assembly")
    mini_state(ax,1174,739,"steady")
    mini_state(ax,1402,739,"disassembly")
    line(ax,856,809,1520,809,NAVY,1.5)

    battery(ax)
    arrow(ax,(1035,919),(1136,919),BLUE,2.0,16,ls=(0,(4,3)))
    network(ax,1202,919,0.53,dense=False,seed=4)
    line(ax,1267,875,1267,986,"#9aa9b8",1.1,(0,(3,4)))
    network(ax,1334,927,0.48,dense=False,seed=5)
    line(ax,1403,875,1403,986,"#9aa9b8",1.1,(0,(3,4)))
    dispersed(ax,1462,925,0.54)
    arrow(ax,(1203,827),(1203,869),GREEN,2.0,14,ls=(0,(3,3)))
    arrow(ax,(1335,827),(1335,869),ORANGE,2.0,14,ls=(0,(3,3)))
    arrow(ax,(1459,827),(1459,869),RED,2.0,14,ls=(0,(3,3)))


def draw():
    fig = plt.figure(figsize=(W/150, H/150), dpi=150, facecolor="white")
    ax = fig.add_axes([0,0,1,1])
    ax.set_xlim(0,W)
    ax.set_ylim(H,0)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")

    # Reference panel geometry.
    line(ax,841,12,841,1012,NAVY,2.5)
    line(ax,841,562,1520,562,NAVY,2.5)
    draw_panel_a(ax)
    draw_panel_b(ax)
    draw_panel_c(ax)

    fig.savefig(OUT.with_suffix(".svg"), facecolor="white", bbox_inches=None,
                pad_inches=0)
    fig.savefig(OUT.with_suffix(".pdf"), facecolor="white", bbox_inches=None,
                pad_inches=0)
    fig.savefig(OUT.with_suffix(".png"), dpi=150, facecolor="white",
                bbox_inches=None, pad_inches=0)
    plt.close(fig)


if __name__ == "__main__":
    draw()
