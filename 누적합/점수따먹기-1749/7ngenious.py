import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

dp = [[0] * (m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = arr[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

tmp = -10001
for x1 in range(1, n + 1):
    for y1 in range(1, m + 1):
        for x2 in range(x1, n + 1):
            for y2 in range(y1, m + 1):
                tmp = max(tmp, dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])
print(tmp)