import pytest

from elevator.controller import Controller
from elevator.cost_model import CostModel, FixedTimeCostModel
from elevator.strategy import (
    Direction,
    DirectionAwareNearestFloorStrategy,
    FifoStragey,
    NearestFloorStrategy,
    Strategy,
)


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
        (
            12,
            [2, 9, 1, 32],
            NearestFloorStrategy(),
            FixedTimeCostModel(),
            420,
            [12, 9, 2, 1, 32],
        ),
        (
            12,
            [2, 9, 9, 9, 9, 9, 1, 32],
            NearestFloorStrategy(),
            FixedTimeCostModel(),
            420,
            [12, 9, 2, 1, 32],
        ),
        (
            12,
            [2, 9, 1, 32],
            DirectionAwareNearestFloorStrategy(Direction.UP),
            FixedTimeCostModel(),
            510,
            [12, 32, 9, 2, 1],
        ),
        (
            12,
            [2, 9, 9, 9, 9, 9, 1, 32],
            DirectionAwareNearestFloorStrategy(Direction.UP),
            FixedTimeCostModel(),
            590,
            [12, 32, 9, 2, 1, 9],
        ),
        (
            12,
            [2, 9, 1, 32],
            DirectionAwareNearestFloorStrategy(Direction.DOWN),
            FixedTimeCostModel(),
            420,
            [12, 9, 2, 1, 32],
        ),
    ],
)
def test_controller_dispatch(  # noqa: PLR0913, PLR0917
    strategy: Strategy,
    cost_model: CostModel,
    start: int,
    floors: list[int],
    expected_total_cost: int,
    expected_visited: list[int],
):
    controller = Controller(strategy, cost_model)
    result = controller.dispatch(start, floors)

    assert result.total_cost == expected_total_cost
    assert result.visited == expected_visited
