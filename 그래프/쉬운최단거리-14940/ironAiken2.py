from sys import stdin
input = stdin.readline
from collections import deque

n, m = [int(x) for x in input().split(' ')]
map1 = [[int(x) for x in input().split(' ')] for _ in range(n)]

sx = 0
sy = 0

for i in range(n):
    for j in range(m):
        if map1[i][j] == 2:
            sx = i
            sy = j
            break

moves = [[1,0],[-1,0],[0,1],[0,-1]]

q = deque()
q.append((sx, sy))
map1[sx][sy] = 0
while q:
    x, y = q.popleft()
    for move in moves:
        nx = x + move[0]
        ny = y + move[1]

        if 0 <= nx < n and 0 <= ny < m:
            if map1[nx][ny] != 0 and map1[nx][ny] == 1:
                q.append((nx,ny))
                map1[nx][ny] = map1[x][y] + 1

for move in moves:
    nx = sx + move[0]
    ny = sy + move[1]
    if 0<= nx < n and 0 <= ny < m and map1[nx][ny] != 0:
        map1[nx][ny] = -2

for i in range(n):
    for j in range(m):
        if map1[i][j] == 1:
            map1[i][j] = -1
        if map1[i][j] == -2:
            map1[i][j] = 1


for asd in map1:
    print(*asd)
