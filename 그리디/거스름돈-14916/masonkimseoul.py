import sys

cost = int(sys.stdin.readline())
coins=[0,-1,1,-1,2,1]+[0]*(cost-5)

for i in range(6,cost+1):
    if coins[i-2] != -1:
        coins[i] = coins[i-2]+1
    if coins[i-5] != -1:
        coins[i] = min(coins[i],coins[i-5] + 1)
print(coins[cost])
#15m