from board import Board


def run(board: Board, y=0):
    if len(board.queens) == board.size:
        return True

    for x in range(board.size):
        if board.make_move(x, y):
            if run(board, y + 1):
                return True
            board.cancel_last_move(x, y)

    return False
