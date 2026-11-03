import sys

from units.convert import length


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 3:
        print("usage: units VALUE FROM TO", file=sys.stderr)
        return 2
    print(f"{length(float(args[0]), args[1], args[2]):g}")
    return 0
