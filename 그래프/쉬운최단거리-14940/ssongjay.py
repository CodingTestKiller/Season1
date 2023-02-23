import sys
from collections import deque

input_ = sys.stdin.readline
N, M = [int(x) for x in input_().rstrip().split()]
graph = [[int(x) for x in input_().rstrip().split()] for _ in range(N)]
visited = [[-1] * M for _ in range(N)]


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(graph, i, j, visited):
    queue = deque()
    queue.append([i, j])
    visited[i][j] += 1
    while queue:
        i, j = queue.popleft()
        for index in range(4):
            nx = i + dx[index]
            ny = j + dy[index]
            if (
                0 <= nx < N and 0 <= ny < M
                and graph[nx][ny] != 0
                and visited[nx][ny] == -1
            ):
                queue.append([nx, ny])
                visited[nx][ny] = visited[i][j] + 1

for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            bfs(graph, i, j, visited)

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()
