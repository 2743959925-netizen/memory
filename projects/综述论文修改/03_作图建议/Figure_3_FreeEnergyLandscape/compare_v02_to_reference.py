"""Measure text-excluded structural similarity to the approved raster reference."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


HERE = Path(__file__).resolve().parent
REF = HERE.parent / "2026-08-12_Figure3_自由能景观与动力学状态_低保真草图_v03.png"
NEW = HERE / "Figure3_FreeEnergyLandscape_vector_v03.png"
OUT = HERE / "Figure3_FreeEnergyLandscape_vector_v03_comparison.png"


def foreground(rgb):
    rgb = rgb.astype(float)
    return np.min(rgb, axis=2) < 238


def dilate(mask, radius=4):
    out = np.zeros_like(mask)
    for dy in range(-radius, radius + 1):
        for dx in range(-radius, radius + 1):
            y0, y1 = max(0, dy), min(mask.shape[0], mask.shape[0] + dy)
            x0, x1 = max(0, dx), min(mask.shape[1], mask.shape[1] + dx)
            out[y0:y1, x0:x1] |= mask[y0-dy:y1-dy, x0-dx:x1-dx]
    return out


def main():
    ref = np.asarray(Image.open(REF).convert("RGB"))
    new = np.asarray(Image.open(NEW).convert("RGB").resize(
        (ref.shape[1], ref.shape[0]), Image.Resampling.LANCZOS))
    keep = np.ones(ref.shape[:2], dtype=bool)

    # Text and panel-letter regions are excluded because the requested vector is text-free.
    boxes = [
        (0,0,45,48),(7,302,38,493),(210,768,640,802),(110,711,287,744),
        (350,651,515,691),(608,674,770,711),(205,378,330,412),
        (674,324,800,354),(15,960,350,1008),(854,8,891,48),
        (888,66,988,96),(1280,111,1348,143),(1132,346,1222,382),
        (1030,502,1118,532),(1397,384,1522,416),(854,572,890,614),
        (888,596,1025,628),(880,638,1025,670),(1110,596,1240,628),
        (1070,638,1270,670),(1342,596,1482,628),(1315,638,1520,670),
        (1045,854,1145,914),(856,873,876,899),(986,873,1008,899),
    ]
    for x0,y0,x1,y1 in boxes:
        keep[y0:y1, x0:x1] = False

    r = foreground(ref) & keep
    n = foreground(new) & keep
    rd, nd = dilate(r, 5), dilate(n, 5)
    recall = (r & nd).sum() / max(1, r.sum())
    precision = (n & rd).sum() / max(1, n.sum())
    score = 2 * precision * recall / max(1e-9, precision + recall)
    color_pixels = r & n
    color_distance = np.linalg.norm(ref.astype(float)-new.astype(float), axis=2)
    color_score = np.mean(1.0 - np.clip(color_distance[color_pixels] / 441.67, 0, 1))
    combined = 0.65 * score + 0.35 * color_score

    overlay = np.full_like(ref, 255)
    overlap = r & n
    overlay[r] = [230, 58, 58]
    overlay[n] = [30, 150, 220]
    overlay[overlap] = [20, 125, 70]
    overlay[~keep] = [245,245,245]

    fig, ax = plt.subplots(figsize=(12,8), dpi=128)
    ax.imshow(overlay)
    ax.axis("off")
    fig.savefig(OUT, dpi=128, bbox_inches="tight", pad_inches=0)
    plt.close(fig)
    print(f"precision={precision:.4f}")
    print(f"recall={recall:.4f}")
    print(f"foreground_f1={score:.4f}")
    print(f"foreground_color={color_score:.4f}")
    print(f"combined_similarity={combined:.4f}")


if __name__ == "__main__":
    main()
