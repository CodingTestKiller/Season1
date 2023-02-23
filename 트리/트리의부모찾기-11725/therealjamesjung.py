from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
matrix = [[] for _ in range(n+1)]

for _ in range(n-1):
    x, y = [int(x) for x in input().split()]
    matrix[x].append(y)
    matrix[y].append(x)

visited = [0 for _ in range(n+1)]
queue = deque([1])
result = [0 for _ in range(n+1)]

while queue:
    current = queue.pop()
    visited[current] = 1
    for x in matrix[current]:
        if not visited[x]:
            queue.append(x)
            result[x] = current

[print(x) for x in result[2:]]
