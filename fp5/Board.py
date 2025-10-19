from dataclasses import dataclass, field
from typing import Tuple

from fp5.Element import Element


@dataclass(frozen=True)
class Board:
    size: int
    cells: Tuple[Tuple[Element, ...], ...] = field(repr=False)

    @staticmethod
    def create_empty(size: int) -> 'Board':
        empty_row = tuple(Element.empty() for _ in range(size))
        cells = tuple(empty_row for _ in range(size))
        return Board(size=size, cells=cells)


@dataclass(frozen=True)
class BoardState:
    board: Board
    score: int

