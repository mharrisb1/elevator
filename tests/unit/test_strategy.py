import pytest

from elevator.strategy import (
    Direction,
    DirectionAwareNearestFloorStrategy,
    FifoStrategy,
    NearestFloorStrategy,
)


@pytest.mark.parametrize(
    ("current", "remaining", "expected"),
    [
        (12, [2, 9, 1, 32], 2),
        (1, [2, 3, 4, 5, 6, 7], 2),
    ],
)
def test_fifo_strategy(current: int, remaining: list[int], expected: int):
    next_floor = FifoStrategy().pick(current, remaining)
    assert next_floor == expected


@pytest.mark.parametrize(
    ("current", "remaining", "expected"),
    [
        (12, [2, 9, 1, 32], 9),
        (1, [2, 3, 4, 5, 6, 7], 2),
        (8, [2, 3, 4, 5, 6, 7], 7),
    ],
)
def test_nearest_floor_strategy(current: int, remaining: list[int], expected: int):
    next_floor = NearestFloorStrategy().pick(current, remaining)
    assert next_floor == expected


def test_direction_toggle():
    direction = Direction.UP
    assert direction.toggle() == Direction.DOWN


@pytest.mark.parametrize(
    ("direction", "current", "remaining", "expected"),
    [
        (Direction.UP, 12, [2, 9, 1, 32], 32),
        (Direction.DOWN, 12, [2, 9, 13, 32], 9),
        (Direction.UP, 12, [1, 2, 3, 4, 5], 5),
        (Direction.UP, 12, [12], 12),
    ],
)
def test_direction_aware_nearest_floor_strategy(
    direction: Direction,
    current: int,
    remaining: list[int],
    expected: int,
):
    next_floor = DirectionAwareNearestFloorStrategy(direction).pick(current, remaining)
    assert next_floor == expected
