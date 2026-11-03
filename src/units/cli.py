import sys

from units.convert import METRES_PER, length


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 3:
        print("usage: units VALUE FROM TO", file=sys.stderr)
        return 2
    value_text, src, dst = args
    for unit in (src, dst):
        if unit not in METRES_PER:
            known = ", ".join(METRES_PER)
            print(f"unknown unit: {unit} (known: {known})", file=sys.stderr)
            return 2
    try:
        value = float(value_text)
    except ValueError:
        print(f"not a number: {value_text}", file=sys.stderr)
        return 2
    print(f"{length(value, src, dst):g}")
    return 0
