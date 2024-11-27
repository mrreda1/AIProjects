from board import Board


def run(board: Board, y=0):
    if len(board.queens) == board.size:
        return True

    for x in range(board.size):
        if board.place_queen(x, y):
            if run(board, y + 1):
                return True
            board.remove_queen(x, y)

    return False
