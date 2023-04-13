import heapq
from sys import stdin
input = stdin.readline

n, d = [int(x) for x in input().split()]
graph = {}
dist = [10001] * (d+1)
dist[0] = 0

for _ in range(n):
    s, e, w = [int(x) for x in input().split()]

    try:
        graph[s].append((e, w))
    except:
        graph[s] = [(e, w)]

for i in range(d+1):
    dist[i] = min(dist[i], dist[i-1] + 1)
    try:
        for end in graph[i]:
            dist[end[0]] = min(dist[end[0]], dist[i] + end[1])
    except:
        dist[i] = min(dist[i], dist[i-1] + 1)

print(dist[-1])
