# 바텀업 2차원 dp 사용
# 점화식, i 는 0부터 n+1 까지, 0일때는 모든값 0
# j 는 0부터 k+1 까지, 0일때는 0
# j % w != 0 이면 왼쪽과 위 값중에 큰값 선택
# j % w == 0 이면 i-1 의 j-w 값 + v 와 현재 dp 값 비교해서 넣기

from sys import stdin
input = stdin.readline

n, k = [int(x) for x in input().split(' ')]

goods = [[int(x) for x in input().split(' ')] for _ in range(n)]

dp = [[0 for _ in range(k + 1)] for _ in range(n+1)]

for i in range(1, n+1):
    w, v = goods[i-1]

    for j in range(1, k+1):
        if j < w:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        else:
            dp[i][j] = max(dp[i-1][j-w] + v, dp[i][j-1], dp[i-1][j])


print(dp[-1][-1])
