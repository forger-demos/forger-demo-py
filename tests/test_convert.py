import pytest

from units.convert import UnknownUnit, convert, length
from units.cli import main


def test_km_to_m():
    assert length(1, "km", "m") == 1000


def test_cli_prints_result(capsys):
    assert main(["2", "km", "m"]) == 0
    assert capsys.readouterr().out.strip() == "2000"


def test_cli_usage():
    assert main([]) == 2


def test_cli_unknown_unit(capsys):
    assert main(["3", "parsec", "m"]) == 2
    err = capsys.readouterr().err.strip()
    assert err.startswith("unknown unit: parsec (known: ")
    assert "km" in err
    assert "\n" not in err


def test_cli_unknown_target_unit(capsys):
    assert main(["3", "m", "parsec"]) == 2
    assert "unknown unit: parsec" in capsys.readouterr().err


def test_cli_not_a_number(capsys):
    assert main(["x", "km", "m"]) == 2
    assert capsys.readouterr().err.strip() == "not a number: x"


def test_cli_mass(capsys):
    assert main(["1", "kg", "lb"]) == 0
    assert capsys.readouterr().out.strip() == "2.20462"


def test_cli_ounces_to_grams(capsys):
    assert main(["1", "oz", "g"]) == 0
    assert capsys.readouterr().out.strip() == "28.3495"


def test_cli_celsius_to_fahrenheit(capsys):
    assert main(["100", "C", "F"]) == 0
    assert capsys.readouterr().out.strip() == "212"


def test_cli_kelvin_to_celsius(capsys):
    assert main(["0", "K", "C"]) == 0
    assert capsys.readouterr().out.strip() == "-273.15"


def test_cli_fahrenheit_to_kelvin(capsys):
    assert main(["32", "F", "K"]) == 0
    assert capsys.readouterr().out.strip() == "273.15"


def test_cli_cross_quantity_names_both(capsys):
    assert main(["1", "km", "kg"]) == 2
    err = capsys.readouterr().err
    assert "km" in err and "kg" in err
    assert "length" in err and "mass" in err


def test_cli_usage_lists_units(capsys):
    assert main([]) == 2
    err = capsys.readouterr().err
    for unit in ("km", "lb", "oz", "C", "F", "K"):
        assert unit in err


def test_convert_round_trip_temperature():
    assert convert(convert(37, "C", "F"), "F", "C") == pytest.approx(37)


def test_convert_unknown_unit_raises():
    with pytest.raises(UnknownUnit):
        convert(1, "parsec", "m")
