import pytest

from elevator.cost_model import FixedTimeCostModel


@pytest.mark.parametrize(
    ("single_floor_travel_time", "from_floor", "to_floor", "expected"),
    [
        (10, 2, 12, 100),
        (2, 2, 12, 20),
        (10, 14, 12, 20),
    ],
)
def test_fixed_time_cost_model(
    single_floor_travel_time: int,
    from_floor: int,
    to_floor: int,
    expected: int,
):
    actual = FixedTimeCostModel(single_floor_travel_time).cost(from_floor, to_floor)
    assert actual == expected
