import sys
from itertools import permutations as P
input = sys.stdin.readline

N = int(input())

num = ['1','2','3','4','5','6','7','8','9']
numl = list(P(num,3))
for _ in range(N):
    n, strike, ball = map(int, input().split())
    n = str(n)

    tmp = []

    for li in numl:
        s = sum([1 if n[j] == li[j] else 0 for j in range(3)])
        b = len(set(n) & set(li)) - s

        if s == strike and b == ball:
            tmp.append(li)
    numl = tmp

print(len(numl))