"""The Funniest Office Joke — a single office joke, one line.

Setup: reply-all to escape a thread. Turn: the escape itself
becomes a reply-all storm — 47 people reply-all to agree.
"""

import os

TEXT = "I hit reply-all to ask to be removed from the thread. Forty-seven people replied-all to agree."


def main():
    # Self-gate mirroring the kit's sealed scorer: 1-200 UTF-8 chars, not
    # only white space.
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    assert TEXT.strip(), "entry must not be only white space"
    assert "\n" not in TEXT, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(TEXT)
    print("chars:", len(TEXT))


if __name__ == "__main__":
    main()
