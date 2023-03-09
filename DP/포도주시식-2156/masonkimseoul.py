import sys

N=int(sys.stdin.readline())
wine=[0]
dp=[0]*(N+1)
for _ in range(N):
    wine.append(int(sys.stdin.readline()))
dp[1]=wine[1]
if N<3:
    print(sum(wine))
else:
    dp[2]=dp[1]+wine[2]
    for i in range(3,N+1):
        dp[i]=max(dp[i-3]+wine[i-1]+wine[i],dp[i-2]+wine[i],dp[i-1])
    print(dp[N])
#1h