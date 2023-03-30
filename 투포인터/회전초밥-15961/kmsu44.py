import sys
from collections import deque
input = sys.stdin.readline
n, d, k, c = map(int, input().split())
L = []
for _ in range(n):
    L.append(int(input()))

res = 0
s = set()
left = 0
life = [0 for _ in range(d+1)]
for i in range(k):
    s.add(L[i])
    life[L[i]] += 1
    if c in s:
        res = max(res, len(s))
    else:
        res = max(res, len(s) + 1)
for right in range(k, n + k - 1):
    if life[L[left]] == 1:
        s.discard(L[left])
        life[L[left]] -= 1
    else:
        life[L[left]] -= 1
    s.add(L[right % n])
    life[L[right % n]] += 1
    if c in s:
        res = max(res, len(s))
    else:
        res = max(res, len(s)+1)
    left += 1
print(res)


# 2 30 2 30
# 1
# 2
