from heapq import heappop, heappush
import sys

N, D = map(int, input().split())
graph = []
for i in range(D):
    graph.append({})
    for j in range(i+1, D+1):
        graph[i][j] = ((j-i))
for _ in range(N):
    start, end, weight = map(int, input().split())
    if end > D:
        continue
    graph[start][end] = (min(graph[start][end], weight))
distance_list = [sys.maxsize for _ in range(D+1)]

distance_list[0] = 0
heap = []
heappush(heap, (distance_list[0], 0))
while heap:
    distance, start = heappop(heap)
    if distance_list[start] < distance:
        continue
    if start == D:
        continue
    for end, weight in graph[start].items():
        if distance + weight < distance_list[end]:
            distance_list[end] = distance + weight
            heappush(heap, (distance_list[end], end))
print(distance_list[-1])
