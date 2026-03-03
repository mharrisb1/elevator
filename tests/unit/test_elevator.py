import pytest

from elevator.cost_model import CostModel, FixedTimeCostModel
from elevator.elevator import Elevator
from elevator.strategy import FifoStragey, Strategy


def test_elevator_invalid_starting_floor():
    with pytest.raises(ValueError, match="Floor number must be greater than zero"):
        Elevator(-1)


@pytest.mark.parametrize(
    (
        "start",
        "floors",
        "strategy",
        "cost_model",
        "expected_total_cost",
        "expected_visited",
    ),
    [
        (
            12,
            [2, 9, 1, 32],
            FifoStragey(),
            FixedTimeCostModel(),
            560,
            [12, 2, 9, 1, 32],
        ),
        (
            12,
            [2, 9, 9, 9, 9, 1, 32],
            FifoStragey(),
            FixedTimeCostModel(),
            560,
            [12, 2, 9, 1, 32],
        ),
    ],
)
def test_elevator_run(  # noqa: PLR0913, PLR0917
    start: int,
    floors: list[int],
    strategy: Strategy,
    cost_model: CostModel,
    expected_total_cost: int,
    expected_visited: list[int],
):
    elevator = Elevator(start)
    result = elevator.run(floors, strategy, cost_model)

    assert result.total_cost == expected_total_cost
    assert result.visited == expected_visited
