# Уточнение формальных спецификаций
import re
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

    def __eq__(self, other):
        if isinstance(other, Cell):
            return self._value == other._value
        return False

    def __str__(self):
        return self._value

    def __repr__(self):
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
                          'score': 0,
                          'failed_attempts': 0}
        self._board = [[Cell() for _ in range(COLUMNS)] for _ in range(ROWS)]  # переход на двумерный массив

    def __str__(self):
        str_board = ''
        str_board += '    ' + ' '.join(str(i) for i in range(COLUMNS)) + '\n'  # Индексы столбцов
        for i, row in enumerate(self._board):
            str_board+= f'{chr(i + 65)}   ' + ' '.join([str(cell) for cell in row]) + f'   {chr(i + 65)}\n'  # Индексы строк и ряды значений
        str_board += '    ' + ' '.join(str(i) for i in range(COLUMNS)) + '\n'  # Индексы столбцов
        return str_board

    # КОМАНДЫ
    # проверить всю доску на совпадения после автозаполнения очищенных ячеек
    def check_the_board(self):
        cells_to_collapse = set()
        # проверить по строкам
        for y in range(ROWS):
            for x in range(COLUMNS - 2):
                if self._board[y][x] == self._board[y][x + 1] == self._board[y][x + 2]:
                    cells_to_collapse.update(((y, x), (y, x + 1), (y, x + 2)))
        # проверить по столбцам
        for y in range(ROWS - 2):
            for x in range(COLUMNS):
                if self._board[y][x] == self._board[y + 1][x] == self._board[y + 2][x]:
                    cells_to_collapse.update(((y, x), (y + 1, x), (y + 2, x)))
        # очистить ячейки и начислить очки
        for y, x in cells_to_collapse:
            self._board[y][x] = EmptyCell()
        # начислить очки, но не начислять ходы, т.к. "оно само"
        self._counters['score'] += len(cells_to_collapse) * 10
        if len(cells_to_collapse) > 0:
            self._has_empty_cell = self.HAS_EMPTY_CELL

    # заполняет опустевшие поля новыми значениями
    def fill_cells(self):
        while self._has_empty_cell == self.HAS_EMPTY_CELL:
            count_empty_cells = 0
            for x in range(COLUMNS):
                if self._board[0][x].get_value() == ' ':
                    self._board[0][x] = Cell()

            for y in range(ROWS - 1):
                for x in range(COLUMNS):
                    if self._board[y + 1][x].get_value() == ' ':
                        self._swap_cells(y, x, y + 1, x)
                        count_empty_cells += 1

            if count_empty_cells == 0:
                self._has_empty_cell = self.HAS_NOT_EMPTY_CELL

    def remove_accidental_coincidences(self):
        old_score = self._counters['score']
        self.check_the_board()
        self.fill_cells()
        while old_score != self._counters['score']:
            self.check_the_board()
            self.fill_cells()
            old_score = self._counters['score']

    # метод, перекочевавший из класса Cell
    def _swap_cells(self, y1, x1, y2, x2):
        self._board[y1][x1], self._board[y2][x2] = self._board[y2][x2], self._board[y1][x1]

    # регистрирует ход
    def make_the_move(self, cell_addresses, indexes):
        y1, x1, y2, x2 = self.__get_indexes(cell_addresses)
        self._swap_cells(y1, x1, y2, x2)
        for y, x in indexes:
            self._board[y][x] = EmptyCell()
        self._counters['moves'] += 1
        self._counters['score'] += len(indexes) * 10
        self._has_empty_cell = self.HAS_EMPTY_CELL

    # увеличить счётчик неверных ходов
    def increase_failed_attempts_counter(self):
        self._counters['failed_attempts'] += 1

    # ЗАПРОСЫ
    # передать массив значений для отображения на экране
    def get_board(self):
        return self._board

    def get_counters(self):
        return self._counters['moves'], self._counters['score'], self._counters['failed_attempts']

    def failed_game(self):
        return self._counters['failed_attempts'] > 4

    # проверить, равны ли значения в указанных трёх ячейках
    def cells_are_equal(self, trio):
        [y1, x1], [y2, x2], [y3, x3] = trio
        return self._board[y1][x1] == self._board[y2][x2] == self._board[y3][x3]

    # проверяет, приводит ли ход к игровому событию
    def match_checker(self, cell_addresses):
        y1, x1, y2, x2 = self.__get_indexes(cell_addresses)
        self._swap_cells(y1, x1, y2, x2)
        indexes_to_check = self.__get_indexes_to_check(y1, x1) + self.__get_indexes_to_check(y2, x2)
        indexes_to_collapse = []
        for trio in indexes_to_check:
            if self.cells_are_equal(trio):
                indexes_to_collapse += trio
        self._swap_cells(y1, x1, y2, x2)
        if len(indexes_to_collapse) == 0:
            self._match_status = self.MATCH_NOT
            return []
        self._match_status = self.MATCH_OK
        return indexes_to_collapse

    # получить индекс массива из полученных координат
    def __get_indexes(self, coordinates):
        first, second = coordinates.split()
        y1 = ord(first[0]) - 65  # приведение 'A' к 0-му ряду и т. д.
        x1 = int(first[1:])
        y2 = ord(second[0]) - 65  # приведение 'A' к 0-му ряду и т. д.
        x2 = int(second[1:])
        return y1, x1, y2, x2

    # получить ряды индексов для проверки совпадений
    def __get_indexes_to_check(self, y, x):
        indexes = [[[y, x - 2], [y, x - 1], [y, x]],
                   [[y, x - 1], [y, x], [y, x + 1]],
                   [[y, x], [y, x + 1], [y, x + 2]],
                   [[y - 2, x], [y - 1, x], [y, x]],
                   [[y - 1, x], [y, x], [y + 1, x]],
                   [[y, x], [y + 1, x], [y + 2, x]]]
        return [trio for trio in indexes if all(0 <= pair[0] < ROWS and 0 <= pair[1] < COLUMNS for pair in trio)]

    def has_match(self):
        if  self._match_status == self.MATCH_NOT:
            self.increase_failed_attempts_counter()
        return self._match_status == self.MATCH_OK

    def has_empty_cell(self):
        return self._has_empty_cell == self.HAS_EMPTY_CELL

    # ЗАПРОСЫ СТАТУСОВ
    def get_match_status(self):
        return self._match_status

    def get_has_empty_cell_status(self):
        return self._has_empty_cell

class GameMaster:

    def __init__(self, last_move):
        self._last_move = last_move

    # получить доску для отображения
    # def get_board(self):
    #     return self._board.get_board()
    #
    # def get_counters(self):
    #     return self._board._counters

    # отображение доски в консоли
    def display_board(self, board):
        os.system('cls' if os.name == 'nt' else 'clear')  # Очистка окна консоли
        print(board)

    def display_count(self, moves, score, failed_attempts):
        print(f'Moves: {moves}. Score: {score}. Failed attempts: {failed_attempts} of 5')

    def game_over(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Очистка окна консоли
        print('Game Over')

    # проверяет пользовательский ввод
    def check_user_input(self, user_input):
        pattern = r'^[A-H]\d+\s[A-H]\d+$'
        if re.match(pattern, user_input):
            return user_input
        return 'exit'

    def handle_bad_coordinates(self):
        print('Coordinates aren\'t valid. Try again.')


if __name__ == '__main__':
    game_master = GameMaster(last_move='')
    game_board = GameBoard()
    while True:
        game_board.remove_accidental_coincidences()
        game_master.display_board(game_board)
        game_master.display_count(*game_board.get_counters())
        user_input = game_master.check_user_input(input('Enter coordinates: ').upper())
        if user_input == 'exit':
            break
        try:
            indexes = game_board.match_checker(user_input)
            if game_board.failed_game():
                game_master.game_over()
                break
            if game_board.has_match():
                game_board.make_the_move(user_input, indexes)
        except (ValueError, IndexError):
            game_master.handle_bad_coordinates()