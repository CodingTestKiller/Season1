import sys

input_ = sys.stdin.readline

T = int(input_())

for _ in range(T):
    N = int(input_())
    coins = list(map(int, input_().split()))
    M = int(input_())
    
    dp = [[0] * (N + 1) for _ in range(M + 1)]
    for j in range(N + 1):
        dp[0][j] = 1
    
    for i in range(1, M+1):
        for j in range(1, N+1):
            dp[i][j] = dp[i][j-1]
            if i >= coins[j-1]:
                dp[i][j] += dp[i-coins[j-1]][j]
    
    print(dp[M][N])
