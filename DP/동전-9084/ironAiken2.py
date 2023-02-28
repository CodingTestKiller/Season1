from sys import stdin
input = stdin.readline

# dp에 새로운 값을 넣는것이 아니라, 기존 저장값을 그대로 가져옴
# i 범위가 0 ~ m 이니까 bottom-up dp 구현

t = int(input())

for _ in range(t):
    n = int(input())
    coins = [int(x) for x in input().split()]
    m = int(input())

    dp = [0] * (m + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, m + 1):
            dp[i] += dp[i - coin]

        
    print(dp[m])