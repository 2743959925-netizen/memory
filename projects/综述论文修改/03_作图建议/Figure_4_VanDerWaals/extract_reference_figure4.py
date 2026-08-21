"""Extract the embedded Figure 4 reference from the manuscript without editing it."""

from pathlib import Path
import sys
import zipfile


docx = Path(sys.argv[1])
out = Path(__file__).resolve().parent / "Figure4_reference_original.jpeg"
with zipfile.ZipFile(docx) as zf:
    out.write_bytes(zf.read("word/media/image4.jpeg"))
print(out)
