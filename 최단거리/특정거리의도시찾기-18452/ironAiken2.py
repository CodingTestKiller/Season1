# BFS 를 사용한 풀이
import heapq
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

# 큐를 이용한 다익스트라 풀이
input = stdin.readline

n, m, k, x = [int(x) for x in input().split()]
graph = [[] for _ in range(n+1)]
dist = [n+2] * (n+1)
for _ in range(m):
    a, b = [int(x) for x in input().split()]
    graph[a].append((b, 1))


def find_short_path(start: int) -> None:
    q = []
    heapq.heappush(q, (x, 0))
    dist[start] = 0

    while q:
        start, cost = heapq.heappop(q)
        for i in graph[start]:
            total = cost + i[1]
            if total < dist[i[0]]:
                dist[i[0]] = total
                heapq.heappush(q, (i[0], dist[i[0]]))


find_short_path(x)
ans = []

for i, distance in enumerate(dist):
    if distance == k:
        ans.append(i)

if ans:
    for a in ans:
        print(a)
else:
    print(-1)
