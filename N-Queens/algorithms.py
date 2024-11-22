class Backtracking:
    queens = []

    def __init__(self, n):
        self.n = n
        self.occupied_column = [False] * n
        self.occupied_diagonal = [False] * n * 2
        self.occupied_revdiagonal = [False] * n * 2

    def run(self):
        self.solve()
        return self.queens

    def solve(self, y=0):
        if len(self.queens) == self.n:
            return
        for x in range(self.n):
            ok = not (self.occupied_column[x] or self.occupied_diagonal[y + x]
                      or self.occupied_revdiagonal[y - x + self.n])
            if ok:
                self.occupied_column[x] = self.occupied_diagonal[y + x] = \
                    self.occupied_revdiagonal[y - x + self.n] = True
                self.queens.append(x)
                self.solve(y + 1)
                if len(self.queens) == self.n:
                    return
                self.queens.pop()
                self.occupied_column[x] = self.occupied_diagonal[y + x] = \
                    self.occupied_revdiagonal[y - x + self.n] = False
