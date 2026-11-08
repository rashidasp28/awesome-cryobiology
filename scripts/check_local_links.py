#!/usr/bin/env python3
"""Check that local links in Markdown files resolve inside the repository."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


INLINE_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
REFERENCE_LINK = re.compile(r"^\s*\[[^\]]+\]:\s*(\S+)", re.MULTILINE)


def _target_path(raw_target: str) -> str | None:
    """Return the local path part of a Markdown target, if it has one."""
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    else:
        target = target.split(maxsplit=1)[0]

    if not target or target.startswith("#") or target.startswith("//"):
        return None

    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc:
        return None
    return unquote(parsed.path) or None


def find_broken_links(root: Path) -> list[str]:
    """Return deterministic diagnostics for unresolved local Markdown links."""
    root = root.resolve()
    problems: list[str] = []

    for document in sorted(root.rglob("*.md")):
        if any(part in {".git", "site"} for part in document.parts):
            continue

        text = document.read_text(encoding="utf-8")
        targets = [*INLINE_LINK.findall(text), *REFERENCE_LINK.findall(text)]
        for raw_target in targets:
            local_path = _target_path(raw_target)
            if local_path is None:
                continue

            if local_path.startswith("/"):
                candidate = root / local_path.lstrip("/")
            else:
                candidate = document.parent / local_path
            candidate = candidate.resolve()

            try:
                candidate.relative_to(root)
            except ValueError:
                problems.append(
                    f"{document.relative_to(root)}: link escapes repository: {raw_target}"
                )
                continue

            if not candidate.exists():
                problems.append(
                    f"{document.relative_to(root)}: missing target: {raw_target}"
                )

    return problems


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check local Markdown links without making network requests."
    )
    parser.add_argument(
        "root",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root (defaults to the parent of scripts/)",
    )
    args = parser.parse_args()

    problems = find_broken_links(args.root)
    if problems:
        print("Local Markdown link validation failed:", file=sys.stderr)
        for problem in problems:
            print(f"- {problem}", file=sys.stderr)
        return 1

    print("Local Markdown link validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
