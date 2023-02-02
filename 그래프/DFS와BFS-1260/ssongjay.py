import sys
from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M, V = [int(x) for x in sys.stdin.readline().rstrip().split()]
visited = [False] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = [int(x) for x in sys.stdin.readline().rstrip().split()]
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

dfs(graph, V, visited)
visited = [False] * (N + 1)
print()
bfs(graph, V, visited)
