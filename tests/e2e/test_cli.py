import pytest

from cli.main import run


@pytest.mark.parametrize(("argv"), [(["-1", "2,3,4"])])
def test_cli_run_invalid_start(argv: list[str]):
    with pytest.raises(ValueError, match=r"Floor number must be greater than zero"):
        run(argv)


@pytest.mark.parametrize(
    ("argv", "exptect_out"),
    [
        (
            ["12", "2,9,1,32"],
            "560 [12, 2, 9, 1, 32]\n",
        ),
        (
            ["--strategy", "fifo", "12", "2,9,1,32"],
            "560 [12, 2, 9, 1, 32]\n",
        ),
        (
            ["--strategy", "nearest", "12", "2,9,1,32"],
            "420 [12, 9, 2, 1, 32]\n",
        ),
        (
            ["--strategy", "dirup", "12", "2,9,1,32"],
            "510 [12, 32, 9, 2, 1]\n",
        ),
        (
            ["--strategy", "dirdown", "12", "2,9,1,32"],
            "420 [12, 9, 2, 1, 32]\n",
        ),
    ],
)
def test_cli_run(argv: list[str], exptect_out: str, capsys):
    run(argv)

    captured = capsys.readouterr()
    assert captured.out == exptect_out
