METRES_PER = {"m": 1.0, "km": 1000.0, "cm": 0.01, "mi": 1609.344, "ft": 0.3048}


def length(value: float, src: str, dst: str) -> float:
    return value * METRES_PER[src] / METRES_PER[dst]
