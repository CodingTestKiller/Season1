from sys import stdin

input = stdin.readline

n = int(input())
wines = [int(input()) for _ in range(n)]

if n < 3:
    print(sum(wines))
    exit()

cache = [0] * n
cache[0] = wines[0]
cache[1] = wines[0] + wines[1]
cache[2] = sum(wines[:3]) - min(wines[:3])

for i in range(3, n):
    cache[i] = max(cache[i-3] + wines[i] + wines[i-1],
                   cache[i-2] + wines[i], cache[i-1])

print(cache[-1])
