import sys
input = sys.stdin.readline

n = int(input())
grape = [int(input()) for _ in range(n)]

dp = [0] * (n+1)
if n == 1:
  print(grape[0])

elif n == 2:
  print(grape[0]+grape[1])

elif n == 3:
  print(max(grape[0] + grape[1], grape[1] + grape[2], grape[0] + grape[2]))

else:  
  dp[1] = grape[0]
  dp[2] = grape[0] + grape[1]
  dp[3] = max(dp[2], grape[1] + grape[2], grape[0] + grape[2])
  for i in range(4, n+1) :
      dp[i] = max(dp[i-1], dp[i-2] + grape[i-1], dp[i-3] + grape[i-2] + grape[i-1])
  print(dp[n])