from collections import deque
from sys import stdin
input = stdin.readline

n, m, k, x = [int(x) for x in input().split()]
town = [[] for _ in range(n)]
visit = [-1 for _ in range(n)]

for _ in range(m):
    a, b = [int(x) for x in input().split()]

    town[a-1].append(b)

q = deque()
q.append(x)
visit[x-1] = 0

ans = []

while q:
    start = q.popleft()
    if visit[start-1] == k:
        ans.append(start)

    for des in town[start-1]:
        if visit[des-1] == -1:
            q.append(des)
            visit[des-1] = visit[start-1] + 1

if not ans:
    print(-1)
    exit()

for a in sorted(ans):
    print(a)
