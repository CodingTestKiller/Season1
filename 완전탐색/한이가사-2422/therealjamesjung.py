from sys import stdin
from itertools import combinations

input = stdin.readline

n, m = [int(x) for x in input().split()]

cases = set(combinations(range(1, n+1), 3))

for _ in range(m):
    a, b = [int(x) for x in input().split()]
    for i in range(1, n+1):
        if a == i or b == i:
            continue
        cases.discard(tuple(sorted([a, b, i])))

print(len(cases))
