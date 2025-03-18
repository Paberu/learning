# Уточнение формальных спецификаций
from typing import Final
from enum import Enum
from random import choice

COLUMNS = 8
ROWS = 8
BOARD_FIELDS = COLUMNS * ROWS


class CellValue(Enum):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'


class Cell:

    def __init__(self):
        self._value = choice(list(CellValue))

    # возвращает хранимое значение для отображения на экране
    def get_value(self):
        return self._value.name


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
        self._board = []
        for i in range(BOARD_FIELDS):
            self._board.append(Cell())

    # ЗАПРОСЫ
    # получить значения по индексам
    def get_values_by_indexes(self, indexes):
        return set(self._board[i].get_value() for i in indexes if i < len(self._board))

    # проверяет, приводит ли ход к игровому событию
    def match_checker(self, cell_addresses):
        i, j = self._exchange_cells(cell_addresses)
        indexes_to_check = self.__get_indexes_to_check(i) + self.__get_indexes_to_check(j)
        filtered_indexes = [inner_group for inner_group in indexes_to_check if all(x >= 0 for x in inner_group)]
        indexes_to_collapse = []
        for inner_group in filtered_indexes:
            values = self.get_values_by_indexes(inner_group)
            if len(values) == 1:
                indexes_to_collapse += inner_group
        self._exchange_cells(cell_addresses)
        if len(indexes_to_collapse) == 0:
            self._match_status = self.MATCH_NOT
            return []
        self._match_status = self.MATCH_OK
        return indexes_to_collapse

    # регистрирует ход
    def make_the_move(self, cell_addresses, indexes):
        i, j = self._exchange_cells(cell_addresses)
        for index in indexes:
            self._board[index] = EmptyCell()
        self._counters['moves'] += 1
        self._counters['score'] += len(indexes) * 10

    # заполняет опустевшие поля новыми значениями
    def fill_cells(self):
        pass

    # КОМАНДЫ
    # метод, перекочевавший из класса Cell
    def _exchange_cells(self, cell_addresses):
        i = self.__get_index(cell_addresses[0][0], cell_addresses[0][1:])
        j = self.__get_index(cell_addresses[1][0], cell_addresses[1][1:])
        self._board[i], self._board[j] = self._board[j], self._board[i]
        return i, j

    # получить индекс массива из полученных координат
    def __get_index(self, y, x):
        row_y = ord(y) - 65  # на случай первого ряда, т.е. нулевого смещения, привожу А к 0, а дальше по схеме
        return row_y * COLUMNS + int(x)

    # получить ряды индексов для проверки совпадений
    def __get_indexes_by_step(self, index, step):
        return [[index - 2 * step, index - step, index],
                [index - step, index, index + step],
                [index, index + step, index + 2 * step]]

    # получить индексы всех ячеек, подлежащих проверке
    def __get_indexes_to_check(self, index):
        return self.__get_indexes_by_step(index, 1) + self.__get_indexes_by_step(index, COLUMNS)

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
            print(game_board._board[row*ROWS+column].get_value(), end=' ')
        print()
    cell_addresses = input('Enter coordinates: ').split()
    indexes = game_board.match_checker(cell_addresses)
    if game_board._match_status == GameBoard.MATCH_OK:
        game_board.make_the_move(cell_addresses, indexes)

    for row in range(ROWS):
        for column in range(COLUMNS):
            print(game_board._board[row*ROWS+column].get_value(), end=' ')
        print()