#!/usr/bin/env python3
"""Entry point for news-image-20261120, variant A (Front Page Classic).

Pure-stdlib byte relay: copies the committed entry.png into
$MAKEFUN_OUTPUT_DIR/entry.png. No drawing, no network, no randomness —
two runs produce byte-identical output.
"""
import os
import sys


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        out_dir = os.path.join(os.getcwd(), "output")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.png"), "rb") as f:
        data = f.read()
    with open(os.path.join(out_dir, "entry.png"), "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
