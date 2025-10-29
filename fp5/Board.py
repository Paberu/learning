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

    def pipe(self, func):
        return func(self)

    def draw(self, ask=False):
        print("  0 1 2 3 4 5 6 7")
        for i in range(8):
            print(f"{i} ", end='')
            for j in range(8):
                print(self.board.cells[i][j].symbol, end=' ')
            print()
        print()
        if ask:
            input('debug mode on, next step on any key...')
