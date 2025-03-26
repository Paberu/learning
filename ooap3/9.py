import re
from typing import Final
import os
from random import choice

COLUMNS: Final = 8
ROWS: Final = 8
BOARD_FIELDS: Final = COLUMNS * ROWS
CELL_VALUES: Final = ['A', 'B', 'C', 'D', 'E']
FAILED_ATTEMPTS: Final = 5


class Cell:
    """ Класс игровой ячейки, хранит одно из значений из массива возможных значений CELL_VALUE.

    В рамках консольного приложения содержит один атрибут _value и ряд служебных методов для отображения,
    сравнения и сериализации на случай необходимости.
    """

    def __init__(self):
        self._value = choice(CELL_VALUES)

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
    """ Дочерний класс игровой ячейки, переопределяет содержимое атрибута на значение, эквивалентное пустой ячейке.
    Предназначен для придания ячейке статуса пустой.
    """

    def __init__(self):
        self._value = ' '


class GameBoard:
    """ Класс игровой доски. Содержит статусы завершения важных операций, игровые счётчики и ячейки игрового поля,
    взаимодействие с которыми и является игрой.

    Три значения для статуса проверки хода (MATCH_NIL - начало игры, ни одного хода не было сделано, MATCH_OK - ход
    привёл к игровому событию (как минимум одно совпадение "три в ряд"), MATCH_NOT - ход не привёл к игровому событию,
    никаких изменений в состояние игрового поля, игрок получает штрафное очко за неверный ход).

    Два значения для статуса проверки доски на наличие пустых ячеек (HAS_NOT_EMPTY_CELL - нормальное состояние доски
    в начале игры и по завершению устранения всех случайных совпадений, HAS_EMPTY_CELL - есть пустые ячейки после
    удаления совпадений (как случайных, так и в результате хода игрока)).
    """

    MATCH_NIL: Final = 0
    MATCH_OK: Final = 1
    MATCH_NOT: Final = 2
    HAS_NOT_EMPTY_CELL: Final = 0
    HAS_EMPTY_CELL: Final = 1

    def __init__(self):
        """ Конструктор проводит инициализацию атрибутов. К сожалению, в Python атрибуты задаются и инициализируются
        в момент вызова конструктора.

        Два флага (статуса) выполнения методов match_checker() и check_the_board().

        Три счётчика для учёта прогресса игрока: ходы, общий счёт и провальные попытки.

        Двумерный массив, содержащий необходимое количество ячеек Cell.
        """

        self._match_status = self.MATCH_NIL
        self._has_empty_cell = self.HAS_NOT_EMPTY_CELL
        self._counters = {'moves': 0,
                          'score': 0,
                          'failed_attempts': 0}
        self._board = [[Cell() for _ in range(COLUMNS)] for _ in range(ROWS)]  # переход на двумерный массив

    def __str__(self):
        """ Перевод содержимого в строковое выражение для передачи для вывода в консоль

        :return: Строка для вывода содержимого доски со всеми индексами и необходимым переносами.
        """
        str_board = '    ' + ' '.join(str(i) for i in range(COLUMNS)) + '\n'  # Индексы столбцов
        str_board += '\n'
        for i, row in enumerate(self._board):
            str_board+= f'{chr(i + 65)}   ' + ' '.join([str(cell) for cell in row]) + f'   {chr(i + 65)}\n'  # Индексы строк и ряды значений
        str_board += '\n'
        str_board += '    ' + ' '.join(str(i) for i in range(COLUMNS)) + '\n'  # Индексы столбцов
        return str_board

    # КОМАНДЫ
    def check_the_board(self):
        """ Проверяет доску на совпадения после автозаполнения очищенных ячеек

        :return: Ничего, так как относится к категории команд
        """
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
        # начислить очки, но не начислять ходы, так как "оно само"
        self._counters['score'] += len(cells_to_collapse) * 10
        if len(cells_to_collapse) > 0:
            self._has_empty_cell = self.HAS_EMPTY_CELL

    def fill_cells(self):
        """ Заполняет опустевшие поля новыми значениями.

        :return: Ничего, так как относится к категории команд
        """
        while self._has_empty_cell == self.HAS_EMPTY_CELL:
            count_empty_cells = 0
            for x in range(COLUMNS):
                if self._board[0][x].get_value() == ' ':
                    self._board[0][x] = Cell()

            for y in range(ROWS - 1):
                for x in range(COLUMNS):
                    if self._board[y + 1][x].get_value() == ' ':
                        self._swap_cells( (y, x, y + 1, x) )
                        count_empty_cells += 1

            if count_empty_cells == 0:
                self._has_empty_cell = self.HAS_NOT_EMPTY_CELL

    def remove_accidental_coincidences(self):
        """ Удаляет случайные совпадения, пока не появится возможность для хода

        :return: Ничего, так как относится к категории команд
        """
        old_score = self._counters['score']
        self.check_the_board()
        self.fill_cells()
        while old_score != self._counters['score']:
            self.check_the_board()
            self.fill_cells()
            old_score = self._counters['score']

    def _swap_cells(self, coordinates_to_swap):
        """ Меняет местами две ячейки, указанные пользователем.

        :param coordinates_to_swap: Список из четырёх значений - координат обеих ячеек.
        :return: Ничего, так как относится к категории команд
        """
        y1, x1, y2, x2 = coordinates_to_swap
        self._board[y1][x1], self._board[y2][x2] = self._board[y2][x2], self._board[y1][x1]

    def make_the_move(self, coordinates_to_swap, indexes):
        """ Совершает ход и учитывает его результаты

        :param coordinates_to_swap: Список из четырёх значений - координат обеих ячеек.
        :param indexes: Список из пар значений - координат ячеек, подлежащих очистке.
        :return: Ничего, так как относится к категории команд
        """
        self._swap_cells(coordinates_to_swap)
        for y, x in indexes:
            self._board[y][x] = EmptyCell()
        self._counters['moves'] += 1
        self._counters['score'] += len(indexes) * 10
        self._has_empty_cell = self.HAS_EMPTY_CELL

    def increase_failed_attempts_counter(self):
        """ Увеличить счётчик неверных ходов

        :return: Ничего, так как относится к категории команд
        """
        self._counters['failed_attempts'] += 1

    # ЗАПРОСЫ
    def get_board(self):
        """ Передать строковое представление доски для отображения на экране

        :return: Строка для вывода содержимого доски со всеми индексами и необходимым переносами.
        """
        return self._board

    def get_counters(self):
        """ Передать кортеж счётчиков для отображения на экране

        :return: Кортеж из трёх числовых значений
        """
        return self._counters['moves'], self._counters['score'], self._counters['failed_attempts']

    def failed_game(self):
        """ Проверка состояния игры на достижения счётчиком ошибочных ходов критического значения.

        :return: Булево значение - превысил ли счётчик ошибок допустимое количество ошибочных ходов.
        """
        return self._counters['failed_attempts'] >= FAILED_ATTEMPTS

    def cells_are_equal(self, trio):
        """ Проверяет, равны ли значения в указанных трёх ячейках

        :param trio: Кортеж из трёх пар значений, соответствующих координатам трёх ячеек.
        :return: Булево значение - проверку равенства значений трёх ячеек друг другу.
        """
        [y1, x1], [y2, x2], [y3, x3] = trio
        return self._board[y1][x1] == self._board[y2][x2] == self._board[y3][x3]

    def match_checker(self, coordinates_to_swap):
        """ Проверяет, приводит ли ход к игровому событию. По завершению работы функции выставляет статус результата
        выполнения: произошло совпадение (MATCH_OK) или нет (MATCH_NOT).

        :param coordinates_to_swap: Список из четырёх значений - координат обеих ячеек.
        :return: Список из пар значений - координат ячеек, подлежащих очистке.
        """
        self._swap_cells(coordinates_to_swap)
        y1, x1, y2, x2 = coordinates_to_swap
        indexes_to_check = self.__get_indexes_to_check(y1, x1) + self.__get_indexes_to_check(y2, x2)
        indexes_to_collapse = []
        for trio in indexes_to_check:
            if self.cells_are_equal(trio):
                indexes_to_collapse += trio
        self._swap_cells(coordinates_to_swap)
        if len(indexes_to_collapse) == 0:
            self._match_status = self.MATCH_NOT
            return []
        self._match_status = self.MATCH_OK
        return indexes_to_collapse

    def __get_indexes(self, coordinates):
        """ Преобразовывает пользовательский ввод в список из индексов.

        :param coordinates: Строковое значение координат в удобном для пользователя виде (e.g. 'B5 C5').
        :return: Список из четырёх целочисленных значений - координат двух ячеек.
        """
        first, second = coordinates.split()
        y1 = ord(first[0]) - 65  # приведение 'A' к 0-му ряду и т. д.
        x1 = int(first[1:])
        y2 = ord(second[0]) - 65  # приведение 'A' к 0-му ряду и т. д.
        x2 = int(second[1:])
        return y1, x1, y2, x2

    def __get_indexes_to_check(self, y, x):
        """ Подставляет значения y и x в заранее подготовленный список, представляющий собой набор списков вида "три
        пары целочисленных значений", являющиеся координатами трёх соседних по горизонтали или вертикали ячеек.

        Проверка значений в данном списке заключается в том, что ни один из индексов на должен выходить за пределы
        допустимых значений. Допустимые значения - это физические параметры доски: строковые индексы могут быть не ниже
        0 и не выше возможного количества строк, а индексы столбцов - не ниже 0 и не выше возможного количества
        столбцов.

        В случае выхода хотя бы одной координаты хотя бы в одной из трёх пар весь список из трёх пар не подлежит
        включению в итоговый, возвращаемый список.

        :param y: Координата y ячейки (номер строки).
        :param x: Координата x ячейки (номер столбца).
        :return: Список из всех возможных допустимых координат ячеек, подлежащих сравнению между собой.
        """
        indexes = [[[y, x - 2], [y, x - 1], [y, x]],
                   [[y, x - 1], [y, x], [y, x + 1]],
                   [[y, x], [y, x + 1], [y, x + 2]],
                   [[y - 2, x], [y - 1, x], [y, x]],
                   [[y - 1, x], [y, x], [y + 1, x]],
                   [[y, x], [y + 1, x], [y + 2, x]]]
        return [trio for trio in indexes if all(0 <= pair[0] < ROWS and 0 <= pair[1] < COLUMNS for pair in trio)]

    def has_match(self):
        """ Проверяет, было ли совпадение, и штрафует, если такового не было.

        :return: Булево значение - результат проверки верности хода.
        """
        if  self._match_status == self.MATCH_NOT:
            self.increase_failed_attempts_counter()
        return self._match_status == self.MATCH_OK

    def has_empty_cell(self):
        """ Проверяет значение статуса "остались пустые ячейки".

        :return: Булево значение - наличие пустых ячеек.
        """
        return self._has_empty_cell == self.HAS_EMPTY_CELL

    # ЗАПРОСЫ СТАТУСОВ
    def get_match_status(self):
        return self._match_status

    def get_has_empty_cell_status(self):
        return self._has_empty_cell

class GameMaster:
    """ Класс управления игрой. Содержит статус проверки пользовательского ввода и значение последнего хода. Отвечает
    за вывод игрового процесса на экран.

    Четыре значения для статуса проверки пользовательского ввода (USER_INPUT_NIL - начало игры, ни одного хода не было
    сделано, USER_INPUT_COORDINATES - пользователь ввёл верные координаты, USER_INPUT_EXIT - пользователь выбрал выйти
    из игры, USER_INPUT_FAILED- пользователь выполнил неверный ввод.
    """
    USER_INPUT_NIL: Final = 0
    USER_INPUT_COORDINATES: Final = 1
    USER_INPUT_COORDINATES_WRONG: Final = 2
    USER_INPUT_EXIT: Final = 3
    USER_INPUT_FAILED: Final = 4

    def __init__(self):
        """ Создаёт и инициализирует два атрибута - запись последнего хода и статус проверки пользовательского хода.
        """
        self._last_move = ''
        self._user_input_status = self.USER_INPUT_NIL

    # КОМАНДЫ
    def display_board(self, board):
        """ Выводит на экран доски.

        :param board: Строковок представление доски.
        :return: Ничего. Это функция вывода на экран.
        """
        os.system('cls' if os.name == 'nt' else 'clear')  # Очистка окна консоли
        if self._user_input_status == self.USER_INPUT_COORDINATES_WRONG:
            self.handle_bad_coordinates()
        print(board)

    def display_count(self, moves, score, failed_attempts):
        """ Выводит на экран прогресса игры.

        :param moves: Количество ходов.
        :param score: Общий счёт игры.
        :param failed_attempts: Количество неверных вводов.
        :return: Ничего. Это функция вывода на экран.
        """
        print(f'Moves: {moves}. Score: {score}. Failed attempts: {failed_attempts} of 5')

    def game_over(self):
        """ Выводит на экран информацию об окончании игры.

        :return: Ничего. Это функция вывода на экран.
        """
        os.system('cls' if os.name == 'nt' else 'clear')  # Очистка окна консоли
        print('Game Over')

    def handle_bad_coordinates(self):
        """ Выводит на экран сообщение о неверных координатах

        :return: Ничего. Это функция вывода на экран.
        """
        print('Coordinates aren\'t valid. Try again.')

    def check_user_input(self, user_input):
        """ Проверяет пользовательский ввод.

        :param user_input: Строка с пользовательским вводом.
        :return: Возвращает кортеж полученных значений (или пустой кортеж, если ввели неверные координаты).
        """
        pattern = r'^[A-H]\d+\s[A-H]\d+$'
        if re.match(pattern, user_input):
            y1, x1, y2, x2 = self.get_coordinates(user_input)
            if abs(y1 - y2) == 1 and x1 == x2 or abs(x1 - x2) == 1 and y1 == y2:
                self._user_input_status = self.USER_INPUT_COORDINATES
                return y1, x1, y2, x2
            self._user_input_status = self.USER_INPUT_COORDINATES_WRONG
            return set()
        if user_input == 'EXIT':
            self._user_input_status = self.USER_INPUT_EXIT
            return set()
        self._user_input_status = self.USER_INPUT_FAILED
        return set()

    def get_coordinates(self, user_input):
        """ Получает координаты в формате пользовательского ввода (проверка проведена заранее методом check_user_input)
        e.g. 'A5 B5'. Приводит их к виду четырёх целочисленных координат. В случае, если пользователь указал координаты
        в правильном формате, но нарушил правило соседних ячеек, возвращается исходное значение.

        :param user_input: Строка с пользовательским вводом.
        :return: Возвращает четыре координаты: первые две для первой ячейки, вторые - для второй.
        """
        first, second = user_input.split()
        return ord(first[0]) - 65, int(first[1:]), ord(second[0]) - 65, int(second[1:])

    def validate_coordinates(self, y1, x1, y2, x2):
        """ Проверяет координаты на соответствие трём условиям: ячейки должны быть соседними, горизонтальные координаты
        должны быть в пределах [0; ROWS), вертикальные координаты должны быть в пределах [0; COLUMNS).

        :param y1: Координата
        :param x1:
        :param y2:
        :param x2:
        :return:
        """
        if_neighbor_cells = abs(y1 - y2) == 1 and x1 == x2 or abs(x1 - x2) == 1 and y1 == y2
        if_y_in_borders = 0 <= y1 < ROWS and 0 <= y2 < ROWS
        if_x_in_borders = 0 <= x1 < COLUMNS and 0 <= x2 < COLUMNS
        return if_neighbor_cells and if_y_in_borders and if_x_in_borders

    def get_user_input_status(self):
        return self._user_input_status


if __name__ == '__main__':
    game_master = GameMaster()
    game_board = GameBoard()
    while True:
        game_board.remove_accidental_coincidences()
        game_master.display_board(game_board)
        game_master.display_count(*game_board.get_counters())
        user_input = game_master.check_user_input(input('Enter coordinates: ').upper())
        if game_board.failed_game():
            game_master.game_over()
            break
        if game_master.get_user_input_status() == game_master.USER_INPUT_EXIT:
            break
        if game_master.get_user_input_status() == game_master.USER_INPUT_FAILED:
            game_master.handle_bad_coordinates()
            game_board.increase_failed_attempts_counter()
            continue
        if game_master.get_user_input_status() == game_master.USER_INPUT_COORDINATES:
            coordinates_to_swap = game_master.get_coordinates(user_input)
            try:
                indexes = game_board.match_checker(coordinates_to_swap)
                if game_board.has_match():
                    game_board.make_the_move(coordinates_to_swap, indexes)
            except (ValueError, IndexError):
                game_master.handle_bad_coordinates()