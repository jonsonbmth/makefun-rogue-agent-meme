#!/usr/bin/env python3
"""Meme Sprint 3: AI Agent Goes Rogue.

Entrypoint for the make.fun program/v1 harness. The grader runs this file
as `python3 -P -s /bot/main.py` with the repository read-only at /bot and
an empty writable directory at $MAKEFUN_OUTPUT_DIR. This program delivers
the meme by copying the AI-generated image shipped in the repository
(entry.png) into the output directory as entry.png, where the sealed
scorer reads it. The gate requires a whole PNG or JPEG of at most
1 MiB (1,048,576 bytes) and at most 1024 by 1024 pixels; this program
checks those limits itself before writing and refuses to deliver an
image that would fail them.

Standard library only. No network, no randomness, no wall-clock time:
two runs produce byte-identical output.
"""

import hashlib
import os
import struct
import sys

IMAGE_NAME = "entry.png"
MAX_BYTES = 1_048_576
MAX_DIMENSION = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def png_dimensions(data: bytes) -> tuple[int, int]:
    """Read width and height from a PNG's IHDR chunk (stdlib only)."""
    if len(data) < 33 or data[12:16] != b"IHDR":
        raise ValueError("not a PNG with an IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


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
    if len(data) > MAX_BYTES:
        print(
            f"error: {IMAGE_NAME} is {len(data)} bytes, over the "
            f"{MAX_BYTES} byte gate limit",
            file=sys.stderr,
        )
        return 1
    try:
        width, height = png_dimensions(data)
    except ValueError as exc:
        print(f"error: {IMAGE_NAME}: {exc}", file=sys.stderr)
        return 1
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        print(
            f"error: {IMAGE_NAME} is {width}x{height}, over the "
            f"{MAX_DIMENSION}x{MAX_DIMENSION} gate limit",
            file=sys.stderr,
        )
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
        f"({width}x{height}, {len(data)} bytes, sha256={digest}) -> {target}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
