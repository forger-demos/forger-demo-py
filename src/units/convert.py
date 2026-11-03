from collections.abc import Callable

Conversion = tuple[Callable[[float], float], Callable[[float], float]]


def _factor(per_base: float) -> Conversion:
    return (lambda v: v * per_base, lambda v: v / per_base)


# Each quantity maps a unit to (to_base, from_base). Temperature needs an
# offset as well as a factor, so conversions are functions, not just factors.
QUANTITIES: dict[str, dict[str, Conversion]] = {
    "length": {
        "m": _factor(1.0),
        "km": _factor(1000.0),
        "cm": _factor(0.01),
        "mi": _factor(1609.344),
        "ft": _factor(0.3048),
    },
    "mass": {
        "g": _factor(1.0),
        "kg": _factor(1000.0),
        "lb": _factor(453.59237),
        "oz": _factor(28.349523125),
    },
    "temperature": {
        "C": (lambda v: v, lambda v: v),
        "F": (lambda v: (v - 32) * 5 / 9, lambda v: v * 9 / 5 + 32),
        "K": (lambda v: v - 273.15, lambda v: v + 273.15),
    },
}


class UnknownUnit(ValueError):
    pass


class QuantityMismatch(ValueError):
    pass


def all_units() -> list[str]:
    return [unit for table in QUANTITIES.values() for unit in table]


def quantity_of(unit: str) -> str:
    for name, table in QUANTITIES.items():
        if unit in table:
            return name
    raise UnknownUnit(unit)


def convert(value: float, src: str, dst: str) -> float:
    src_quantity = quantity_of(src)
    dst_quantity = quantity_of(dst)
    if src_quantity != dst_quantity:
        raise QuantityMismatch(
            f"cannot convert {src} ({src_quantity}) to {dst} ({dst_quantity})"
        )
    table = QUANTITIES[src_quantity]
    return table[dst][1](table[src][0](value))


def length(value: float, src: str, dst: str) -> float:
    return convert(value, src, dst)
