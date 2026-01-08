from dataclasses import dataclass, field
from enum import Enum
from random import choice
from typing import List, Tuple


SYMBOLS = ['A', 'B', 'C', 'D', 'E', 'F']


@dataclass(frozen=True)
class Element:
    symbol: str

    def __init__(self, c: str):
        object.__setattr__(self, 'symbol', c)


@dataclass(frozen=True)
class EmptyElement(Element):
    symbol: str

    def __init__(self):
        super().__init__('0')


class MatchDirection(Enum):
    Horizontal = 1
    Vertical = 2


@dataclass(frozen=True)
class Match:
    direction: MatchDirection
    row: int
    col: int
    length: int


@dataclass(frozen=True)
class Board:
    size: int
    cells: Tuple[Tuple[Element, ...], ...] = field(repr=False)


@dataclass(frozen=True)
class BoardState:
    board: Board
    score: int


def create_empty_board(size: int) -> 'Board':
        empty_row = tuple(EmptyElement() for _ in range(size))
        cells = tuple(empty_row for _ in range(size))
        return Board(size=size, cells=cells)


def pipe(self, func):
    return func(self)


def add_match_if_valid(matches: List[Match], row: int, col: int, length: int, direction: MatchDirection):
    if length >= 3:
        matches.append(Match(direction, row, col, length))


def find_matches(board: 'Board') -> List[Match]:
    size = board.size
    matches: List[Match] = []

    # Горизонтальные комбинации
    for row in range(size):
        start_col = 0
        for col in range(1, size):
            # Пропускаем пустые ячейки в начале строки
            if EmptyElement.symbol == board.cells[row][start_col].symbol:
                start_col = col
                continue
            # Если текущая ячейка пустая, обрываем текущую последовательность
            if EmptyElement.symbol == board.cells[row][col].symbol:
                add_match_if_valid(matches, row, start_col, col - start_col, MatchDirection.Horizontal)
                start_col = col + 1
                continue
            # Проверяем совпадение символов для непустых ячеек
            if board.cells[row][col].symbol != board.cells[row][start_col].symbol:
                add_match_if_valid(matches, row, start_col, col - start_col, MatchDirection.Horizontal)
                start_col = col
            elif col == size - 1:
                add_match_if_valid(matches, row, start_col, col - start_col + 1, MatchDirection.Horizontal)

    # Вертикальные комбинации
    for col in range(size):
        start_row = 0
        for row in range(1, size):
            # Пропускаем пустые ячейки в начале столбца
            if EmptyElement.symbol == board.cells[start_row][col].symbol:
                start_row = row
                continue
            # Если текущая ячейка пустая, обрываем текущую последовательность
            if EmptyElement.symbol == board.cells[row][col].symbol:
                add_match_if_valid(matches, start_row, col, row - start_row, MatchDirection.Vertical)
                start_row = row + 1
                continue
            # Проверяем совпадение символов для непустых ячеек
            if board.cells[row][col].symbol != board.cells[start_row][col].symbol:
                add_match_if_valid(matches, start_row, col, row - start_row, MatchDirection.Vertical)
                start_row = row
            elif row == size - 1:
                add_match_if_valid(matches, start_row, col, row - start_row + 1, MatchDirection.Vertical)

    return matches


def remove_matches(current_state: 'BoardState', matches: List[Match]) -> 'BoardState':
    if not matches:
        return current_state

    marked_cells = mark_cells_for_removal(current_state.board, matches)
    gravity_applied_cells = apply_gravity(marked_cells, current_state.board.size)
    removed_count = sum(m.length for m in matches)
    new_score = current_state.score + calculate_score(removed_count)

    new_board = Board(size=current_state.board.size, cells=gravity_applied_cells)
    return BoardState(new_board, new_score)


def mark_cells_for_removal(board: 'Board', matches: List[Match]) -> Tuple[Tuple[Element, ...], ...]:
    new_cells = [list(row) for row in board.cells]

    for match in matches:
        for i in range(match.length):
            row = match.row if match.direction == MatchDirection.Horizontal else match.row + i
            col = match.col + i if match.direction == MatchDirection.Horizontal else match.col
            new_cells[row][col] = EmptyElement()

    return tuple(tuple(row) for row in new_cells)


def apply_gravity(cells: Tuple[Tuple[Element, ...], ...], size: int) -> Tuple[Tuple[Element, ...], ...]:
    new_cells = [[EmptyElement() for _ in range(size)] for _ in range(size)]

    for col in range(size):
        new_row = size - 1
        for row in range(size - 1, -1, -1):
            if EmptyElement.symbol != cells[row][col].symbol:
                new_cells[new_row][col] = cells[row][col]
                new_row -= 1

    return tuple(tuple(row) for row in new_cells)


def calculate_score(removed_count: int) -> int:
    # Базовая система подсчёта очков: 10 за каждый элемент
    return removed_count * 10


def fill_empty_spaces(current_state: 'BoardState') -> 'BoardState':
    if current_state.board.cells is None:
        return current_state

    rows = [list(row) for row in current_state.board.cells]
    size = current_state.board.size

    for row in range(size):
        for col in range(size):
            if EmptyElement.symbol == rows[row][col].symbol:
                rows[row][col] = Element(choice(SYMBOLS))

    new_cells = tuple(tuple(row) for row in rows)

    new_board = Board(size=size, cells=new_cells)
    return BoardState(new_board, current_state.score)




def process_cascade(current_state: 'BoardState') -> 'BoardState':
    # debug_mode = True
    return current_state if not find_matches(current_state.board) else (current_state
                                                                         .pipe(lambda bs: remove_matches(bs, find_matches(bs.board)))
                                                                         .pipe(fill_empty_spaces)
                                                                         .pipe(process_cascade))