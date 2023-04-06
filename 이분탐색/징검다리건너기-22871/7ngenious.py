import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

def min_power(N, A):
    INF = 4000000001
    dp = [0] + [INF] * (N - 1)

    for i in range(1, N):
        for j in range(i):
            power = max((i - j) * (1 + abs(A[i] - A[j])), dp[j])
            dp[i] = min(dp[i], power)

    return dp[N - 1]

ans = min_power(N, A)
print(ans)

