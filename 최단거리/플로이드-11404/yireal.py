import sys
import heapq
inp = sys.stdin.readline
n = int(inp())
m = int(inp())
INF = 1e9
graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(m):
    s,e,c = map(int,inp().split())
    if graph[s][e] > c:
        graph[s][e] = c
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i!=j and graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            print(0,end=' ')
        else:
            print(graph[i][j],end=' ')
    print()
#플로이드-월셔 사용한 풀이 400ms python
            

"""
import sys
import heapq
inp = sys.stdin.readline
n = int(inp())
m = int(inp())
INF = 1e9
graph = [[] for _ in range(n+1)]
for _ in range(m):
    start,end,pay = map(int,inp().split())
    graph[start].append((end,pay))
for i in range(1,n+1):
    cost = [INF] * (n+1)
    q = []
    cost[i] = 0
    heapq.heappush(q,(i,0))
    while q:
        now,c = heapq.heappop(q)
        if cost[now] < c:
            continue
        for i in graph[now]:
            tmp = c + i[1]
            if tmp < cost[i[0]]:
                cost[i[0]] = tmp
                heapq.heappush(q,(i[0],tmp))
    for i in range(1,n+1):
        if cost[i] == INF:
            print(0,end=' ')
        else:
            print(cost[i],end = ' ')
    print('')
"""
#다익스트라 사용한 풀이 800ms pypy3