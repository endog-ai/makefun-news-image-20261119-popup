# A news-image-daily entry (Python 3.13, standard library only): its image is
# the entry.jpg beside this file, and the program copies it to
# /output/entry.png. The gate takes a whole PNG or JPEG of at most 1 MiB and
# 1024 by 1024 pixels, and the judge sees exactly the bytes copied.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
from pathlib import Path

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
src = Path(__file__).resolve().parent / "entry.jpg"
shutil.copyfile(src, out_dir / "entry.png")
