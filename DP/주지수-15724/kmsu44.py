import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
S = [[0] * (m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        S[i][j] = S[i][j-1] + S[i-1][j] - S[i-1][j-1] + graph[i-1][j-1]
k = int(input())
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    res = S[x2][y2] - S[x2][y1-1] - S[x1-1][y2] + S[x1-1][y1-1]
    print(res)
# 4 4
# 9 14 29 7
# 1 31 6 13
# 21 26 40 16
# 8 38 11 23
# 3
# 1 1 3 2
# 1 1 1 4
# 1 1 4 4
