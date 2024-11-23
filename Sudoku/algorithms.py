from board import Board


def backtracking(board: Board, row=0, column=0) -> bool:
    if column == board.size:
        column = 0
        row += 1
    if row == board.size:
        return True

    if board.board[row][column]:
        if backtracking(board, row, column + 1):
            return True
    else:
        for value in range(1, board.size + 1):
            if board.make_move(row, column, value):
                if backtracking(board, row, column + 1):
                    return True
                board.cancel_move(row, column)

    return False
