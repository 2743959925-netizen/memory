"""Trace the approved raster reference into a text-free SVG/PDF vector figure.

The reference is treated as the geometric authority. Colored foreground masks
are cleaned, text regions are removed, and the remaining contours are exported
as editable vector paths. This avoids redesign drift during reconstruction.
"""

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.path import Path as MplPath
from matplotlib.patches import PathPatch
import numpy as np
from PIL import Image


HERE = Path(__file__).resolve().parent
REF = HERE.parent / "2026-08-12_Figure3_自由能景观与动力学状态_低保真草图_v03.png"
OUT = HERE / "Figure3_FreeEnergyLandscape_vector_v03"
W, H = 1536, 1024
WIDTH_MM, HEIGHT_MM = 183, 122
PNG_WIDTH, PNG_HEIGHT, PNG_DPI = 2560, 1707, 300

mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
    "font.size": 7,
    "svg.fonttype": "none",
    "pdf.fonttype": 42,
})


TEXT_BOXES = [
    (0,0,45,48),(7,302,38,493),(210,768,640,802),(110,711,287,744),
    (350,651,515,691),(608,674,770,711),(205,378,330,412),
    (674,324,800,354),(15,960,350,1008),
    (854,8,891,48),(888,66,988,96),(1280,111,1348,143),
    (1132,346,1222,382),(1030,502,1118,532),(1397,384,1522,416),
    (854,572,890,614),
    (888,596,1025,628),(880,638,1025,670),
    (1110,596,1240,628),(1070,638,1270,670),
    (1342,596,1482,628),(1315,638,1520,670),
    (1045,854,1145,914),(856,873,876,899),(986,873,1008,899),
]


def erase_text(rgb):
    arr = rgb.copy()
    for x0,y0,x1,y1 in TEXT_BOXES:
        arr[y0:y1, x0:x1] = 255
    return arr


def quantized_groups(rgb):
    """Map antialiased source pixels to the reference's scientific palette."""
    palette = np.array([
        [255,255,255], [253,252,251], [7,29,93], [4,94,198],
        [12,130,42], [50,160,65], [232,128,15], [235,156,43],
        [248,47,27], [211,88,67], [222,121,95], [83,151,218],
        [142,186,216], [232,246,249], [156,128,150], [112,132,155],
    ], dtype=np.int32)
    flat = rgb.reshape(-1,3).astype(np.int32)
    distance = np.sum((flat[:,None,:] - palette[None,:,:]) ** 2, axis=2)
    labels = np.argmin(distance, axis=1).reshape(rgb.shape[:2])
    groups = {}
    for idx in np.unique(labels):
        color = palette[idx]
        if idx in (0,1):
            continue
        groups["#%02x%02x%02x" % tuple(color)] = labels == idx
    return groups


def mask_to_paths(mask):
    """Convert runs of pixels to compact filled vector rectangles."""
    # Run-length rectangles preserve the exact reference geometry while keeping
    # path counts manageable. Adjacent horizontal pixels become one rectangle.
    verts, codes = [], []
    h,w = mask.shape
    for y in range(h):
        row = mask[y]
        changes = np.flatnonzero(np.diff(np.r_[False,row,False]))
        for x0,x1 in changes.reshape(-1,2):
            verts.extend([(x0,y),(x1,y),(x1,y+1),(x0,y+1),(x0,y)])
            codes.extend([MplPath.MOVETO,MplPath.LINETO,MplPath.LINETO,
                          MplPath.LINETO,MplPath.CLOSEPOLY])
    return MplPath(np.asarray(verts,float), codes) if verts else None


def draw():
    rgb = np.asarray(Image.open(REF).convert("RGB"))
    rgb = erase_text(rgb)
    groups = quantized_groups(rgb)

    fig = plt.figure(figsize=(WIDTH_MM/25.4,HEIGHT_MM/25.4),dpi=300,facecolor="white")
    ax = fig.add_axes([0,0,1,1])
    ax.set_xlim(0,W); ax.set_ylim(H,0); ax.set_aspect("equal"); ax.axis("off")
    for color,mask in groups.items():
        path = mask_to_paths(mask)
        if path is not None:
            ax.add_patch(PathPatch(path,facecolor=color,edgecolor="none",lw=0))

    fig.savefig(OUT.with_suffix(".svg"),facecolor="white",bbox_inches=None,pad_inches=0)
    fig.savefig(OUT.with_suffix(".pdf"),facecolor="white",bbox_inches=None,pad_inches=0)
    fig.set_size_inches(PNG_WIDTH/PNG_DPI, PNG_HEIGHT/PNG_DPI, forward=True)
    fig.savefig(OUT.with_suffix(".png"),dpi=PNG_DPI,facecolor="white",
                bbox_inches=None,pad_inches=0)
    plt.close(fig)


if __name__ == "__main__":
    draw()
