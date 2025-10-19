from dataclasses import dataclass
from random import random

@dataclass(frozen=True)
class Element:
    symbol: str
    EMPTY = '0'

    def __init__(self, c: str):
        object.__setattr__(self, 'symbol', c)

    @classmethod
    def empty(cls):
        return Element(cls.EMPTY)

class Board:
    def __init__(self, size: int):
        self.size = size
        # Создаём двумерный список размером size x size, заполненный элементами с символом EMPTY
        self.cells = [[Element(Element.EMPTY) for _ in range(size)] for _ in range(size)]

@dataclass(frozen=True)
class BoardState:
    board: Board
    score: int

class Game:
    symbols = ['A', 'B', 'C', 'D', 'E', 'F']

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
    def clone_board(board):
        b = Board(board.size)
        for row in range(board.size):
            for col in range(board.size):
                b.cells[row][col] = board.cells[row][col]
        return b

