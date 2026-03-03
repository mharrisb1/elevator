import argparse
from collections.abc import Callable
from enum import StrEnum

from elevator.controller import Controller
from elevator.cost_model import FixedTimeCostModel
from elevator.strategy import (
    Direction,
    DirectionAwareNearestFloorStrategy,
    FifoStrategy,
    NearestFloorStrategy,
    Strategy,
)
from elevator.utils import parse_csv


class StrategyOption(StrEnum):
    FIFO = "fifo"
    NEAR = "nearest"
    DIRU = "dirup"
    DIRD = "dirdown"


STRATMAP: dict[StrategyOption, Callable[[], Strategy]] = {
    StrategyOption.FIFO: FifoStrategy,
    StrategyOption.NEAR: NearestFloorStrategy,
    StrategyOption.DIRU: lambda: DirectionAwareNearestFloorStrategy(Direction.UP),
    StrategyOption.DIRD: lambda: DirectionAwareNearestFloorStrategy(Direction.DOWN),
}


def run(argv: list[str] | None = None):
    parser = argparse.ArgumentParser()
    parser.add_argument("start", type=int, help="Starting floor")
    parser.add_argument("floors", type=str, help="Comma-separated floors to visit")
    parser.add_argument(
        "--strategy",
        type=StrategyOption,
        default=StrategyOption.FIFO,
        choices=list(StrategyOption),
        help="Dispatch strategy",
    )

    args = parser.parse_args(argv)

    strategy = STRATMAP[args.strategy]()
    cost_model = FixedTimeCostModel()

    start = args.start
    floors = parse_csv(args.floors)

    controller = Controller(strategy, cost_model)
    result = controller.dispatch(start, floors)

    print(result.total_cost, ",".join([str(f) for f in result.visited]))
