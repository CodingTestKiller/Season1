import sys

N,M=map(int,sys.stdin.readline().split())
prq=[]
dp=[1]*(N+1)
for i in range(M):
    prq.append(list(map(int,sys.stdin.readline().split())))
prq.sort(key=lambda x:x[0])
for i in range(M):
    if dp[prq[i][1]]<dp[prq[i][0]]+1:
        dp[prq[i][1]] = dp[prq[i][0]] + 1
print(*dp[1:])
#30m