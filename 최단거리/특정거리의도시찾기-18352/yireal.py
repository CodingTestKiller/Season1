import sys
import heapq
inp = sys.stdin.readline
n,m,k,x = map(int,inp().split())
graph = [[] for i in range(n+1)]
distance = [sys.maxsize] * (n+1)
for _ in range(m):
    a,b = map(int,inp().split())
    graph[a].append(b)
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dis,pos = heapq.heappop(q)
        if distance[pos] < dis : continue
        for i in graph[pos]:
            next_dis = dis + 1
            if next_dis < distance[i]:
                distance[i] = next_dis
                heapq.heappush(q,(next_dis,i))
dijkstra(x)
if k not in distance:
    print(-1)
else:
    for i in range (1,n+1):
        if distance[i] == k:
            print(i)