import numpy as np
from math import sqrt


class Board:
    size = 0

    def __init__(self):
        print("Board size?")
        print("4x4")
        print("6x6")
        print("9x9")

        while self.size not in [4, 6, 9]:
            self.size = int(input("\\> ")[0])

        print("Insert board")
        self.board = np.empty(10000, dtype=int)
        self.squares = np.zeros(
            self.size * 10, dtype=bool).reshape(self.size, 10)
        self.columns = np.zeros(
            self.size * 10, dtype=bool).reshape(self.size, 10)
        self.rows = np.zeros(self.size * 10, dtype=bool).reshape(self.size, 10)
        i = 0
        while i < self.size ** 2:
            line = input().split()
            for x in line:
                try:
                    self.board[i] = int(x)
                except:
                    self.board[i] = 0
                i += 1
        self.board.resize(self.size ** 2)
        self.board = self.board.reshape(self.size, self.size)
        if self.size in [4, 9]:
            self.square_width = self.square_height = sqrt(self.size)
        else:
            self.square_width = 3
            self.square_height = 2

    def is_valid(self) -> bool:
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] < 0 or self.board[i][j] > self.size:
                    return False
        return True

    def is_safe(self) -> bool:
        for row in range(self.size):
            for column in range(self.size):
                value = self.board[row][column]
                if value == 0:
                    continue

                square = self.get_square(row, column)
                if self.squares[square][value] or self.rows[row][value] \
                        or self.columns[column][value]:
                    return False
                self.squares[square][value] = self.rows[row][value] \
                    = self.columns[column][value] = True
        return True

    def get_square(self, row: int, column: int) -> int:
        if self.size in [4, 9]:
            sq = int(sqrt(self.size))
            return row - (row % sq) + int(column / sq)
        return row - (row % 2) + int(column / 3)

    def __repr__(self):
        board = f"{" ---" * self.size}\n"
        for i in range(self.size):
            board += '|'
            for j in range(self.size):
                board += f" {self.board[i][j] } {' ' if (j + 1) % self.square_width else '|'}"
            if (i + 1) % self.square_height == 0:
                board += f"\n{" ---" * self.size}\n"
            else:
                board += f"\n{' ' * 4 * self.size}\n"

        return board
