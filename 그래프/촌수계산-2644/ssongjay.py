import sys


def dfs(graph, v, find, visited, cnt, value):
    visited[v] = True
    cnt += 1
    if v == find:
        print(cnt - 1)
        value[0] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, find, visited, cnt, value)


input_ = sys.stdin.readline
n = int(input_().rstrip())
a, b = [int(x) for x in input_().rstrip().split()]
m = int(input_().rstrip())
visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = [int(x) for x in input_().rstrip().split()]
    graph[x].append(y)
    graph[y].append(x)

value = [False]
dfs(graph, a, b, visited, 0, value)
if value[0] == False:
    print(-1)
