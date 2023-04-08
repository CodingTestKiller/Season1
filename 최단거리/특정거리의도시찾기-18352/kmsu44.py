import sys
from heapq import heappush, heappop
input = sys.stdin.readline
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n)]
distance_list = [sys.maxsize for _ in range(n)]
for _ in range(m):
    start, end = map(int, input().split())
    graph[start-1].append(end-1)


distance_list[x-1] = 0

heap = []
heappush(heap, (distance_list[x-1], x-1))

while heap:
    distance, start = heappop(heap)
    if distance_list[start] < distance:
        continue
    for end in graph[start]:
        if distance + 1 < distance_list[end]:
            distance_list[end] = distance+1
            heappush(heap, (distance_list[end], end))
flag = 0
for idx, data in enumerate(distance_list):
    if data == k:
        print(idx+1)
        flag = 1
if flag == 0:
    print(-1)
