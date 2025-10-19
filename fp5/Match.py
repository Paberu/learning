from dataclasses import dataclass
from enum import Enum
from typing import List

from fp5.Element import Element


class MatchDirection(Enum):
    Horizontal = 1
    Vertical = 2


@dataclass(frozen=True)
class Match:
    direction: MatchDirection
    row: int
    col: int
    length: int

matches: List[Match] = []

def add_match_if_valid(matches: List[Match], row: int, col: int, length: int, direction: MatchDirection):
    # Учитываем только комбинации из 3 и более элементов
    if length >= 3:
        matches.append(Match(direction, row, col, length))

def find_matches(board: 'Board') -> List[Match]:
    size = board.size

    # Горизонтальные комбинации
    for row in range(size):
        start_col = 0
        for col in range(1, size):
            # Пропускаем пустые ячейки в начале строки
            if board.cells[row][start_col].symbol == Element.EMPTY:
                start_col = col
                continue
            # Если текущая ячейка пустая, обрываем текущую последовательность
            if board.cells[row][col].symbol == Element.EMPTY:
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
            if board.cells[start_row][col].symbol == Element.EMPTY:
                start_row = row
                continue
            # Если текущая ячейка пустая, обрываем текущую последовательность
            if board.cells[row][col].symbol == Element.EMPTY:
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