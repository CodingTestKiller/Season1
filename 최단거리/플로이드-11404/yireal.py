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
