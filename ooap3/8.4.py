# Уточнение формальных спецификаций
from typing import Final
import os
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
    HAS_NOT_EMPTY_CELL: Final = 0
    HAS_EMPTY_CELL: Final = 1

    def __init__(self):
        self._match_status = self.MATCH_NIL
        self._has_empty_cell = self.HAS_NOT_EMPTY_CELL
        self._counters = {'moves': 0,
                          'score': 0}
        self._board = [[Cell() for _ in range(COLUMNS)] for _ in range(ROWS)]  # переход на двумерный массив

    # ЗАПРОСЫ
    # передать массив значений для отображения на экране
    def get_board(self):
        return self._board

    # получить значения по индексам
    def get_values_by_indexes(self, indexes):
        return set(self._board[y][x].get_value() for y, x in indexes)

    # проверяет, приводит ли ход к игровому событию
    def match_checker(self, cell_addresses):
        y1, x1 = self.__get_indexes(cell_addresses[0])
        y2, x2 = self.__get_indexes(cell_addresses[1])
        self._swap_cells(y1, x1, y2, x2)
        indexes_to_check = self.__get_indexes_to_check(y1, x1) + self.__get_indexes_to_check(y2, x2)
        indexes_to_collapse = []
        for trio in indexes_to_check:
            values = self.get_values_by_indexes(trio)
            if len(values) == 1:
                indexes_to_collapse += trio
        self._swap_cells(y1, x1, y2, x2)
        if len(indexes_to_collapse) == 0:
            self._match_status = self.MATCH_NOT
            return []
        self._match_status = self.MATCH_OK
        return indexes_to_collapse

    # регистрирует ход
    def make_the_move(self, cell_addresses, indexes):
        y1, x1 = self.__get_indexes(cell_addresses[0])
        y2, x2 = self.__get_indexes(cell_addresses[1])
        self._swap_cells(y1, x1, y2, x2)
        for y, x  in indexes:
            self._board[y][x] = EmptyCell()
        self._counters['moves'] += 1
        self._counters['score'] += len(indexes) * 10
        self._has_empty_cell = self.HAS_EMPTY_CELL

    # КОМАНДЫ
    # заполняет опустевшие поля новыми значениями
    def fill_cells(self):
        while self._has_empty_cell == self.HAS_EMPTY_CELL:
            count_empty_cells = 0
            for y in range(ROWS - 1, 0, -1):
                for x in range(COLUMNS):
                    if self._board[y][x].get_value() == ' ':
                        count_empty_cells += 1
                        self._swap_cells(y, x, y - 1, x)

            for x in range(COLUMNS):
                if self._board[0][x].get_value() == ' ':
                    self._board[0][x] = Cell()
                    count_empty_cells -= 1

            if count_empty_cells == 0:
                self._has_empty_cell = self.HAS_NOT_EMPTY_CELL

    # получить индекс массива из полученных координат
    def __get_indexes(self, coordinates):
        y = ord(coordinates[0]) - 65  # приведение 'A' к 0-му ряду и т. д.
        x = int(coordinates[1:])
        return y, x

    # метод, перекочевавший из класса Cell
    def _swap_cells(self, y1, x1, y2, x2):
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

    # получить доску для отображения
    def get_board(self):
        return self._board.get_board()

    def get_counters(self):
        return self._board._counters

    # отображение доски в консоли
    def display_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        print('   ' + ' '.join(str(i) for i in range(COLUMNS)))  # Column indices
        print()
        for i, row in enumerate(self.get_board()):
            print(f'{chr(i+65)}   ' + ' '.join([cell.get_value() for cell in row]))  # Row indices and elements

    def display_count(self):
        counters = self.get_counters()
        print(f'Moves: {counters['moves']}. Score: {counters['score']}')

    # проверяет пользовательский ввод
    def check_user_input(self, user_input):
        pass


if __name__ == '__main__':
    game_master = GameMaster()
    last_command = ''
    while last_command != 'exit':
        game_master.display_board()
        game_master.display_count()
        cell_addresses = input('Enter coordinates: ').split()
        indexes = game_master._board.match_checker(cell_addresses)
        if game_master._board._match_status == GameBoard.MATCH_OK:
            game_master._board.make_the_move(cell_addresses, indexes)
        game_master._board.fill_cells()
