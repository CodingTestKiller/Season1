import sys

sys.setrecursionlimit(10**9)


def dfs(graph, v, visited):
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = v
            dfs(graph, i, visited)


input_ = sys.stdin.readline
N = int(input_().rstrip())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(N - 1):
    a, b = [int(x) for x in input_().rstrip().split()]
    graph[a].append(b)
    graph[b].append(a)


dfs(graph, 1, visited)

for i in range(2, N + 1):
    print(visited[i])
