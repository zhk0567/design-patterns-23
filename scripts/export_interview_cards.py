"""Export docs/INTERVIEW.md Q&A to CSV (Anki-compatible)."""

from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs" / "INTERVIEW.md"
OUTPUT_CSV = ROOT / "docs" / "interview_cards.csv"


def _parse_cards(text: str) -> list[tuple[str, str, str]]:
    cards: list[tuple[str, str, str]] = []
    section = ""
    pending_q = ""
    for line in text.splitlines():
        if line.startswith("## "):
            section = line.removeprefix("## ").strip()
        elif line.startswith("**Q"):
            pending_q = re.sub(r"^\*\*Q\d*\.?\*\*\s*", "", line).strip()
        elif line.startswith("**A.**") and pending_q:
            ans = line.removeprefix("**A.**").strip()
            cards.append((section, pending_q, ans))
            pending_q = ""
    return cards


def main() -> None:
    text = SOURCE.read_text(encoding="utf-8")
    cards = _parse_cards(text)
    with OUTPUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["section", "question", "answer"])
        writer.writerows(cards)
    print(f"[export] {len(cards)} cards -> {OUTPUT_CSV}")
    print("[export] Anki: File -> Import -> interview_cards.csv")


if __name__ == "__main__":
    main()
