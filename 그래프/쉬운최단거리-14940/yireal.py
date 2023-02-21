from sys import stdin
from collections import deque
import time
inp = stdin.readline
n,m = map(int,inp().rstrip().split())
field = [list(map(int,inp().rstrip().split())) for _ in range(n)]
n_field = [[-1]*m for _ in range(n)]
ran = [(-1,0),(1,0),(0,-1),(0,1)]
que = deque()
for i in range(n):
    for j in range(m):
        if field[i][j] == 2:
            que.append((i,j,0))
            field[i][j] = -1
        if field[i][j] == 0:
            n_field[i][j] = 0
while que:
    x,y,cnt = que.popleft()
    n_field[x][y] = cnt
    for i in range(4):
        nx = x+ran[i][0]
        ny = y+ran[i][1]
        if(nx >= n or ny >= m or nx <0 or ny <0) : continue
        if(field[nx][ny] == -1): continue
        if(field[nx][ny] == 0) :
            n_field[nx][ny] = 0
            continue
        if(field[nx][ny] == 1):
            field[nx][ny] = -1
            que.append((nx,ny,cnt+1))
for i in range(n):
    for j in range(m):
        print(n_field[i][j],end=' ')
    print()
