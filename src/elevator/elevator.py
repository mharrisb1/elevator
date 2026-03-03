from .cost_model import CostModel
from .result import Result
from .strategy import Strategy
from .utils import validate_floor


class Elevator:
    def __init__(self, floor: int) -> None:
        """
        Args:
            floor: Starting floor

        Raises:
            ValueError: If floor is not greater than zero
        """
        self._floor = validate_floor(floor)

    def run(
        self,
        floors: list[int],
        strategy: Strategy,
        cost_model: CostModel,
    ) -> Result:
        """
        Args:
            floors: Requested floors to visit
            strategy: Dispatch strategy
            cost_model: Cost model for calculating total cost

        Returns:
            Result of floors visited in order visited with total cost
        """
        visited = [self._floor]
        total_cost = 0
        current = self._floor
        remaining = floors.copy()

        while remaining:
            next_floor = strategy.pick(current, remaining)
            remaining.remove(next_floor)
            if current == next_floor:
                continue

            total_cost += cost_model.cost(current, next_floor)
            current = next_floor
            visited.append(current)

        return Result(total_cost=total_cost, visited=visited)
