import sys
input = sys.stdin.readline

n, k, q, m = map(int, input().split())
sleep =  list(map(int, input().split()))
check = list(map(int, input().split()))

dp = [0]*(n+3)
arr = [True]*(n+3)

for i in sleep:
    arr[i]=False

for i in check:
    if arr[i]:
        dp[i]=1
        for j in range(i, n+3):
            if arr[j] and j%i==0 and dp[j]==0:
                dp[j]=1
for i in range(n+3):
    dp[i] += dp[i-1]
for _ in range(m):
    x,y = map(int, input().split())
    print(y+1 - x - (dp[y] - dp[x-1]))
