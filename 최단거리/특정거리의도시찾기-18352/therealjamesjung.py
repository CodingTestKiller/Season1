from sys import stdin
from collections import deque


input = stdin.readline


n, m, k, x = [int(x) for x in input().split()]

graph = {}
distance = [0] + [-1] * n
distance[x] = 0


for _ in range(m):
    start, dest = [int(x) for x in input().split()]
    try:
        graph[start].append(dest)
    except KeyError:
        graph[start] = [dest, ]

queue = deque()
queue.append(x)

while queue:
    current = queue.popleft()
    if distance[current] > k:
        break
    try:
        for vertex in graph[current]:
            if distance[vertex] > distance[current] + 1:
                distance[vertex] = distance[current] + 1
                queue.append(vertex)
    except KeyError:
        pass


flag = False
for i, d in enumerate(distance):
    if d == k:
        print(i)
        flag = True
if not flag:
    print(-1)
