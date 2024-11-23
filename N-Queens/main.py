from board import Board
import backtracking


def main():
    n = int(input("n = "))
    board = Board(n)
    backtracking.run(board)
    if board.is_solved():
        print(board)
    else:
        print("No solutions found!")


if __name__ == "__main__":
    main()
