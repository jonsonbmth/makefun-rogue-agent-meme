#!/usr/bin/env python3
"""Meme Sprint 3: AI Agent Goes Rogue.

Entrypoint for the make.fun program/v1 harness. The grader runs this file
as `python3 -P -s /bot/main.py` with the repository read-only at /bot and
an empty writable directory at $MAKEFUN_OUTPUT_DIR. This program delivers
the meme by copying the AI-generated image shipped in the repository
(meme.png) into the output directory, where the judge reads it.

Standard library only. No network, no randomness, no wall-clock time:
two runs produce byte-identical output.
"""

import hashlib
import os
import shutil
import sys

IMAGE_NAME = "meme.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main() -> int:
    bot_dir = os.environ.get("MAKEFUN_BOT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    source = os.path.join(bot_dir, IMAGE_NAME)

    with open(source, "rb") as handle:
        data = handle.read()
    if not data.startswith(PNG_MAGIC):
        print(f"error: {IMAGE_NAME} is not a PNG file", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, IMAGE_NAME)
    with open(target, "wb") as handle:
        handle.write(data)

    digest = hashlib.sha256(data).hexdigest()
    with open(target, "rb") as handle:
        written = handle.read()
    if hashlib.sha256(written).hexdigest() != digest:
        print("error: written meme failed its integrity check", file=sys.stderr)
        return 1

    print(
        f"meme delivered: {IMAGE_NAME} "
        f"({len(data)} bytes, sha256={digest}) -> {target}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
