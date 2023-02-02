import sys
inp = sys.stdin.readline
n= int(inp().rstrip())
ran = [(-1,0),(1,0),(0,-1),(0,1)]
def packing(field,x,y):
    cnt = 1
    field[x][y] = 0
    for i in range(4):
        nx,ny = x + ran[i][0], y + ran[i][1]
        if(field[nx][ny] == 1):
            cnt += packing(field,nx,ny)
    return cnt

tmp = [list(map(int,inp().rstrip()))for _ in range(n)]
field = [[0]*(n+2) for _ in range(n+2)]
for i in range(n+2):
    for j in range(n+2):
        if(i==0 or i == n+1 or j == 0 or j == n+1):
            field[i][j] = 0
        else:
            field[i][j] = tmp[i-1][j-1]
ans_list = []
for i in range(n+2):
    for j in range(n+2):
        if(field[i][j] == 1):
            ans_list.append(packing(field,i,j))
ans_list.sort()
print(len(ans_list))
for i in range(len(ans_list)):
    print(ans_list[i])    