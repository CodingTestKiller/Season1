import sys
import heapq
inp = sys.stdin.readline
n,d = map(int,inp().split())
graph = [[] for _ in range(d+1)]
for i in range (d):
    graph[i].append((i+1,1))
for _ in range(n):
    s,e,l = map(int,inp().split())
    if e > d: continue
    graph[s].append((e,l))
INF = 1e9
distance = [INF] * (d+1)
q = []
heapq.heappush(q,(0,0))
distance[0] = 0
while q:
    dist,now = heapq.heappop(q)
    if dist > distance[now]:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))
print(distance[d])