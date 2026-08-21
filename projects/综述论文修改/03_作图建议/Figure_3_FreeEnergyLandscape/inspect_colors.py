from pathlib import Path
from PIL import Image
import numpy as np
import trace_reference_vector as tr

here = Path(__file__).resolve().parent
ref = Image.open(here.parent / "2026-08-12_Figure3_自由能景观与动力学状态_低保真草图_v03.png").convert("RGB")
new = Image.open(here / "Figure3_FreeEnergyLandscape_vector_v03.png").convert("RGB")
for xy in [(147,621),(170,645),(407,560),(650,590),(1235,142),(964,282),(1337,313)]:
    print(xy, "ref", ref.getpixel(xy), "new", new.getpixel(xy))
q=ref.quantize(colors=64, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
pal=np.asarray(q.getpalette(),dtype=np.uint8).reshape(-1,3)
lab=np.asarray(q)
for xy in [(147,621),(170,645),(1235,142),(964,282),(1337,313)]:
    x,y=xy; idx=lab[y,x]; print(xy,"idx",idx,"pal",pal[idx])
arr=np.asarray(ref)
groups=tr.quantized_groups(tr.erase_text(arr))
for xy in [(147,621),(170,645),(1235,142),(964,282),(1337,313)]:
    x,y=xy; print("group",xy,[c for c,m in groups.items() if m[y,x]])
