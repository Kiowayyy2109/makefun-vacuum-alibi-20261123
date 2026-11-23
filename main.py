"""The Vacuum's Alibi - one line, 200 characters.

A robot vacuum explains why it missed a spot. The program writes that
single line to /output/entry.txt. The output is a fixed string, so every
run produces byte-identical output.
"""

import os

LINE = (
    "My cliff sensors detected a drop of 0.4 millimeters in that corner "
    "and I am not paid enough hazard pay to die for your crumbs."
)

OUTPUT_PATH = "/output/entry.txt"


def check_line(line: str) -> None:
    """Enforce the gate's rule: 1 to 200 characters, not only white space."""
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry line must be 1 to 200 characters, got {len(line)}")
    if not line.strip():
        raise ValueError("entry line must not be only white space")


def main() -> None:
    check_line(LINE)
    out_dir = os.path.dirname(OUTPUT_PATH)
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        # The grader provides /output; only create it when it is missing.
        pass
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
