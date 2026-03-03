from typing import NamedTuple


class Result(NamedTuple):
    total_cost: int
    visited: list[int]
