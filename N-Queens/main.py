from board import Board
import backtracking
import genetic


def main():
    n = int(input("Board size? "))
    print("1. Backtracking")
    print("2. Genetic")
    algorithm = int(input("\\> "))
    match algorithm:
        case 1:
            board = Board(n)
            backtracking.run(board)
            if board.is_solved():
                print(board)
            else:
                print("No solutions found!")
        case 2:
            genetic.run(n)
        case _:
            print("Invalid choice")


if __name__ == "__main__":
    main()
