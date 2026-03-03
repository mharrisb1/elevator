from typing import Protocol


class CostModel(Protocol):
    def cost(self, from_floor: int, to_floor: int) -> int:
        """
        Args:
            from_floor: Source floor
            to_floor: Destination floor

        Returns:
            Cost from going from source to dest
        """
        ...


class FixedTimeCostModel(CostModel):
    def __init__(self, single_floor_travel_time: int = 10) -> None:
        self._single_floor_travel_time = single_floor_travel_time

    def cost(self, from_floor: int, to_floor: int) -> int:
        """Fixed travel time between floors with no additional costs"""
        return abs(to_floor - from_floor) * self._single_floor_travel_time
