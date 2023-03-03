from sys import stdin
input = stdin.readline

n, m = [int(x) for x in input().split(' ')]

cmd = [[0]*(m+1)] + [[0]+[int(x) for x in input().split(' ')]
                     for _ in range(n)]


dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] += dp[i-1][j] + dp[i][j-1] + cmd[i][j] - dp[i-1][j-1]

k = int(input())
for _ in range(k):
    x1, y1, x2, y2 = [int(x) for x in input().split(' ')]

    ans = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]

    print(ans)
