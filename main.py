#!/usr/bin/env python3
"""The Houseplant Out-of-Office.

Writes one out-of-office auto-reply as a houseplant would send it.
Deterministic, standard library only, no network, no clock, no secrets.
"""
import os

LINE = (
    "On leave. My owner waters the succulents first, so I've unionised "
    "with the cactus. No emails till rain."
)


def main():
    if not 1 <= len(LINE) <= 120:
        raise ValueError("entry must be 1 to 120 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
