import sys

from units.convert import QuantityMismatch, all_units, convert


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 3:
        print("usage: units VALUE FROM TO", file=sys.stderr)
        print(f"units: {', '.join(all_units())}", file=sys.stderr)
        return 2
    value_text, src, dst = args
    known = all_units()
    for unit in (src, dst):
        if unit not in known:
            print(f"unknown unit: {unit} (known: {', '.join(known)})", file=sys.stderr)
            return 2
    try:
        value = float(value_text)
    except ValueError:
        print(f"not a number: {value_text}", file=sys.stderr)
        return 2
    try:
        result = convert(value, src, dst)
    except QuantityMismatch as err:
        print(str(err), file=sys.stderr)
        return 2
    print(f"{result:g}")
    return 0
