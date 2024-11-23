import algorithms


def print_board(board):
    n = len(board)
    print(" ---"*n)
    for y in range(n):
        for x in range(n):
            print(f"| {'Q' if x == board[y] else ' '} ", end="")
        print("|\n" + " ---"*n)


def main():
    n = int(input("n = "))
    board = algorithms.Backtracking(n).run()
    if board:
        print_board(board)
    else:
        print("No solutions found!")


if __name__ == "__main__":
    main()
