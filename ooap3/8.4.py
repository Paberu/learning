# Уточнение формальных спецификаций
from typing import Final
from enum import Enum
from random import choice

COLUMNS: Final = 8
ROWS: Final = 8
BOARD_FIELDS: Final = COLUMNS * ROWS
CELL_VALUES: Final = ['A', 'B', 'C', 'D', 'E']


class Cell:

    def __init__(self):
        self._value = choice(CELL_VALUES)

    # возвращает хранимое значение для отображения на экране
    def get_value(self):
        return self._value


class EmptyCell(Cell):

    def __init__(self):
        self._value = ' '


class GameBoard:

    MATCH_NIL: Final = 0
    MATCH_OK: Final = 1
    MATCH_NOT: Final = 2

    def __init__(self):
        self._match_status = self.MATCH_NIL
        self._counters = {'moves': 0,
                          'score': 0}
        self._board = [[Cell() for _ in range(COLUMNS)] for _ in range(ROWS)]  # переход на двумерный массив

    # ЗАПРОСЫ
    # получить значения по индексам
    def get_values_by_indexes(self, indexes):
        return set(self._board[y][x].get_value() for y, x in indexes)

    # проверяет, приводит ли ход к игровому событию
    def match_checker(self, cell_addresses):
        y1, x1 = self.__get_indexes(cell_addresses[0])
        y2, x2 = self.__get_indexes(cell_addresses[1])
        self._exchange_cells(y1, x1, y2, x2)
        indexes_to_check = self.__get_indexes_to_check(y1, x1) + self.__get_indexes_to_check(y2, x2)
        indexes_to_collapse = []
        for trio in indexes_to_check:
            values = self.get_values_by_indexes(trio)
            if len(values) == 1:
                indexes_to_collapse += trio
        self._exchange_cells(y1, x1, y2, x2)
        if len(indexes_to_collapse) == 0:
            self._match_status = self.MATCH_NOT
            return []
        self._match_status = self.MATCH_OK
        return indexes_to_collapse

    # регистрирует ход
    def make_the_move(self, cell_addresses, indexes):
        y1, x1 = self.__get_indexes(cell_addresses[0])
        y2, x2 = self.__get_indexes(cell_addresses[1])
        self._exchange_cells(y1, x1, y2, x2)
        for y, x  in indexes:
            self._board[y][x] = EmptyCell()
        self._counters['moves'] += 1
        self._counters['score'] += len(indexes) * 10

    # заполняет опустевшие поля новыми значениями
    def fill_cells(self):
        pass

    # КОМАНДЫ
    # получить индекс массива из полученных координат
    def __get_indexes(self, coordinates):
        y = ord(coordinates[0]) - 65  # приведение 'A' к 0-му ряду и т. д.
        x = int(coordinates[1:])
        return y, x

    # метод, перекочевавший из класса Cell
    def _exchange_cells(self, y1, x1, y2, x2):
        self._board[y1][x1], self._board[y2][x2] = self._board[y2][x2], self._board[y1][x1]

    # получить ряды индексов для проверки совпадений
    def __get_indexes_to_check(self, y, x):
        indexes = [[[y, x - 2], [y, x - 1], [y, x]],
                   [[y, x - 1], [y, x], [y, x + 1]],
                   [[y, x], [y, x + 1], [y, x + 2]],
                   [[y - 2, x], [y - 1, x], [y, x]],
                   [[y - 1, x], [y, x], [y + 1, x]],
                   [[y, x], [y + 1, x], [y + 2, x]]]
        return [trio for trio in indexes if all(0 <= pair[0] < ROWS and 0 <= pair[1] < COLUMNS for pair in trio)]


class GameMaster:

    def __init__(self):
        self._board = GameBoard()

    # проверяет пользовательский ввод
    def check_user_input(self, user_input):
        pass


if __name__ == '__main__':
    game_board = GameBoard()
    for row in range(ROWS):
        for column in range(COLUMNS):
            print(game_board._board[row][column].get_value(), end=' ')
        print()
    cell_addresses = input('Enter coordinates: ').split()
    indexes = game_board.match_checker(cell_addresses)
    if game_board._match_status == GameBoard.MATCH_OK:
        game_board.make_the_move(cell_addresses, indexes)

    for row in range(ROWS):
        for column in range(COLUMNS):
            print(game_board._board[row][column].get_value(), end=' ')
        print()