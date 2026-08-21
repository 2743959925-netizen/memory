"""Create a text-free vector Figure 4 while preserving the original layout.

The three-card geometry is traced from the manuscript figure. Text is removed.
The Debye card is then overlaid with a correct permanent-dipole / nonpolar-cloud
to induced-dipole schematic; Keesom and London pictograms remain as referenced.
"""

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.path import Path as MplPath
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, PathPatch, Polygon
import numpy as np
from PIL import Image


HERE = Path(__file__).resolve().parent
REF = HERE / "Figure4_reference_original.jpeg"
OUT = HERE / "Figure4_VanDerWaals_vector_v02"
W, H = 1268, 579

NAVY="#102a5e"; BLUE="#4d79cf"; BLUE_LIGHT="#8eb4e7"
RED_LIGHT="#f0b19f"; YELLOW="#f1ba55"; CARD_3="#fff4e8"

mpl.rcParams.update({
    "font.family":"sans-serif",
    "font.sans-serif":["Arial","Helvetica","DejaVu Sans","sans-serif"],
    "font.size":7,"svg.fonttype":"none","pdf.fonttype":42,
})

# Precise text-only masks in the reference's 1268 x 579 pixel space.
TEXT_BOXES=[
    (105,29,315,61),(54,72,352,102),(128,213,317,250),(31,509,397,548),
    (481,28,783,62),(482,72,794,101),(463,214,811,247),
    (438,470,614,500),(670,470,814,500),(425,508,831,546),
    (976,28,1164,61),(904,72,1252,101),(892,214,1027,258),
    (1112,214,1256,258),(1016,272,1121,304),(887,509,1258,546),
    # charge symbols and A/B letters are also omitted by user request
    (75,112,347,199),(18,365,393,455),(869,112,1264,205),(866,365,1268,463),
]


def erase_text(rgb):
    out=rgb.copy()
    for x0,y0,x1,y1 in TEXT_BOXES:
        out[y0:y1,x0:x1]=255
    return out


def groups(rgb):
    image=Image.fromarray(rgb).quantize(colors=48,method=Image.Quantize.MEDIANCUT,
                                        dither=Image.Dither.NONE)
    labels=np.asarray(image)
    palette=np.asarray(image.getpalette(),dtype=np.uint8).reshape(-1,3)
    result=[]
    for idx in np.unique(labels):
        c=palette[idx]
        if np.min(c)>=250:
            continue
        result.append(("#%02x%02x%02x"%tuple(c),labels==idx))
    return result


def mask_path(mask):
    verts=[]; codes=[]
    for y,row in enumerate(mask):
        runs=np.flatnonzero(np.diff(np.r_[False,row,False])).reshape(-1,2)
        for x0,x1 in runs:
            verts.extend([(x0,y),(x1,y),(x1,y+1),(x0,y+1),(x0,y)])
            codes.extend([MplPath.MOVETO,MplPath.LINETO,MplPath.LINETO,
                          MplPath.LINETO,MplPath.CLOSEPOLY])
    return MplPath(np.asarray(verts,float),codes) if verts else None


def arrow(ax,p0,p1,color=NAVY,lw=2.1,scale=15):
    ax.add_patch(FancyArrowPatch(p0,p1,arrowstyle="-|>",mutation_scale=scale,
        linewidth=lw,color=color,shrinkA=0,shrinkB=0,zorder=20))


def dipole(ax,cx,cy,w=132,h=58):
    left=np.array([(cx,cy-h/2),(cx-w/2,cy),(cx,cy+h/2)])
    right=np.array([(cx,cy-h/2),(cx+w/2,cy),(cx,cy+h/2)])
    ax.add_patch(Polygon(left,closed=True,facecolor=RED_LIGHT,edgecolor="none",zorder=12))
    ax.add_patch(Polygon(right,closed=True,facecolor=BLUE_LIGHT,edgecolor="none",zorder=12))
    ax.add_patch(Ellipse((cx,cy),w,h,fill=False,edgecolor=NAVY,lw=1.4,zorder=13))
    arrow(ax,(cx-28,cy),(cx+28,cy),NAVY,1.2,9)


def nonpolar(ax,cx,cy,w=132,h=58):
    ax.add_patch(Ellipse((cx,cy),w,h,facecolor="#7795da",edgecolor=NAVY,lw=1.4,zorder=13))
    ax.add_patch(Ellipse((cx,cy),w*0.55,h*0.65,facecolor="#91abe4",edgecolor="none",zorder=14))
    ax.add_patch(Circle((cx,cy),5,facecolor=YELLOW,edgecolor=NAVY,lw=0.8,zorder=15))


def correct_debye(ax):
    # Clean only the pictogram interiors, preserving the original card and central arrow.
    ax.add_patch(Polygon([(870,104),(1264,104),(1264,215),(870,215)],closed=True,
                         facecolor=CARD_3,edgecolor="none",zorder=10))
    ax.add_patch(Polygon([(870,357),(1264,357),(1264,470),(870,470)],closed=True,
                         facecolor=CARD_3,edgecolor="none",zorder=10))
    dipole(ax,958,161,132,58)
    nonpolar(ax,1178,161,132,58)
    dipole(ax,958,416,132,58)
    dipole(ax,1178,416,132,58)
    for dy in (-10,0,10):
        ax.plot([1025,1111],[416+dy,416+dy],color="#9fb5ca",lw=1.5,
                ls=(0,(4,3)),zorder=12)
    arrow(ax,(1095,321),(1124,374),"#e69a32",1.6,11)


def draw():
    rgb=np.asarray(Image.open(REF).convert("RGB"))
    rgb=erase_text(rgb)
    fig=plt.figure(figsize=(183/25.4,83.6/25.4),dpi=300,facecolor="white")
    ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,W); ax.set_ylim(H,0); ax.set_aspect("equal"); ax.axis("off")
    for color,mask in groups(rgb):
        path=mask_path(mask)
        if path is not None:
            ax.add_patch(PathPatch(path,facecolor=color,edgecolor="none",lw=0,zorder=1))
    correct_debye(ax)
    fig.savefig(OUT.with_suffix(".svg"),facecolor="white",bbox_inches=None,pad_inches=0)
    fig.savefig(OUT.with_suffix(".pdf"),facecolor="white",bbox_inches=None,pad_inches=0)
    fig.set_size_inches(2560/300,1169/300,forward=True)
    fig.savefig(OUT.with_suffix(".png"),dpi=300,facecolor="white",bbox_inches=None,pad_inches=0)
    plt.close(fig)


if __name__=="__main__": draw()
