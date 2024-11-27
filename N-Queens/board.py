from typing import List, override


class Board:
    def __init__(self, size):
        self.queens = []
        self.size = size
        self.occupied_column = [0] * size
        self.occupied_diagonal = [0] * size * 2
        self.occupied_revdiagonal = [0] * size * 2

    def is_solved(self) -> bool:
        if len(self.queens) == self.size:
            return True
        return False

    def is_safe_move(self, x, y) -> bool:
        return not (self.occupied_column[x] or self.occupied_diagonal[y + x]
                    or self.occupied_revdiagonal[y - x + self.size])

    def place_queen(self, x, y) -> int:
        if not self.is_safe_move(x, y):
            return False

        self.occupied_column[x] = self.occupied_diagonal[y + x] = \
            self.occupied_revdiagonal[y - x + self.size] = True
        self.queens.append(x)
        return True

    def remove_queen(self, x, y):
        self.queens.pop()
        self.occupied_column[x] = self.occupied_diagonal[y + x] = \
            self.occupied_revdiagonal[y - x + self.size] = False

    def __repr__(self):
        board = f"{" ---" * self.size}\n"
        for y in range(self.size):
            for x in range(self.size):
                board += f"| {'Q' if x == self.queens[y] else ' '} "
            board += f"|\n{" ---" * self.size}\n"
        return board


class GeneticBoard(Board):
    def __init__(self, queens: List[int]):
        super().__init__(len(queens))
        self.calculate_number_of_threatens(queens)

    def calculate_number_of_threatens(self, queens: List[int]):
        self.threatens = 0
        for y, q in enumerate(queens):
            self.threatens += self.place_queen(q, y)

    @override
    def place_queen(self, x: int, y: int) -> int:
        threatens = self.occupied_column[x] + self.occupied_diagonal[y + x] + \
            self.occupied_revdiagonal[y - x + self.size]

        self.occupied_column[x] += 1
        self.occupied_diagonal[y + x] += 1
        self.occupied_revdiagonal[y - x + self.size] += 1

        self.queens.append(x)

        return threatens
