from sys import stdin

input = stdin.readline

n = int(input())

cache = [0 for _ in range(12)]

cache[1] = 1
cache[2] = 2
cache[3] = 4

for i in range(4, 12):
    cache[i] = cache[i-1] + cache[i-2] + cache[i-3]

for _ in range(n):
    x = int(input())
    print(cache[x])
