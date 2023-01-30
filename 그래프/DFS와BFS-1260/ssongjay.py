import sys
from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph:
        if not visited[i]:
            dfs(graph, i, visited)


N, M, V = [int(x) for x in sys.stdin.readline().rstrip().split()]
