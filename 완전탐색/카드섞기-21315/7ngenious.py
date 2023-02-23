from sys import stdin
inp = stdin.readline
offset_1 = [(-1,0),(1,0),(0,-1),(0,1),(0,0)]
offset_2 = [(-2,0),(-1,-1),(-1,0),(-1,1),(0,-2),(0,-1),(0,0),(0,1),(0,2),(1,-1),(1,0),(1,1),(2,0)]
n = int(inp().rstrip())
field = [[int(x) for x in inp().rstrip().split()] for _ in range(n)]
sum_field = [[-1]*n for _ in range(n)]
ans = 0
def field_cnt(x,y):
    cnt = 0
    for i in range(5):
        nx = x+offset_1[i][0]
        ny = y+offset_1[i][1]
        if(nx >= n or ny >= n or nx <0 or ny <0):
            return -1
        cnt += field[nx][ny]
    return cnt

for i in range(n):
    for j in range(n):
        sum_field[i][j] = field_cnt(i,j)


for _ in range(3):
    min = 1000
    min_index = [0,0]
    for i in range(n):
        for j in range(n):
            tmp = sum_field[i][j]
            if(tmp == -1): continue
            elif(tmp < min):
                min_index = [i,j]
                min = sum_field[i][j]
    ans += min
    for i in range(len(offset_2)):
        nx = min_index[0]+offset_2[i][0]
        ny = min_index[1]+offset_2[i][1]
        if(nx >= n or ny >= n or nx <0 or ny <0):
            continue
        else:
            sum_field[nx][ny] = -1
print(ans)