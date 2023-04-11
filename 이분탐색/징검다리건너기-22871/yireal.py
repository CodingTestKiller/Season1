import sys
inp = sys.stdin.readline
n = int(inp())
a = list(map(int,inp().split()))
dp = [0] + [sys.maxsize] * (n-1)
for i in range(1,n):
    for j in range(0,i):
        power = max((i-j)*(1+abs(a[i]-a[j])),dp[j])
        dp[i] = min(power,dp[i])
print(dp[-1])