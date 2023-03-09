from sys import stdin

input = stdin.readline

n, m = [int(x) for x in input().split()]

cache = [1] * (n+1)
prerequisites = sorted([[int(x) for x in input().split()]
                       for _ in range(m)], key=lambda x: (x[0], x[1]))

for pre, post in prerequisites:
    cache[post] = max(cache[pre] + 1, cache[post])

print(*cache[1:])
