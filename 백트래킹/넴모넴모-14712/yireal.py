import sys
inp = sys.stdin.readline
n,m = map(int,inp().split())
field = [[0]*m for _ in range(n)]
def dfs(x,y):
    count = 0
    if y >=m :
        x = x+1
        y = 0
    if x >= n:
        return 0
    if field[x][y-1] == 0 or field[x-1][y-1] == 0 or field[x-1][y] == 0:
        field[x][y] = 1
        count += dfs(x,y+1) + 1
        field[x][y] = 0
    count += dfs(x,y+1) 

    return count
print(dfs(0,0)+1)
