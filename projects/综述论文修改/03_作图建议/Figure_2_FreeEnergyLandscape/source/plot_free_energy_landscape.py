"""Generate an editable SVG schematic for the self-assembly free-energy landscape.

This script intentionally uses only the Python standard library so it can run without
third-party plotting packages. The output is a vector SVG with editable text nodes.
"""

from math import atan2, cos, degrees, sin
from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


OUTPUT_DIR = Path(__file__).resolve().parents[1] / "output"
OUTPUT_BASE = OUTPUT_DIR / "Figure_2_FreeEnergyLandscape_v01"
SVG_FILE = OUTPUT_BASE.with_suffix(".svg")
PDF_FILE = OUTPUT_BASE.with_suffix(".pdf")
PNG_FILE = OUTPUT_BASE.with_suffix(".png")
TIFF_FILE = OUTPUT_BASE.with_suffix(".tiff")
FONT_FILE = Path(r"C:\Windows\Fonts\arial.ttf")

WIDTH_MM = 183
HEIGHT_MM = 110
VIEWBOX_WIDTH = 1830
VIEWBOX_HEIGHT = 1100

# Native SVG <text> nodes are written directly (equivalent to svg.fonttype='none').
# ReportLab embeds TrueType text in the PDF (equivalent to pdf.fonttype=42).

COLORS = {
    "axis": "#272727",
    "curve": "#40594C",
    "text": "#272727",
    "amber": "#D39A2C",
    "amber_fill": "#F4D79E",
    "green": "#609B6C",
    "green_fill": "#C8DEC9",
    "red": "#B8534B",
    "red_fill": "#EDC4BF",
    "blue": "#1F5CA8",
    "blue_fill": "#D9E7F7",
    "grey": "#777777",
}


def text(x, y, value, size=30, fill=COLORS["text"], anchor="start", weight="400"):
    """Create an editable SVG text element."""
    return (
        f'<text x="{x}" y="{y}" fill="{fill}" font-family="Arial, Helvetica, sans-serif" '
        f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{escape(value)}</text>'
    )


def circle(cx, cy, r, stroke, fill, width=3):
    return (
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" '
        f'stroke="{stroke}" stroke-width="{width}"/>'
    )


def molecular_pair(x, y, stroke, fill, connected=True):
    """Draw two flat molecular units as a restrained support symbol."""
    items = []
    if connected:
        items.append(f'<line x1="{x}" y1="{y}" x2="{x + 55}" y2="{y}" stroke="{stroke}" stroke-width="4"/>')
    items.extend([
        circle(x, y, 16, stroke, fill),
        circle(x + 55, y, 16, stroke, fill),
        circle(x + 110, y, 16, stroke, fill),
    ])
    return "\n".join(items)


def curve_segments():
    """Return the cubic Bézier segments of the non-dissipative landscape."""
    return [
        ((180, 410), (255, 475), (315, 635), (405, 610)),
        ((405, 610), (490, 585), (525, 430), (585, 390)),
        ((585, 390), (655, 470), (700, 735), (820, 760)),
        ((820, 760), (930, 785), (975, 400), (1065, 255)),
        ((1065, 255), (1155, 350), (1170, 630), (1250, 620)),
        ((1250, 620), (1305, 613), (1340, 505), (1380, 430)),
    ]


def bezier_points(segment, steps=50):
    """Sample a cubic Bézier segment for the PNG preview."""
    p0, p1, p2, p3 = segment
    points = []
    for index in range(steps + 1):
        t = index / steps
        u = 1 - t
        x = u**3 * p0[0] + 3 * u**2 * t * p1[0] + 3 * u * t**2 * p2[0] + t**3 * p3[0]
        y = u**3 * p0[1] + 3 * u**2 * t * p1[1] + 3 * u * t**2 * p2[1] + t**3 * p3[1]
        points.append((x, y))
    return points


def register_arial():
    if not FONT_FILE.exists():
        raise FileNotFoundError(f"Arial font is required but missing: {FONT_FILE}")
    registerFont(TTFont("Arial", str(FONT_FILE)))


def draw_pdf_arrow(pdf, start, end, color, width=4):
    """Draw an arrow in SVG-style coordinates on the PDF canvas."""
    scale = WIDTH_MM / 25.4 * 72 / VIEWBOX_WIDTH
    height = HEIGHT_MM / 25.4 * 72

    def point(value):
        return value[0] * scale, height - value[1] * scale

    x1, y1 = point(start)
    x2, y2 = point(end)
    pdf.setStrokeColor(color)
    pdf.setFillColor(color)
    pdf.setLineWidth(width * scale)
    pdf.line(x1, y1, x2, y2)
    angle = degrees(atan2(y2 - y1, x2 - x1))
    arrow_size = 13 * scale
    pdf.saveState()
    pdf.translate(x2, y2)
    pdf.rotate(angle)
    path = pdf.beginPath()
    path.moveTo(0, 0)
    path.lineTo(-arrow_size, arrow_size * 0.55)
    path.lineTo(-arrow_size, -arrow_size * 0.55)
    path.close()
    pdf.drawPath(path, fill=1, stroke=0)
    pdf.restoreState()


def draw_pdf():
    """Write a vector PDF with editable embedded TrueType text."""
    register_arial()
    width_pt = WIDTH_MM / 25.4 * 72
    height_pt = HEIGHT_MM / 25.4 * 72
    scale = width_pt / VIEWBOX_WIDTH
    pdf = canvas.Canvas(str(PDF_FILE), pagesize=(width_pt, height_pt), pageCompression=1)

    def xy(x, y):
        return x * scale, height_pt - y * scale

    def set_fill(color):
        pdf.setFillColor(color)

    def text_pdf(x, y, value, size=30, color=COLORS["text"], anchor="start"):
        px, py = xy(x, y)
        pdf.setFillColor(color)
        pdf.setFont("Arial", size * scale)
        if anchor == "middle":
            px -= pdf.stringWidth(value, "Arial", size * scale) / 2
        pdf.drawString(px, py, value)

    def circle_pdf(cx, cy, r, stroke, fill, width=3):
        px, py = xy(cx, cy)
        pdf.setStrokeColor(stroke)
        pdf.setFillColor(fill)
        pdf.setLineWidth(width * scale)
        pdf.circle(px, py, r * scale, fill=1, stroke=1)

    def pair_pdf(x, y, stroke, fill):
        pdf.setStrokeColor(stroke)
        pdf.setLineWidth(4 * scale)
        x1, y1 = xy(x, y)
        x2, y2 = xy(x + 55, y)
        pdf.line(x1, y1, x2, y2)
        for offset in (0, 55, 110):
            circle_pdf(x + offset, y, 16, stroke, fill)

    pdf.setFillColor("#FFFFFF")
    pdf.rect(0, 0, width_pt, height_pt, fill=1, stroke=0)
    draw_pdf_arrow(pdf, (135, 930), (1730, 930), COLORS["axis"])
    draw_pdf_arrow(pdf, (135, 930), (135, 105), COLORS["axis"])
    pdf.saveState()
    px, py = xy(70, 540)
    pdf.translate(px, py)
    pdf.rotate(90)
    pdf.setFillColor(COLORS["axis"])
    pdf.setFont("Arial", 34 * scale)
    pdf.drawCentredString(0, 0, "Gibbs free energy, G")
    pdf.restoreState()
    text_pdf(900, 1000, "Assembly coordinate", size=34, anchor="middle")

    path = pdf.beginPath()
    first = True
    for p0, p1, p2, p3 in curve_segments():
        if first:
            path.moveTo(*xy(*p0))
            first = False
        path.curveTo(*xy(*p1), *xy(*p2), *xy(*p3))
    pdf.setStrokeColor(COLORS["curve"])
    pdf.setLineWidth(6 * scale)
    pdf.setLineCap(1)
    pdf.setLineJoin(1)
    pdf.drawPath(path, fill=0, stroke=1)

    text_pdf(500, 350, "finite ΔG‡", size=28, anchor="middle")
    text_pdf(1065, 195, "large ΔG‡", size=28, anchor="middle")
    circle_pdf(405, 590, 15, COLORS["amber"], COLORS["amber_fill"])
    circle_pdf(820, 740, 15, COLORS["green"], COLORS["green_fill"])
    circle_pdf(1250, 600, 15, COLORS["red"], COLORS["red_fill"])
    text_pdf(405, 680, "Metastable state", size=29, anchor="middle")
    pair_pdf(325, 735, COLORS["amber"], COLORS["amber_fill"])
    text_pdf(820, 845, "Thermodynamic", size=29, anchor="middle")
    text_pdf(820, 880, "equilibrium state", size=29, anchor="middle")
    pair_pdf(735, 805, COLORS["green"], COLORS["green_fill"])
    text_pdf(1250, 685, "Kinetically trapped state", size=29, anchor="middle")
    pair_pdf(1170, 745, COLORS["red"], COLORS["red_fill"])

    x, y = xy(1440, 325)
    pdf.setFillColor("#FFFFFF")
    pdf.setStrokeColor(COLORS["blue"])
    pdf.setLineWidth(4 * scale)
    pdf.roundRect(x, y, 300 * scale, 105 * scale, 52 * scale, fill=1, stroke=1)
    text_pdf(1590, 135, "Dissipative nonequilibrium", size=28, anchor="middle")
    text_pdf(1590, 168, "steady state", size=28, anchor="middle")
    pair_pdf(1515, 272, COLORS["blue"], COLORS["blue_fill"])
    draw_pdf_arrow(pdf, (1600, 600), (1600, 350), COLORS["blue"])
    text_pdf(1625, 460, "continuous energy", size=26, color=COLORS["blue"])
    text_pdf(1625, 492, "or matter input", size=26, color=COLORS["blue"])
    dashed = pdf.beginPath()
    dashed.moveTo(*xy(1490, 350))
    dashed.curveTo(*xy(1460, 430), *xy(1445, 550), *xy(1515, 675))
    pdf.setStrokeColor(COLORS["grey"])
    pdf.setLineWidth(4 * scale)
    pdf.setDash(14 * scale, 12 * scale)
    pdf.drawPath(dashed, fill=0, stroke=1)
    pdf.setDash()
    draw_pdf_arrow(pdf, (1505, 652), (1515, 675), COLORS["grey"])
    text_pdf(1520, 710, "input removed", size=26, color=COLORS["grey"])
    pdf.save()


def draw_png():
    """Write a 600-dpi PNG preview using the same Python geometry."""
    dpi = 600
    scale = dpi / 25.4 / 10
    size = (round(VIEWBOX_WIDTH * scale), round(VIEWBOX_HEIGHT * scale))
    image = Image.new("RGB", size, "white")
    draw = ImageDraw.Draw(image)

    def xy(x, y):
        return round(x * scale), round(y * scale)

    def font(size_pt):
        return ImageFont.truetype(str(FONT_FILE), round(size_pt * scale))

    def text_png(x, y, value, size=30, color=COLORS["text"], anchor="la"):
        draw.text(xy(x, y), value, font=font(size), fill=color, anchor=anchor)

    def circle_png(cx, cy, r, stroke, fill, width=3):
        x1, y1 = xy(cx - r, cy - r)
        x2, y2 = xy(cx + r, cy + r)
        draw.ellipse((x1, y1, x2, y2), fill=fill, outline=stroke, width=round(width * scale))

    def pair_png(x, y, stroke, fill):
        draw.line((xy(x, y), xy(x + 55, y)), fill=stroke, width=round(4 * scale))
        for offset in (0, 55, 110):
            circle_png(x + offset, y, 16, stroke, fill)

    def arrow_png(start, end, color, width=4):
        x1, y1 = xy(*start)
        x2, y2 = xy(*end)
        line_width = round(width * scale)
        draw.line((x1, y1, x2, y2), fill=color, width=line_width)
        angle = atan2(y2 - y1, x2 - x1)
        head = 13 * scale
        points = [
            (x2, y2),
            (x2 - head * cos(angle - 0.55), y2 - head * sin(angle - 0.55)),
            (x2 - head * cos(angle + 0.55), y2 - head * sin(angle + 0.55)),
        ]
        draw.polygon(points, fill=color)

    arrow_png((135, 930), (1730, 930), COLORS["axis"])
    arrow_png((135, 930), (135, 105), COLORS["axis"])
    text_png(900, 1000, "Assembly coordinate", 34, anchor="ma")
    y_label = Image.new("RGBA", (round(600 * scale), round(100 * scale)), (255, 255, 255, 0))
    label_draw = ImageDraw.Draw(y_label)
    label_draw.text((y_label.width // 2, y_label.height // 2), "Gibbs free energy, G", font=font(34), fill=COLORS["axis"], anchor="mm")
    y_label = y_label.rotate(90, expand=True)
    image.paste(y_label, (round(18 * scale), round(540 * scale - y_label.height / 2)), y_label)

    curve = []
    for segment in curve_segments():
        curve.extend(bezier_points(segment))
    draw.line([xy(x, y) for x, y in curve], fill=COLORS["curve"], width=round(6 * scale), joint="curve")
    text_png(500, 350, "finite ΔG‡", 28, anchor="ma")
    text_png(1065, 195, "large ΔG‡", 28, anchor="ma")
    circle_png(405, 590, 15, COLORS["amber"], COLORS["amber_fill"])
    circle_png(820, 740, 15, COLORS["green"], COLORS["green_fill"])
    circle_png(1250, 600, 15, COLORS["red"], COLORS["red_fill"])
    text_png(405, 680, "Metastable state", 29, anchor="ma")
    pair_png(325, 735, COLORS["amber"], COLORS["amber_fill"])
    text_png(820, 845, "Thermodynamic", 29, anchor="ma")
    text_png(820, 880, "equilibrium state", 29, anchor="ma")
    pair_png(735, 805, COLORS["green"], COLORS["green_fill"])
    text_png(1250, 685, "Kinetically trapped state", 29, anchor="ma")
    pair_png(1170, 745, COLORS["red"], COLORS["red_fill"])
    draw.rounded_rectangle((xy(1440, 220), xy(1740, 325)), radius=round(52 * scale), fill="white", outline=COLORS["blue"], width=round(4 * scale))
    text_png(1590, 135, "Dissipative nonequilibrium", 28, anchor="ma")
    text_png(1590, 168, "steady state", 28, anchor="ma")
    pair_png(1515, 272, COLORS["blue"], COLORS["blue_fill"])
    arrow_png((1600, 600), (1600, 350), COLORS["blue"])
    text_png(1625, 460, "continuous energy", 26, COLORS["blue"])
    text_png(1625, 492, "or matter input", 26, COLORS["blue"])
    dashed = bezier_points(((1490, 350), (1460, 430), (1445, 550), (1515, 675)), steps=80)
    for index in range(0, len(dashed) - 2, 8):
        if (index // 8) % 2 == 0:
            draw.line((xy(*dashed[index]), xy(*dashed[min(index + 7, len(dashed) - 1)])), fill=COLORS["grey"], width=round(4 * scale))
    arrow_png((1505, 652), (1515, 675), COLORS["grey"])
    text_png(1520, 710, "input removed", 26, COLORS["grey"])
    image.save(PNG_FILE, dpi=(dpi, dpi))
    image.save(TIFF_FILE, dpi=(dpi, dpi), compression="tiff_lzw")


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    elements = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        (
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH_MM}mm" height="{HEIGHT_MM}mm" '
            f'viewBox="0 0 {VIEWBOX_WIDTH} {VIEWBOX_HEIGHT}" role="img" '
            'aria-label="Conceptual Gibbs free-energy landscape for self-assembly">'
        ),
        '<defs>',
        f'<marker id="axis-arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto">'
        f'<path d="M 0 0 L 12 6 L 0 12 z" fill="{COLORS["axis"]}"/></marker>',
        f'<marker id="blue-arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto">'
        f'<path d="M 0 0 L 12 6 L 0 12 z" fill="{COLORS["blue"]}"/></marker>',
        f'<marker id="grey-arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto">'
        f'<path d="M 0 0 L 12 6 L 0 12 z" fill="{COLORS["grey"]}"/></marker>',
        '</defs>',
        '<rect width="100%" height="100%" fill="#FFFFFF"/>',
        # Axes.
        f'<line x1="135" y1="930" x2="1730" y2="930" stroke="{COLORS["axis"]}" stroke-width="4" marker-end="url(#axis-arrow)"/>',
        f'<line x1="135" y1="930" x2="135" y2="105" stroke="{COLORS["axis"]}" stroke-width="4" marker-end="url(#axis-arrow)"/>',
        (
            '<text x="70" y="540" fill="#272727" font-family="Arial, Helvetica, sans-serif" '
            'font-size="34" text-anchor="middle" transform="rotate(-90 70 540)">Gibbs free energy, G</text>'
        ),
        text(900, 1000, "Assembly coordinate", size=34, anchor="middle"),
        # The non-dissipative free-energy landscape: three basins only.
        (
            f'<path d="M 180 410 '
            f'C 255 475, 315 635, 405 610 '
            f'C 490 585, 525 430, 585 390 '
            f'C 655 470, 700 735, 820 760 '
            f'C 930 785, 975 400, 1065 255 '
            f'C 1155 350, 1170 630, 1250 620 '
            f'C 1305 613, 1340 505, 1380 430" '
            f'fill="none" stroke="{COLORS["curve"]}" stroke-width="6" '
            'stroke-linecap="round" stroke-linejoin="round"/> '
        ),
        # Barrier labels.
        text(500, 350, "finite ΔG‡", size=28, anchor="middle"),
        text(1065, 195, "large ΔG‡", size=28, anchor="middle"),
        # State markers at the three wells.
        circle(405, 590, 15, COLORS["amber"], COLORS["amber_fill"], width=3),
        circle(820, 740, 15, COLORS["green"], COLORS["green_fill"], width=3),
        circle(1250, 600, 15, COLORS["red"], COLORS["red_fill"], width=3),
        # Labels and restrained molecular symbols.
        text(405, 680, "Metastable state", size=29, anchor="middle"),
        molecular_pair(325, 735, COLORS["amber"], COLORS["amber_fill"]),
        text(820, 845, "Thermodynamic", size=29, anchor="middle"),
        text(820, 880, "equilibrium state", size=29, anchor="middle"),
        molecular_pair(735, 805, COLORS["green"], COLORS["green_fill"]),
        text(1250, 685, "Kinetically trapped state", size=29, anchor="middle"),
        molecular_pair(1170, 745, COLORS["red"], COLORS["red_fill"]),
        # Dissipative driven state, deliberately placed outside the Gibbs landscape.
        f'<rect x="1440" y="220" width="300" height="105" rx="52" fill="#FFFFFF" stroke="{COLORS["blue"]}" stroke-width="4"/>',
        text(1590, 135, "Dissipative nonequilibrium", size=28, anchor="middle"),
        text(1590, 168, "steady state", size=28, anchor="middle"),
        molecular_pair(1515, 272, COLORS["blue"], COLORS["blue_fill"]),
        # Energy or matter input and relaxation after removal.
        f'<line x1="1600" y1="600" x2="1600" y2="350" stroke="{COLORS["blue"]}" stroke-width="4" marker-end="url(#blue-arrow)"/>',
        text(1625, 460, "continuous energy", size=26, fill=COLORS["blue"]),
        text(1625, 492, "or matter input", size=26, fill=COLORS["blue"]),
        f'<path d="M 1490 350 C 1460 430, 1445 550, 1515 675" fill="none" '
        f'stroke="{COLORS["grey"]}" stroke-width="4" stroke-dasharray="14 12" marker-end="url(#grey-arrow)"/>',
        text(1520, 710, "input removed", size=26, fill=COLORS["grey"]),
        '</svg>',
    ]

    SVG_FILE.write_text("\n".join(elements), encoding="utf-8")
    draw_pdf()
    draw_png()
    for path in (SVG_FILE, PDF_FILE, PNG_FILE, TIFF_FILE):
        print(path)


if __name__ == "__main__":
    main()
