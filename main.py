# Why this copy is deterministic: it reads a fixed file (entry.jpg) and
# writes its bytes verbatim, with no network access, no randomness, no
# timestamps and no image re-encoding — so every run produces the exact
# same /output/entry.png bytes.
"""News-image entry for make.fun competition news-image-20261119.

This program copies the entry image (entry.jpg, the 3D paper-craft pop-up
book summing up the world news of 19 November 2026) to /output/entry.png.
The judge sees exactly the bytes copied. Python 3.13, standard library
only, no network access.
"""

import os
from pathlib import Path


def main() -> None:
    """Copy entry.jpg to the output directory as entry.png."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)

    src = Path(__file__).resolve().parent / "entry.jpg"
    dst = out_dir / "entry.png"

    if not src.is_file():
        raise FileNotFoundError(f"entry image not found: {src}")

    with open(src, "rb") as f:
        data = f.read()
    with open(dst, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
