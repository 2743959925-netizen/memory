"""Convert the approved Figure 4 PNG into a path-only SVG.

The conversion uses palette-aware horizontal run tracing.  Each visible run is
written as SVG path geometry; the source PNG is not embedded in the SVG.
"""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path

from PIL import Image


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "Figure4_VanDerWaals_principle_v05.png"
OUTPUT = HERE / "Figure4_VanDerWaals_principle_v05_vector.svg"

TARGET_WIDTH = 2560
PALETTE_SIZE = 64
WHITE_THRESHOLD = 252


def rgb_hex(rgb: tuple[int, int, int]) -> str:
    return "#{:02x}{:02x}{:02x}".format(*rgb)


def trace_runs(indexed: Image.Image) -> dict[int, list[str]]:
    """Return compact SVG path commands grouped by palette index."""
    width, height = indexed.size
    pixels = indexed.load()
    runs: dict[int, list[str]] = defaultdict(list)

    for y in range(height):
        x = 0
        while x < width:
            color_index = pixels[x, y]
            x0 = x
            x += 1
            while x < width and pixels[x, y] == color_index:
                x += 1
            runs[color_index].append(f"M{x0} {y}H{x}V{y + 1}H{x0}Z")
    return runs


def main() -> None:
    with Image.open(SOURCE) as opened:
        source = opened.convert("RGB")

    width, height = source.size
    target_height = round(height * TARGET_WIDTH / width)
    indexed = source.quantize(
        colors=PALETTE_SIZE,
        method=Image.Quantize.MEDIANCUT,
        dither=Image.Dither.NONE,
    )
    palette = indexed.getpalette()
    assert palette is not None

    colors = {
        index: tuple(palette[index * 3 : index * 3 + 3])
        for index in set(indexed.getdata())
    }
    runs = trace_runs(indexed)

    with OUTPUT.open("w", encoding="utf-8", newline="\n") as svg:
        svg.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        svg.write(
            f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'width="{TARGET_WIDTH}" height="{target_height}" '
            f'viewBox="0 0 {width} {height}" '
            f'role="img" aria-labelledby="title description">\n'
        )
        svg.write(
            "<title id=\"title\">Van der Waals forces: physical origin, "
            "interaction principle, strengths and limitations</title>\n"
        )
        svg.write(
            "<desc id=\"description\">Path-only vector tracing of the approved "
            "scientific schematic. No raster image is embedded.</desc>\n"
        )
        svg.write(f'<rect width="{width}" height="{height}" fill="#ffffff"/>\n')

        for index, commands in sorted(runs.items()):
            rgb = colors[index]
            if min(rgb) >= WHITE_THRESHOLD:
                continue
            svg.write(f'<path fill="{rgb_hex(rgb)}" d="')
            svg.write("".join(commands))
            svg.write('"/>\n')

        svg.write("</svg>\n")

    print(f"source={width}x{height}")
    print(f"svg={TARGET_WIDTH}x{target_height}")
    print(f"colors={len(colors)}")
    print(f"paths={sum(1 for c in colors.values() if min(c) < WHITE_THRESHOLD)}")
    print(OUTPUT)


if __name__ == "__main__":
    main()
