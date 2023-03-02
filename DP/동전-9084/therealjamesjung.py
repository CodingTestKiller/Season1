from sys import stdin

input = stdin.readline

n = int(input())

for _ in range(n):
    _ = input()
    coins = [int(x) for x in input().split()]
    price = int(input())
    cache = [0] * (price+1)
    cache[0] = 1
    for coin in coins:
        for i in range(coin, price+1):
            cache[i] += cache[i - coin]
    print(cache[price])
