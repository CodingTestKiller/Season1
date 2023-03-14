import sys

input_ = sys.stdin.readline

N = int(input_())


def is_valid_board(board, column):
    for i in range(column):
        if board[column] == board[i]:
            return False
        elif board[column] - board[i] == column - i:
            return False
        elif board[i] - board[column] == column - i:
            return False
    return True


def init_board(board, column, count):
    board[column] = 0
    while board[column] < N:
        if is_valid_board(board, column):
            if column == N - 1:
                count[0] += 1
            else:
                init_board(board, column + 1, count)
        board[column] += 1


def N_queens_puzzle(N):
    board = [0] * N
    count = [0]
    init_board(board, 0, count)
    return count[0]


print(N_queens_puzzle(N))
