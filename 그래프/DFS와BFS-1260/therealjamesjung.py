from sys import stdin
from collections import deque


input = stdin.readline

n, m, v = [int(x) for x in input().split()]

graph = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y = [int(x) - 1 for x in input().split()]
    graph[x][y], graph[y][x] = 1, 1


def dfs(graph, current, visited):
    if current in visited:
        return
    visited.append(current)
    print(current + 1, end=' ')
    for vertex, connected in enumerate(graph[current]):
        if connected:
            dfs(graph, vertex, visited)


def bfs(graph, start):
    queue = deque()
    visited = []
    queue.append(start)
    while queue:
        current = queue.popleft()
        visited.append(current)
        print(current + 1, end=' ')
        for vertex, connected in enumerate(graph[current]):
            if connected and vertex not in visited and vertex not in queue:
                queue.append(vertex)


visited = []
dfs(graph, v - 1, visited)
print()
bfs(graph, v - 1)
