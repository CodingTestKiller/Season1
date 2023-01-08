import sys

N, M = [int(x) for x in sys.stdin.readline().rstrip().split()]
arr_2D = [[int(x) for x in sys.stdin.readline().rstrip().split()] for _ in range(N)]

sum_2D = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        sum_2D[i][j] = arr_2D[i - 1][j - 1] + sum_2D[i - 1][j] + sum_2D[i][j - 1] - sum_2D[i - 1][j - 1]

K = int(sys.stdin.readline().rstrip())
for _ in range(K):
    i, j, x, y = [int(x) for x in sys.stdin.readline().rstrip().split()]
    print(sum_2D[x][y] - sum_2D[i - 1][y] - sum_2D[x][j - 1] + sum_2D[i - 1][j - 1])
