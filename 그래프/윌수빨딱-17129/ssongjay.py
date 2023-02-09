# 솔루션 봄
import sys
from collections import deque

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
                0 <= nx < N
                and 0 <= ny < M
                and graph[nx][ny] != 1
                and not visited[nx][ny]
            ):
                queue.append([nx, ny])
                visited[nx][ny] = visited[i][j] + 1
                if graph[nx][ny] in (3, 4, 5):
                    print("TAK")
                    print(visited[i][j])
                    return
    print("NIE")


input_ = sys.stdin.readline
N, M = [int(x) for x in input_().rstrip().split()]
visited = [[0] * M for _ in range(N)]
graph = [[int(x) for x in str(sys.stdin.readline().rstrip())] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            bfs(graph, i, j, visited)
