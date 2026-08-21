"""Draw a text-free vector Figure 4 on van der Waals interactions.

Scientific logic:
1) permanent-permanent dipoles (Keesom),
2) instantaneous-induced dipoles (London dispersion),
3) permanent-induced dipoles (Debye),
4) nonspecific attraction promotes contact, while faceting and evaporation /
   capillary confinement select orientational order.
"""

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, FancyBboxPatch, Polygon
import numpy as np


W, H = 1268, 760
OUT = Path(__file__).resolve().parent / "Figure4_VanDerWaals_draft_v03"

NAVY = "#102a5e"
BLUE = "#4d79cf"
BLUE_LIGHT = "#8eb4e7"
CYAN = "#2ab7ab"
CYAN_LIGHT = "#9bded7"
RED = "#d96b50"
RED_LIGHT = "#f0b19f"
GREEN = "#2b8a57"
ORANGE = "#e69a32"
GREY = "#8da0ad"
CARD_1 = "#e8f4f2"
CARD_2 = "#edf3fb"
CARD_3 = "#fff4e8"
FOOT = "#f7f9fa"

mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
    "font.size": 7,
    "svg.fonttype": "none",
    "pdf.fonttype": 42,
    "path.snap": False,
})


def arrow(ax, p0, p1, color=NAVY, lw=2.1, scale=15, rad=0.0, ls="-"):
    ax.add_patch(FancyArrowPatch(
        p0, p1, arrowstyle="-|>", mutation_scale=scale,
        linewidth=lw, color=color, linestyle=ls,
        connectionstyle=f"arc3,rad={rad}", shrinkA=0, shrinkB=0,
        capstyle="round", joinstyle="round", zorder=8,
    ))


def double_arrow(ax, p0, p1, color=NAVY, lw=1.4, scale=10, ls="-"):
    ax.add_patch(FancyArrowPatch(
        p0, p1, arrowstyle="<->", mutation_scale=scale,
        linewidth=lw, color=color, linestyle=ls,
        shrinkA=0, shrinkB=0, capstyle="round", joinstyle="round", zorder=8,
    ))


def label(ax, x, y, text, size=7.2, color=NAVY, weight="normal",
          ha="center", va="center", rotation=0, z=20):
    ax.text(x, y, text, fontsize=size, color=color, fontweight=weight,
            ha=ha, va=va, rotation=rotation, zorder=z)


def half_ellipse(ax, cx, cy, width, height, left, right, edge=NAVY, lw=1.5):
    t1 = np.linspace(np.pi/2, 3*np.pi/2, 80)
    left_pts = np.c_[cx + width/2*np.cos(t1), cy + height/2*np.sin(t1)]
    left_poly = np.vstack(([cx, cy-height/2], left_pts, [cx, cy+height/2]))
    ax.add_patch(Polygon(left_poly, closed=True, facecolor=left, edgecolor="none", zorder=3))
    t2 = np.linspace(-np.pi/2, np.pi/2, 80)
    right_pts = np.c_[cx + width/2*np.cos(t2), cy + height/2*np.sin(t2)]
    right_poly = np.vstack(([cx, cy-height/2], right_pts, [cx, cy+height/2]))
    ax.add_patch(Polygon(right_poly, closed=True, facecolor=right, edgecolor="none", zorder=3))
    ax.add_patch(Ellipse((cx,cy), width, height, fill=False, edgecolor=edge, lw=lw, zorder=5))


def permanent_dipole(ax, cx, cy, flip=False, scale=1.0):
    left, right = (RED_LIGHT, BLUE_LIGHT) if not flip else (BLUE_LIGHT, RED_LIGHT)
    half_ellipse(ax, cx, cy, 105*scale, 56*scale, left, right)
    signs = ((r"$\delta^{+}$", RED), (r"$\delta^{-}$", BLUE)) if not flip else \
            ((r"$\delta^{-}$", BLUE), (r"$\delta^{+}$", RED))
    label(ax, cx-40*scale, cy-40*scale, signs[0][0], 6.7, signs[0][1])
    label(ax, cx+40*scale, cy-40*scale, signs[1][0], 6.7, signs[1][1])


def nonpolar_cloud(ax, cx, cy, scale=1.0):
    ax.add_patch(Ellipse((cx,cy),105*scale,56*scale,facecolor="#7795da",
                         edgecolor=NAVY,lw=1.4,zorder=4))
    ax.add_patch(Ellipse((cx,cy),62*scale,38*scale,facecolor="#91abe4",
                         edgecolor="none",alpha=0.85,zorder=5))
    ax.add_patch(Circle((cx,cy),5.5*scale,facecolor="#f1ba55",
                        edgecolor=NAVY,lw=0.9,zorder=6))


def fluctuating_atom(ax, cx, cy, scale=1.0, phase=1):
    ax.add_patch(Circle((cx,cy),42*scale,facecolor=CYAN_LIGHT,
                        edgecolor=NAVY,lw=1.4,zorder=3))
    shift = 11*phase*scale
    ax.add_patch(Circle((cx+shift,cy),30*scale,facecolor=CYAN,
                        edgecolor="none",alpha=0.72,zorder=4))
    ax.add_patch(Circle((cx,cy),6*scale,facecolor="#f1ba55",
                        edgecolor=NAVY,lw=0.9,zorder=6))
    if phase > 0:
        label(ax,cx-26*scale,cy-42*scale,r"$\delta^{+}$",6.4,RED)
        label(ax,cx+26*scale,cy-42*scale,r"$\delta^{-}$",6.4,BLUE)
    else:
        label(ax,cx-26*scale,cy-42*scale,r"$\delta^{-}$",6.4,BLUE)
        label(ax,cx+26*scale,cy-42*scale,r"$\delta^{+}$",6.4,RED)


def contact_lines(ax, x0, x1, y, color="#9fb5ca"):
    for dy in (-10,0,10):
        ax.plot([x0,x1],[y+dy,y+dy],color=color,lw=1.6,
                ls=(0,(4,3)),solid_capstyle="round",zorder=2)


def card(ax, x, color):
    ax.add_patch(FancyBboxPatch((x,8),398,382,
        boxstyle="round,pad=0.0,rounding_size=52",facecolor=color,
        edgecolor="#d7e1e4",lw=1.2,zorder=0))


def draw_keesom(ax, x):
    # Two permanent dipoles approach and select the attractive antiparallel contact.
    permanent_dipole(ax,x+128,150,False,0.80)
    permanent_dipole(ax,x+274,150,True,0.80)
    arrow(ax,(x+201,192),(x+201,242),BLUE,2.4,17)
    permanent_dipole(ax,x+120,312,False,0.78)
    permanent_dipole(ax,x+282,312,False,0.78)
    contact_lines(ax,x+162,x+239,312)
    arrow(ax,(x+180,312),(x+220,312),GREEN,1.4,10)
    arrow(ax,(x+222,312),(x+182,312),GREEN,1.4,10)
    label(ax,x+20,31,"a",10.5,NAVY,"bold",ha="left")
    label(ax,x+201,39,"Keesom interaction",10.0,NAVY,"bold")
    label(ax,x+201,67,"permanent dipole–permanent dipole",7.2,NAVY)
    label(ax,x+201,99,"like poles face",6.7,GREY)
    label(ax,x+242,211,"rotational\nreorientation",6.6,BLUE,ha="left")
    label(ax,x+201,369,"opposite poles align at contact",7.0,GREEN,"bold")


def draw_london(ax, x):
    # A spontaneous fluctuation in one atom induces a correlated dipole in the other.
    nonpolar_cloud(ax,x+130,150,0.75)
    nonpolar_cloud(ax,x+270,150,0.75)
    arrow(ax,(x+201,192),(x+201,242),BLUE,2.4,17)
    fluctuating_atom(ax,x+124,312,0.78,phase=1)
    fluctuating_atom(ax,x+278,312,0.78,phase=1)
    contact_lines(ax,x+160,x+242,312)
    # A small asymmetric electron mark indicates the instantaneous fluctuation.
    ax.add_patch(Circle((x+140,289),5,facecolor=BLUE,edgecolor=NAVY,lw=0.7,zorder=7))
    label(ax,x+20,31,"b",10.5,NAVY,"bold",ha="left")
    label(ax,x+201,39,"London dispersion",10.0,NAVY,"bold")
    label(ax,x+201,67,"instantaneous dipole–induced dipole",7.2,NAVY)
    label(ax,x+201,102,"symmetric charge distribution",6.7,GREY)
    label(ax,x+242,211,"fluctuation\n+ induction",6.6,BLUE,ha="left")
    label(ax,x+124,369,"instantaneous dipole",6.7,NAVY)
    label(ax,x+278,369,"induced dipole",6.7,NAVY)


def draw_debye(ax, x):
    # A permanent dipole polarizes an initially nonpolar neighbour.
    permanent_dipole(ax,x+120,150,False,0.78)
    nonpolar_cloud(ax,x+282,150,0.78)
    arrow(ax,(x+201,192),(x+201,242),BLUE,2.4,17)
    permanent_dipole(ax,x+120,312,False,0.78)
    permanent_dipole(ax,x+282,312,False,0.78)
    contact_lines(ax,x+162,x+239,312)
    arrow(ax,(x+240,270),(x+250,292),ORANGE,1.5,10,rad=-0.15)
    label(ax,x+20,31,"c",10.5,NAVY,"bold",ha="left")
    label(ax,x+201,39,"Debye interaction",10.0,NAVY,"bold")
    label(ax,x+201,67,"permanent dipole–induced dipole",7.2,NAVY)
    label(ax,x+120,102,"permanent dipole",6.7,NAVY)
    label(ax,x+282,102,"polarizable nonpolar molecule",6.5,GREY)
    label(ax,x+242,211,"polarization",6.7,BLUE,ha="left")
    label(ax,x+278,265,"induction",6.5,ORANGE,ha="left")
    label(ax,x+201,369,"induced polarization stabilizes contact",6.8,ORANGE,"bold")


def hexagon(cx,cy,r,angle=0):
    t=np.deg2rad(np.arange(0,360,60)+angle)
    return np.c_[cx+r*np.cos(t),cy+r*np.sin(t)]


def sphere_cluster(ax,cx,cy):
    pts=[(-52,-17),(-20,-35),(14,-22),(49,-34),(-39,18),(-5,10),(31,17),(58,7),
         (-19,42),(20,43)]
    for dx,dy in pts:
        ax.add_patch(Circle((cx+dx,cy+dy),12,facecolor="#8bb7d6",
                            edgecolor=NAVY,lw=1.2,zorder=5))
    for i,(dx,dy) in enumerate(pts[:-1]):
        if i%2==0:
            ax.plot([cx+dx,cx+pts[i+1][0]],[cy+dy,cy+pts[i+1][1]],
                    color="#9db2c0",lw=1.1,zorder=2)


def dispersed_spheres(ax,cx,cy):
    for dx,dy in [(-48,-20),(-14,26),(18,-27),(52,16)]:
        ax.add_patch(Circle((cx+dx,cy+dy),12,facecolor="#8bb7d6",
                            edgecolor=NAVY,lw=1.2,zorder=5))


def faceted_order(ax,cx,cy):
    positions=[]
    for row in range(3):
        for col in range(5):
            positions.append((cx+(col-2)*42+(row%2)*21,cy+(row-1)*35))
    for x,y in positions:
        ax.add_patch(Polygon(hexagon(x,y,20,30),closed=True,
                             facecolor="#e7b35a",edgecolor=NAVY,lw=1.2,zorder=5))
        ax.plot([x-12,x+12],[y,y],color=ORANGE,lw=1.2,zorder=6)


def droplet(ax,x,y,s=1.0):
    pts=np.array([[x,y-13*s],[x-9*s,y+2*s],[x,y+12*s],[x+9*s,y+2*s]])
    ax.add_patch(Polygon(pts,closed=True,facecolor="#8fc9df",edgecolor=BLUE,
                         lw=1.0,zorder=5))


def draw_distance_panel(ax):
    ax.add_patch(FancyBboxPatch((5,407),295,345,
        boxstyle="round,pad=0.0,rounding_size=28",facecolor=FOOT,
        edgecolor="#d7e1e4",lw=1.2,zorder=0))
    arrow(ax,(45,700),(45,445),NAVY,1.8,13)
    arrow(ax,(45,700),(270,700),NAVY,1.8,13)
    ax.plot([45,270],[585,585],color="#b8c5cf",lw=1.1,
            ls=(0,(4,4)),zorder=1)
    # Qualitative Lennard-Jones-like potential: steep short-range repulsion,
    # an attractive minimum, then decay toward zero at larger separation.
    r=np.linspace(0.88,3.0,360)
    u=4*((1/r)**12-(1/r)**6)
    u=np.clip(u,-1.15,2.2)
    x=78+(r-0.88)/(3.0-0.88)*178
    y=585-u*78
    ax.plot(x,y,color=NAVY,lw=2.5,solid_capstyle="round",zorder=4)
    ax.plot([99,99],[585,675],color=BLUE,lw=1.3,ls=(0,(3,3)),zorder=2)
    double_arrow(ax,(111,585),(111,665),BLUE,1.3,9)
    label(ax,18,429,"d",10.5,NAVY,"bold",ha="left")
    label(ax,145,429,"Short-range\ndistance dependence",6.2,NAVY,"bold",
          ha="left",va="top")
    label(ax,22,575,r"Interaction potential, $U(r)$",7.0,NAVY,
          rotation=90)
    label(ax,165,721,r"Separation, $r$",7.0,NAVY)
    label(ax,101,475,"steep repulsion",6.7,RED,ha="left")
    label(ax,115,651,"attractive well",6.7,BLUE,ha="left")
    label(ax,225,568,r"$U(r)\rightarrow 0$",6.7,GREY)
    label(ax,99,691,r"$r_0$",6.7,BLUE)
    label(ax,272,741,"conceptual—not to scale",5.5,GREY,ha="right")


def draw_geometry_strip(ax):
    ax.add_patch(FancyBboxPatch((315,407),948,345,
        boxstyle="round,pad=0.0,rounding_size=28",facecolor=FOOT,
        edgecolor="#d7e1e4",lw=1.2,zorder=0))
    ax.plot([340,1238],[579,579],color="#c4cfd6",lw=1.1,
            ls=(0,(4,4)),zorder=1)
    # Parallel comparison, not a particle-shape transformation.
    dispersed_spheres(ax,455,512)
    arrow(ax,(522,512),(610,512),GREY,2.0,15)
    sphere_cluster(ax,745,512)

    # Faceted building blocks constrain contact orientations; evaporation and
    # capillary confinement cooperate with short-range attraction.
    for x,y,a in [(406,644,8),(456,684,-11),(511,642,16),(551,694,3)]:
        ax.add_patch(Polygon(hexagon(x,y,27,30+a),closed=True,
                             facecolor="#e7b35a",edgecolor=NAVY,lw=1.25,zorder=5))
    arrow(ax,(590,666),(665,666),GREY,2.0,15)
    droplet(ax,710,692,0.85); droplet(ax,750,653,0.72); droplet(ax,790,692,0.58)
    arrow(ax,(710,642),(710,608),BLUE,1.5,11,rad=-0.10)
    arrow(ax,(750,625),(755,595),BLUE,1.5,11,rad=0.10)
    arrow(ax,(790,646),(801,616),BLUE,1.5,11,rad=0.12)
    arrow(ax,(830,666),(915,666),GREY,2.0,15)
    faceted_order(ax,1080,666)
    label(ax,335,431,"e",10.5,NAVY,"bold",ha="left")
    label(ax,789,431,"Attraction promotes contact; geometry and process select order",
          8.5,NAVY,"bold")
    label(ax,455,465,"spherical particles",6.8,NAVY)
    label(ax,566,488,"nonspecific\nvdW attraction",6.5,GREY)
    label(ax,865,530,"nondirectional\naggregation",6.8,NAVY,"bold",ha="left")
    label(ax,505,607,"faceted ZIF-8 particles",6.8,NAVY)
    label(ax,750,604,"evaporation +\ncapillary confinement",6.6,BLUE,"bold")
    label(ax,1080,607,"orientational + positional order",6.8,GREEN,"bold")


def draw():
    fig=plt.figure(figsize=(183/25.4,109.7/25.4),dpi=300,facecolor="white")
    ax=fig.add_axes([0,0,1,1])
    ax.set_xlim(0,W); ax.set_ylim(H,0); ax.set_aspect("equal"); ax.axis("off")
    card(ax,3,CARD_1); card(ax,435,CARD_2); card(ax,867,CARD_3)
    draw_keesom(ax,3); draw_london(ax,435); draw_debye(ax,867)
    draw_distance_panel(ax)
    draw_geometry_strip(ax)
    fig.set_size_inches(2560/300,1535/300,forward=True)
    fig.savefig(OUT.with_suffix(".png"),dpi=300,facecolor="white",bbox_inches=None,pad_inches=0)
    plt.close(fig)


if __name__=="__main__":
    draw()
