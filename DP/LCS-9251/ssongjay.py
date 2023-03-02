import sys

input_ = sys.stdin.readline

str1 = str(input_().rstrip())
str2 = str(input_().rstrip())

N = len(str1)
M = len(str2)

dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[N][M])
