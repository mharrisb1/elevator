import argparse
from enum import StrEnum

from elevator.controller import Controller
from elevator.cost_model import FixedTimeCostModel
from elevator.strategy import (
    Direction,
    DirectionAwareNearestFloorStrategy,
    FifoStrategy,
    NearestFloorStrategy,
)
from elevator.utils import parse_csv, validate_floor


class StrategyOption(StrEnum):
    FIFO = "fifo"
    NEAR = "nearest"
    DIRU = "dirup"
    DIRD = "dirdown"


STRATMAP = {
    StrategyOption.FIFO: FifoStrategy(),
    StrategyOption.NEAR: NearestFloorStrategy(),
    StrategyOption.DIRU: DirectionAwareNearestFloorStrategy(Direction.UP),
    StrategyOption.DIRD: DirectionAwareNearestFloorStrategy(Direction.DOWN),
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

    strategy = STRATMAP[args.strategy]
    cost_model = FixedTimeCostModel()

    start = validate_floor(args.start)
    floors = parse_csv(args.floors)

    controller = Controller(strategy, cost_model)
    result = controller.dispatch(start, floors)

    print(result.total_cost, result.visited)
