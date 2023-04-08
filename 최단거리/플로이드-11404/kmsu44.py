from heapq import heappop, heappush
import sys
n = int(input())
m = int(input())
graph = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s][e] = min(graph[s][e], w)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j or k == i or k == j:
                continue
            else:
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == sys.maxsize:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()
