from units.convert import length
from units.cli import main


def test_km_to_m():
    assert length(1, "km", "m") == 1000


def test_cli_prints_result(capsys):
    assert main(["2", "km", "m"]) == 0
    assert capsys.readouterr().out.strip() == "2000"


def test_cli_usage():
    assert main([]) == 2
