import algorithms

n = int(input("n = "))

board = algorithms.Backtracking(n).run()

if board:
    print(" ---"*n)
    for y in range(n):
        for x in range(n):
            print(f"| {'Q' if x == board[y] else ' '} ", end="")
        print("|\n" + " ---"*n)
else:
    print("No solutions found!")
