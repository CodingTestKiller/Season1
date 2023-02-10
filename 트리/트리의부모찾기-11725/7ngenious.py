from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[False] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].extend([b])
    graph[b].extend([a])

queue = deque()
queue.append(1)

init = [0] * (n+1)

def BFS():
    while queue:
        tmp = queue.popleft()
        for i in graph[tmp]:
            if init[i] == 0:
                init[i] = tmp
                queue.append(i)

BFS()
for i in init[2:]:
    print(i)