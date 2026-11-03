from units.convert import length
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
