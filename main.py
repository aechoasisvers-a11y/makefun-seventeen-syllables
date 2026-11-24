"""Seventeen Syllables of Debugging — make.fun entry.

Writes one haiku about debugging (5-7-5, seventeen syllables) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Pure stdlib Python 3.13. Deterministic: the same bytes every run.
"""

import os

HAIKU_LINES = (
    "red line on the log",
    "past midnight, the stack trace loops",
    "one semicolon",
)

HAIKU = "\n".join(HAIKU_LINES)

# Syllable counts for every word the haiku uses. A small explicit map
# keeps the check exact instead of guessing with a heuristic counter.
SYLLABLES = {
    "red": 1,
    "line": 1,
    "on": 1,
    "the": 1,
    "log": 1,
    "past": 1,
    "midnight": 2,
    "stack": 1,
    "trace": 1,
    "loops": 1,
    "one": 1,
    "semicolon": 4,
}

EXPECTED_SHAPE = (5, 7, 5)


def check_haiku(text: str) -> None:
    """Fail loudly if the text is not a 5-7-5 haiku inside the gate."""
    lines = text.split("\n")
    assert len(lines) == 3, f"expected 3 lines, got {len(lines)}"
    counts = []
    for line in lines:
        words = line.replace(",", "").split()
        counts.append(sum(SYLLABLES[w] for w in words))
    assert tuple(counts) == EXPECTED_SHAPE, (
        f"expected syllable shape {EXPECTED_SHAPE}, got {tuple(counts)}"
    )
    assert sum(counts) == 17, f"expected 17 syllables, got {sum(counts)}"
    assert 1 <= len(text) <= 200, f"expected 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"


def main() -> None:
    check_haiku(HAIKU)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(HAIKU)
    # Read back and verify the file on disk is exactly the intended text.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == HAIKU, "entry.txt on disk differs from the haiku"


if __name__ == "__main__":
    main()
