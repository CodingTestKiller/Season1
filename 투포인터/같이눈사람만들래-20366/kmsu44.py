from itertools import combinations
n = int(input())
L = list(map(int, input().split()))
LL = [i for i in range(n)]
C = list(combinations(LL, 2))
C.sort(key=lambda x: L[x[0]] + L[x[1]])
res = 1000000001


prev = C[0]
for cur in C[1:]:
    tmp = set(prev + cur)
    if len(tmp) == 4:
        res = min(res, abs(L[prev[0]] + L[prev[1]] - L[cur[0]] - L[cur[1]]))
    prev = cur
print(res)
