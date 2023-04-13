from sys import stdin, maxsize
input = stdin.readline

n = int(input())
m = int(input())
matrix = [[maxsize for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    s, e, w = [int(x) for x in input().split()]
    matrix[s][e] = min(matrix[s][e], w)

for i in range(1, n+1):
    matrix[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if matrix[i][j] == maxsize:
            print(0, end=' ')
        else:
            print(matrix[i][j], end=' ')
    print()
