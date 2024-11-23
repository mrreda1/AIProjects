from board import Board

board = Board()

if not board.is_valid():
    print("The entered board is not valid")
elif not board.is_safe():
    print("No solution exists for the entered board.")
else:
    print(board)
