from sys import stdin

input = stdin.readline
n, m = [int(x) for x in input().split()]

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

for i in range(n):
    for j in range(n):
        matrix[i][j] += matrix[i-1][j] if i > 0 else 0
        matrix[i][j] += matrix[i][j-1] if j > 0 else 0
        matrix[i][j] -= matrix[i-1][j-1] if i > 0 and j > 0 else 0


for _ in range(m):
    x1, y1, x2, y2 = [int(x) - 1 for x in input().split()]

    result = matrix[x2][y2]
    result -= matrix[x2][y1-1] if y1 > 0 else 0
    result -= matrix[x1-1][y2] if x1 > 0 else 0
    result += matrix[x1-1][y1-1] if x1 > 0 and y1 > 0 else 0

    print(result)
