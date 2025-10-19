from sys import exit
from Board import Board, BoardState
from fp5.Match import process_cascade, fill_empty_spaces

INITIAL_SIZE = 8
INITIAL_SCORE = 0

class Game:

    @staticmethod
    def initialize_game() -> 'BoardState':
        board = Board.create_empty(INITIAL_SIZE)
        return process_cascade(fill_empty_spaces(BoardState(Board(INITIAL_SIZE), INITIAL_SCORE)))

    @staticmethod
    def draw(board):
        print("  0 1 2 3 4 5 6 7")
        for i in range(8):
            print(f"{i} ", end='')
            for j in range(8):
                print(board.cells[i][j].symbol, end=' ')
            print()
        print()

    @staticmethod
    def clone_board(board: 'Board') -> 'Board':
        new_cells = tuple(tuple(cell for cell in row) for row in board.cells)
        return Board(size=board.size, cells=new_cells)

    @staticmethod
    def read_move(bs: 'BoardState') -> 'BoardState':
        print(">", end=' ')
        input_line = input().strip()
        if input_line == 'q':
            exit(0)

        coords = input_line.split()
        if len(coords) != 4:
            print("Ошибка: введите 4 числа через пробел, например: 0 1 0 2")
            return bs

        try:
            y, x, y1, x1 = map(int, coords)
        except ValueError:
            print("Ошибка: введите корректные числа")
            return bs

        # Проверка границ доски (можно расширить)
        if not all(0 <= c < bs.Board.size for c in (x, y, x1, y1)):
            print("Ошибка: координаты вне диапазона")
            return bs

        board = Game.clone_board(bs.Board)

        # Меняем местами элементы
        # В Python cells — кортежи, поэтому нужно создать новый кортеж с заменой
        # Для удобства преобразуем строки в списки, поменяем, потом обратно в кортежи

        rows = [list(row) for row in board.cells]
        rows[x][y], rows[x1][y1] = rows[x1][y1], rows[x][y]
        new_cells = tuple(tuple(row) for row in rows)

        new_board = Board(size=board.size, cells=new_cells)
        return BoardState(new_board, bs.Score)



if __name__ == "__main__":
    bs = Game.initialize_game()
    while True:
        Game.draw(bs.Board)
        bs = Game.read_move(bs)
