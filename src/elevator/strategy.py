from enum import Enum
from typing import Protocol


class Strategy(Protocol):
    def pick(self, current: int, remaining: list[int]) -> int:
        """
        Args:
            current: Current floor
            remaining: List of remaining floors to service
        """
        ...


class FifoStrategy(Strategy):
    def pick(self, current: int, remaining: list[int]) -> int:  # noqa: ARG002, PLR6301
        """Returns next floor in FIFO order"""
        return remaining[0]


class NearestFloorStrategy(Strategy):
    def pick(self, current: int, remaining: list[int]) -> int:  # noqa: PLR6301
        """Returns whichever floor is closest"""
        return min(remaining, key=lambda f: abs(f - current))


class Direction(Enum):
    UP = 1
    DOWN = -1

    def toggle(self) -> "Direction":
        """Opposite direction"""
        return Direction(self.value * -1)


class DirectionAwareNearestFloorStrategy(Strategy):
    def __init__(self, direction: Direction = Direction.UP) -> None:
        self._direction = direction

    def pick(self, current: int, remaining: list[int]) -> int:
        """
        Returns the closes floor in the direction already going.
        If no more floors are left in current direction then direction
        changed
        """
        ahead = [f for f in remaining if (f - current) * self._direction.value > 0]
        if not ahead:
            self._direction = self._direction.toggle()
            ahead = [f for f in remaining if (f - current) * self._direction.value > 0]

        if not ahead:
            return NearestFloorStrategy().pick(current, remaining)
        return NearestFloorStrategy().pick(current, ahead)
