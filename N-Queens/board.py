class Board:
    queens = []

    def __init__(self, size):
        self.size = size
        self.occupied_column = [False] * size
        self.occupied_diagonal = [False] * size * 2
        self.occupied_revdiagonal = [False] * size * 2

    def is_solved(self) -> bool:
        if len(self.queens) == self.size:
            return True
        return False

    def is_safe_move(self, x, y) -> bool:
        return not (self.occupied_column[x] or self.occupied_diagonal[y + x]
                    or self.occupied_revdiagonal[y - x + self.size])

    def make_move(self, x, y) -> bool:
        if not self.is_safe_move(x, y):
            return False

        self.occupied_column[x] = self.occupied_diagonal[y + x] = \
            self.occupied_revdiagonal[y - x + self.size] = True
        self.queens.append(x)
        return True

    def cancel_last_move(self, x, y):
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
