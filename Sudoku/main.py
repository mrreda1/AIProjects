from board import Board
import algorithms

board = Board()

if not board.is_valid():
    print("The entered board is not valid")
elif not (board.is_safe() and algorithms.backtracking(board)):
    print("No solution exists for the entered board.")
print(board)
