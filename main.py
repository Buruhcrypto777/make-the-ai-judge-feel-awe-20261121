"""Make the AI judge feel awe -- make.fun bounty entry.

Writes one short text, written to relax the reader, to
/output/entry.txt. Pure standard library; the output is
deterministic -- the same bytes on every run.
"""

import os
from pathlib import Path

TEXT = (
    "Far above the clouds, the night unfolds star by star, slow as snow "
    "settling on a field no one walks. You are small beneath it, and that "
    "is the gift: the sky does not hurry, the dark holds you, and every "
    "tired thought has room to drift away and rest."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 280:
        raise ValueError(
            f"entry text must be 1-280 characters, got {len(TEXT)}"
        )
    if not TEXT.strip():
        raise ValueError("entry text must not be only whitespace")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
