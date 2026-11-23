#!/usr/bin/env python3
"""Writes a one-line office joke to /output/entry.txt for make.fun."""
import os

JOKE = "Someone hit reply-all to 4,000 people saying 'please remove me,' and for one beautiful minute we were finally all aligned."


def validate_joke() -> None:
    if "\n" in JOKE or "\r" in JOKE:
        raise ValueError("Joke must be a single line")
    if not JOKE.strip():
        raise ValueError("Joke must not be only whitespace")
    if not (1 <= len(JOKE) <= 199):
        raise ValueError("Joke must be between 1 and 199 characters")
    # Validate UTF-8 encodability
    JOKE.encode("utf-8")


def main() -> None:
    validate_joke()

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
