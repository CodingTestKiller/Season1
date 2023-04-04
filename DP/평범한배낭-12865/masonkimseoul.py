import sys

N,K=map(int,sys.stdin.readline().split())
payload=[]
dp=[[0]*(K+1) for _ in range(N+1)]
for _ in range(N):
    payload.append(list(map(int,sys.stdin.readline().split())))

for i in range(1,N+1):
    for j in range(1,K+1):
        if payload[i-1][0]<=j:
            dp[i][j]=max(dp[i-1][j],payload[i-1][1]+dp[i-1][j-payload[i-1][0]])
        else:
            dp[i][j]=dp[i-1][j]
print(dp[-1][-1])
#2h