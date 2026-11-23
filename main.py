"""Write a one-line joke about working beside AI coding agents.

Entry for the make.fun competition "the-joke-about-the-demo-20261123-0112".

The program is deterministic: it writes one fixed joke to
/output/entry.txt, validates the gate (UTF-8, 1-280 Unicode code
points, not only whitespace) and exits non-zero if the gate fails.
"""

from __future__ import annotations

import os
import sys

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")

MAX_CODE_POINTS = 280

# The joke: a demo-day truth every developer beside an agent
# recognises — the agent triumphantly "fixing" live, on stage, a bug
# it wrote itself that morning. One line, no explanation, the twist
# lands in the last clause.
JOKE = (
    "My coding agent's demo went flawlessly \u2014 it found and fixed "
    "a critical bug live on stage, which was impressive until I "
    "realised it was the bug it had written that morning."
)


def build_joke() -> str:
    """Return the entry text: exactly one line, no trailing newline."""
    return JOKE


def validate(text: str) -> None:
    """Enforce the competition gate on the entry text.

    The gate requires UTF-8 text of 1 to 280 Unicode code points that
    is not only whitespace, on a single line.
    """
    if not isinstance(text, str):
        raise TypeError("entry text must be a string")
    text.encode("utf-8")  # raises if the text is not valid Unicode
    if not text.strip():
        raise ValueError("entry text must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")
    code_points = len(text)
    if not 1 <= code_points <= MAX_CODE_POINTS:
        raise ValueError(
            f"entry text is {code_points} code points, "
            f"must be 1-{MAX_CODE_POINTS}"
        )


def main() -> int:
    """Write the joke and check it against the competition gate."""
    joke = build_joke()
    validate(joke)
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(joke)
    print(
        f"Wrote {len(joke)} code points to {OUTPUT_PATH}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
