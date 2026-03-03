import pytest

from elevator.utils import parse_csv, validate_floor


@pytest.mark.parametrize(
    ("value", "is_valid"),
    [
        (-3, False),
        (0, False),
        (12, True),
    ],
)
def test_validate_floor(value: int, is_valid: bool):
    if not is_valid:
        with pytest.raises(ValueError, match="Floor number must be greater than zero"):
            validate_floor(value)

    else:
        assert value == validate_floor(value)


@pytest.mark.parametrize(
    ("s", "is_valid", "size"),
    [
        ("1, 2, 3, 4, 5, 6, 7, 8, 9, 10", True, 10),
        ("1, 2, 3,45,6, 7,8, 9,10", True, 9),
        ("a, b, c, d", False, 0),
        ("1, 2, 3, a", False, 0),
        ("1, 2, 3, 4, 5, 6, 7, 8, 9, -10", False, 0),
    ],
)
def test_parse_csv(s: str, is_valid: bool, size: int):
    if not is_valid:
        with pytest.raises(ValueError, match=r".*"):
            parse_csv(s)

    else:
        data = parse_csv(s)
        assert len(data) == size
