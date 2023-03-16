import sys
from itertools import combinations

input_ = sys.stdin.readline

N, M = [int(x) for x in input_().split()]

not_eat = set()
for _ in range(M):
    a, b = [int(x) for x in input_().split()]
    not_eat.add((a, b))
    not_eat.add((b, a))

combs = combinations(range(1, N + 1), 3)
cnt = 0
for comb in combs:
    if (comb[0], comb[1]) not in not_eat and (comb[1], comb[0]) not in not_eat and \
        (comb[0], comb[2]) not in not_eat and (comb[2], comb[0]) not in not_eat and \
        (comb[1], comb[2]) not in not_eat and (comb[2], comb[1]) not in not_eat:
        cnt += 1

print(cnt)
