import sys

N, M = [int(x) for x in sys.stdin.readline().rstrip().split()]

arr_N = [[int(x) for x in sys.stdin.readline().rstrip().split()] for _ in range(N)]
sum_N = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        sum_N[i][j] = arr_N[i - 1][j - 1] + sum_N[i - 1][j] + sum_N[i][j - 1] - sum_N[i - 1][j - 1]

for _ in range(M):
    x1, y1, x2, y2 = [int(x) for x in sys.stdin.readline().rstrip().split()]
    print(sum_N[x2][y2] - sum_N[x1 - 1][y2] - sum_N[x2][y1 - 1] + sum_N[x1 - 1][y1 - 1])
