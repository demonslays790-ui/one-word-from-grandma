"""one-word-from-grandma.

Writes one original word -- the single word a grandma would text about
AI -- to <MAKEFUN_OUTPUT_DIR or /output>/entry.txt.

The word is "Witchcraft": the verdict a grandmother gives on a machine
that talks back, remembers everything and does things she cannot explain.
She has seen enough of the world to know real magic when she sees it,
and this, to her, is it. It reads as the one word she would text to a
grandchild about AI -- warm and a little baffled, funny with no caption
needed, tied to the machine-as-magic rather than any subject -- and it is
fresh against the obvious picks. The word is 10 characters, inside the
1-30 character gate.

Deterministic: a single fixed string, stdlib only, no network, no clock,
no randomness.
"""

import os

WORD = "Witchcraft"


def main() -> None:
    if not 1 <= len(WORD) <= 30:
        raise SystemExit("entry text must be 1-30 characters")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
