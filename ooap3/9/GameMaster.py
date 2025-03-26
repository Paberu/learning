import re
from typing import Final
import os

from GameBoard import GameBoard

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