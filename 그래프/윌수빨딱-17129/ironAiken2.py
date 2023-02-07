from collections import deque
from sys import stdin
input = stdin.readline

n, m = [int(x) for x in input().split(' ')]

map1 = [[x for x in input().rstrip()] for _ in range(n)]


move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
visit = [[0 for _ in range(m)] for _ in range(n)]


def bfs(x, y):
    q = deque()
    q.append([x, y])
    visit[x][y] = 1

    while q:
        x, y = q.popleft()

        for nx, ny in move:
            if 0 <= x + nx < n and 0 <= y + ny < m and not visit[x+nx][y+ny] and map1[x+nx][y+ny] != '1':
                visit[x + nx][y + ny] = visit[x][y]+1
                q.append([x + nx, y + ny])
                if map1[x + nx][y + ny] == '3' or map1[x + nx][y + ny] == '4' or map1[x + nx][y + ny] == '5':
                    print('TAK')
                    print(visit[x + nx][y + ny] - 1)
                    return

    print('NIE')


for i in range(n):
    for j in range(m):
        if map1[i][j] == '2':
            bfs(i, j)
