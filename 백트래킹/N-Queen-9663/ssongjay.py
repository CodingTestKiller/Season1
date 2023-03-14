import sys

input_ = sys.stdin.readline

N = int(input_())
board = [[0 for _ in range(N)] for _ in range(N)]

def N_queen_puzzle(N):
    cnt = 0
    