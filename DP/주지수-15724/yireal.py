import sys
inp = sys.stdin.readline
n,m = map(int,inp().split())
field = [list(map(int,inp().split())) for _ in range(n)]
sum_table = [[0] * (m+1) for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        sum_table[i][j] = sum_table[i][j-1] + sum_table[i-1][j] - sum_table[i-1][j-1] + field[i-1][j-1]
for _ in range(int(inp())):
    x1,y1,x2,y2 = map(int,inp().split())
    print(sum_table[x2][y2] - sum_table[x2][y1-1] - sum_table[x1-1][y2] + sum_table[x1-1][y1-1])