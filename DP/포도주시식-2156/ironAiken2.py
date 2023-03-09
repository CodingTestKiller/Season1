# i > 3 일 경우,
# 점화식 1, input[i] + input[i-1] + dp[i-3]
# 점화식 2, input[i] + dp[i-2]
# 점화식 3, dp[i -1]
# bottom-up dp 구현

from sys import stdin
input = stdin.readline

n = int(input())
dp = [0] * n

wine = [int(input()) for _ in range(n)]


dp[0] = wine[0]
if n == 1:
    print(dp[-1])
    exit()
dp[1] = wine[0] + wine[1]
if n == 2:
    print(dp[-1])
    exit()
dp[2] = max(dp[1], wine[0] + wine[2], wine[1] + wine[2])

for i in range(3, n):
    first = wine[i] + wine[i-1] + dp[i-3]
    second = wine[i] + dp[i-2]
    third = dp[i-1]

    dp[i] = max(first, second, third)

print(dp[-1])
