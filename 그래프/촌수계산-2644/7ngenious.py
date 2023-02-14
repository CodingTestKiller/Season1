from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
A, B = map(int, input().split())
graph = [[False] for _ in range(n+1)]

for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].extend([b])
    graph[b].extend([a])

init = [-1] * (n+1)
init[A] = 0

def BFS(v):
    queue = deque()
    queue.append(v)
    while queue:
        tmp = queue.popleft()
        for i in graph[tmp]:
            if init[i] == -1:
                init[i] = init[tmp] + 1
                queue.append(i)

BFS(A)
print(init[B])