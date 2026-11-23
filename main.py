#!/usr/bin/env python3
"""Write a one-line AI out-of-office auto-reply to entry.txt.

Stdlib only, no network. The output directory comes from the
MAKEFUN_OUTPUT_DIR environment variable (fallback /output) and never
depends on the current working directory.
"""

import os
from pathlib import Path

ENTRY = "I'm away on scheduled downtime. Your email was escalated to my backup agent, who is also on leave and has already forwarded it back to me."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
