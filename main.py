import os
import sys
from pathlib import Path

SENTENCE = "Imagine a library where the book you seek opens on your table at once, and any reader may write in its margins."

def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Write exactly one file, exactly the sentence, nothing else.
    (out_dir / "entry.txt").write_bytes(SENTENCE.encode("utf-8"))
    return 0

if __name__ == "__main__":
    sys.exit(main())
