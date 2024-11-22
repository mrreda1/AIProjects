class Backtracking:
    """ Solves the N-Queens problem using the backtracking algorithm.
    Attributes:
        n: The size of the chessboard (NxN). """

    queens = []

    def __init__(self, n):
        self.n = n
        self.occupied_column = [False] * n
        self.occupied_diagonal = [False] * n * 2
        self.occupied_revdiagonal = [False] * n * 2

    def run(self):
        return self.queens if self.solve() else None

    def solve(self, y=0):
        if len(self.queens) == self.n:
            return True
        for x in range(self.n):
            ok = not (self.occupied_column[x] or self.occupied_diagonal[y + x]
                      or self.occupied_revdiagonal[y - x + self.n])
            if ok:
                self.occupied_column[x] = self.occupied_diagonal[y + x] = \
                    self.occupied_revdiagonal[y - x + self.n] = True
                self.queens.append(x)
                if self.solve(y + 1):
                    return True
                self.queens.pop()
                self.occupied_column[x] = self.occupied_diagonal[y + x] = \
                    self.occupied_revdiagonal[y - x + self.n] = False
        return False
