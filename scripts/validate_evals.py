"""Validate the static Skill behavioral-contract dataset, not agent runtime behavior."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "evals" / "cases.json"
SKILL = ROOT / "skills" / "product-development-coach"


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        raise ValueError("Unexpected eval schema_version")
    cases = data.get("cases")
    if not isinstance(cases, list) or len(cases) < 10:
        raise ValueError("At least 10 static scenarios required")
    seen = set()
    positive = negative = 0
    for case in cases:
        case_id = case.get("id")
        if not isinstance(case_id, str) or not re.fullmatch(r"[a-z][a-z0-9_]+", case_id):
            raise ValueError("Invalid scenario ID")
        if case_id in seen:
            raise ValueError("Duplicate scenario ID")
        seen.add(case_id)
        if not isinstance(case.get("input"), str) or not case["input"].strip():
            raise ValueError(f"Missing input for {case_id}")
        for field in ("should", "must_not"):
            items = case.get(field)
            if not isinstance(items, list) or not items or not all(
                isinstance(item, str) and item.strip() for item in items
            ):
                raise ValueError(f"Missing {field} criteria for {case_id}")
        route = case.get("route")
        if route is None:
            negative += 1
        else:
            positive += 1
            if not isinstance(route, str) or not route.startswith("references/") or ".." in route:
                raise ValueError(f"Invalid route for {case_id}")
            if not (SKILL / route).is_file():
                raise ValueError(f"Missing guide for {case_id}")
    if negative < 2 or positive < 6:
        raise ValueError("Need both positive and negative routing scenarios")
    print(f"PASS: {len(cases)} static scenario contracts ({positive} skill, {negative} non-skill).")
    print("LIMITS: no live Codex invocation, model adherence, or production integration tested.")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, OSError, UnicodeError, json.JSONDecodeError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
