from dataclasses import dataclass
from enum import Enum
from typing import List, Tuple
from random import random

from fp5.Board import Board, BoardState
from fp5.Element import Element

SYMBOLS = ['A', 'B', 'C', 'D', 'E', 'F']

class MatchDirection(Enum):
    Horizontal = 1
    Vertical = 2


@dataclass(frozen=True)
class Match:
    direction: MatchDirection
    row: int
    col: int
    length: int


def add_match_if_valid(matches: List[Match], row: int, col: int, length: int, direction: MatchDirection):
    # Учитываем только комбинации из 3 и более элементов
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

def remove_matches(current_state: 'BoardState', matches: List[Match]) -> 'BoardState':
    if not matches:
        return current_state

    # Шаг 1: Помечаем ячейки для удаления
    marked_cells = mark_cells_for_removal(current_state.board, matches)

    # Шаг 2: Применяем гравитацию
    gravity_applied_cells = apply_gravity(marked_cells, current_state.board.size)

    # Шаг 3: Подсчитываем очки
    removed_count = sum(m.length for m in matches)
    new_score = current_state.score + calculate_score(removed_count)

    # Возвращаем новое состояние с обновлённой доской и счётом
    new_board = Board(size=current_state.board.size, cells=gravity_applied_cells)
    return BoardState(new_board, new_score)

def mark_cells_for_removal(board: 'Board', matches: List[Match]) -> Tuple[Tuple[Element, ...], ...]:
    # Создаём копию cells как список списков для удобства изменения
    rows = [list(row) for row in board.cells]

    for match in matches:
        for i in range(match.length):
            row = match.row if match.direction == MatchDirection.Horizontal else match.row + i
            col = match.col + i if match.direction == MatchDirection.Horizontal else match.col
            # Помечаем ячейку пустым элементом
            rows[row][col] = Element(Element.EMPTY)

    # Преобразуем обратно в кортеж кортежей (иммутабельная структура)
    return tuple(tuple(row) for row in rows)

def apply_gravity(cells: Tuple[Tuple[Element, ...], ...], size: int) -> Tuple[Tuple[Element, ...], ...]:
    # Создаём пустую доску
    new_cells = [[Element(Element.EMPTY) for _ in range(size)] for _ in range(size)]

    for col in range(size):
        new_row = size - 1
        for row in range(size - 1, -1, -1):
            if cells[row][col].symbol != Element.EMPTY:
                new_cells[new_row][col] = cells[row][col]
                new_row -= 1

    # Преобразуем в кортеж кортежей
    return tuple(tuple(row) for row in new_cells)


def calculate_score(removed_count: int) -> int:
    # Базовая система подсчёта очков: 10 за каждый элемент
    return removed_count * 10


def fill_empty_spaces(current_state: 'BoardState') -> 'BoardState':
    if current_state.board.cells is None:
        return current_state

    # Создаём изменяемую копию доски
    rows = [list(row) for row in current_state.board.cells]
    size = current_state.board.size

    for row in range(size):
        for col in range(size):
            if rows[row][col].symbol == Element.EMPTY:
                rows[row][col] = Element(random(SYMBOLS))

    # Преобразуем обратно в кортеж кортежей (иммутабельная структура)
    new_cells = tuple(tuple(row) for row in rows)

    new_board = Board(size=size, cells=new_cells)
    return BoardState(new_board, current_state.score)


def process_cascade(current_state: 'BoardState') -> 'BoardState':

    matches = find_matches(current_state.board)
    if not matches:
        return current_state
    # Удаляем совпадения и применяем гравитацию
    state_after_removal = remove_matches(current_state, matches)
    # Заполняем пустые ячейки новыми символами
    state_after_filling = fill_empty_spaces(state_after_removal)
    return process_cascade(state_after_filling)
