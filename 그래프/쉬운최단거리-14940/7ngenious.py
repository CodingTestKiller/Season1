from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

check = [[0 for _ in range(m)] for _ in range(n)]
graph = [0 for _ in range(n)]

tr, tc = 0, 0

for i in range(n):
    graph[i] = list(map(int, input().strip().split()))
    for j in range(len(graph[i])):
        if graph[i][j] == 2:
            tr, tc = i, j

ans = [[-1 for _ in range(m)] for _ in range(n)]

def bfs(x, y):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    queue = deque()
    
    ans[x][y] = 0

    check[x][y] = 1
    graph[x][y] = 0
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny <m and graph[nx][ny] == 1 and check[nx][ny] == 0:
                check[nx][ny] = 1
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

bfs(tr, tc)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and check[i][j] == 0:
            graph[i][j] = -1

for i in graph:
    for j in i:
        print(j, end = ' ')
    print()
