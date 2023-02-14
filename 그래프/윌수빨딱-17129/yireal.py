import sys
from collections import deque
inp = sys.stdin.readline
n,m = map(int,inp().rstrip().split())
field = [list(map(int,list(inp().rstrip()))) for _ in range(n)]
offset = [(-1,0),(1,0),(0,-1),(0,1)]
des = [3,4,5]
total = 0
queue = deque()
for i in range(n):
    for j in range(m):
        if field[i][j] == 2:
            queue.append((i,j,0))
            field[i][j] = 1
while queue:

    x,y,cnt = queue.popleft()
 
    for i in range (4):
        nx,ny = x+offset[i][0],y+offset[i][1]
        if(nx < 0 or ny < 0 or nx >= n or ny >= m):
            continue
        if(field[nx][ny] == 1):
            continue
        if field[nx][ny] in des:
            print("TAK")
            print(cnt + 1)
            exit()
        field[nx][ny] = 1
        queue.append((nx,ny,cnt+1))
print("NIE")
        