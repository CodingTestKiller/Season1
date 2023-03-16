import sys

N, M = map(int, sys.stdin.readline().split())
graph = [[0] * M for _ in range(N)]


def DFS(x, y):
    cnt = 0

    if y >= M:
        x += 1
        y = 0
    if x >= N:
        return 0

    if graph[x][y - 1] == 0 or graph[x - 1][y - 1] == 0 or graph[x - 1][y] == 0:
        graph[x][y] = 1
        cnt += DFS(x, y + 1) + 1
        graph[x][y] = 0

    cnt += DFS(x, y + 1)
    return cnt


print(DFS(0, 0) + 1)

#1h 30m