import sys
n = int(input())
L = [0] + list(map(int, input().split()))
dp = [0] * (n+1)
for i in range(n-1, 0, -1):
    M = sys.maxsize
    for j in range(i+1, n):
        M = min(M, max((j-i) * (1 + abs(L[i] - L[j])), dp[j]))
    M = min(M, (n-i) * (1 + abs(L[i]-L[n])))
    dp[i] = M
print(dp[1])
