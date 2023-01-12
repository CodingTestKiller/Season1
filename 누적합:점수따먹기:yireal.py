import sys
inp = sys.stdin.readline
N,M = map(int,inp().rstrip().split())
table = list()
sum_table = [[0] * (M+1) for i in range(N+1)]
for i in range(N):
    table.append([])
    table[i] = list(map(int,inp().rstrip().split()))
for i in range(1,N+1):
    for j in range(1,M+1):
        sum_table[i][j] = sum_table[i][j-1] + sum_table[i-1][j] - sum_table[i-1][j-1] + table[i-1][j-1]
max_val = -400000001
for x1 in range(1,N+1):
    for y1 in range(1,M+1):
        for x2 in range(x1,N+1):
            for y2 in range(y1,M+1):
                val = sum_table[x2][y2]-sum_table[x2][y1-1]-sum_table[x1-1][y2]+sum_table[x1-1][y1-1]
                if(max_val < val):
                    max_val = val
print(max_val)
