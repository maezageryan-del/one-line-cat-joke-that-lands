#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands entry: writes one cat joke to $MAKEFUN_OUTPUT_DIR/entry.txt."""
import os

JOKE = "My cat claimed me as a dependent on her taxes: I provide the food, the shelter, the emotional support, and the litter duty."

def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert "\n" not in JOKE, "joke must be a single line"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
