# начинаем создание формальной спецификации
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
        pass

    # обмен значениями с соседней ячейкой; плохо то, что требуется доступ к внутреннему содержимому другой ячейки,
    # можно обойтись заменой содержимого этой ячейки и возвратом нового объекта класса Cell (???)
    def exchange_values(self, another_cell):
        pass


class GameBoard:

    def __init__(self):
        self._counters = {'moves': 0,
                          'score': 0}
        self._board = [] * BOARD_FIELDS
        for i in range(BOARD_FIELDS):
            self._board[i] = Cell()

    # проверяет, приводит ли ход к игровому событию
    def match_checker(self, first_cell, second_cell):
        pass

    # регистрирует ход
    def make_the_move(self, first_cell, second_cell):
        pass

    # заполняет опустевшие поля новыми значениями
    def fill_cells(self):
        pass


class GameMaster:

    def __init__(self):
        self._board = GameBoard()

    # проверяет пользовательский ввод
    def check_user_input(self, user_input):
        pass
