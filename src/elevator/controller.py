from .cost_model import CostModel
from .elevator import Elevator
from .result import Result
from .strategy import Strategy


class Controller:
    def __init__(self, strategy: Strategy, cost_model: CostModel) -> None:
        """
        Args:
            strategy: Dispatch strategy
            cost_model: Cost model for calculating total cost
        """
        self._strategy = strategy
        self._cost_model = cost_model

    def dispatch(self, start: int, floors: list[int]) -> Result:
        """
        Dispatches floor requests

        Args:
            start: Initial floor
            floors: Floors requested to visit

        Returns:
            Run result with visited floors in order and total cost of travel

        Raises:
            ValueError: If any floors are not valid (not greater than zero)
        """
        elevator = Elevator(start)
        return elevator.run(floors, self._strategy, self._cost_model)
