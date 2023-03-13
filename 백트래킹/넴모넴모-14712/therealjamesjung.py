from sys import stdin

input = stdin.readline

n, m = [int(x) for x in input().split()]

matrix = [[0] * m for _ in range(n)]
count = 0


def validate(matrix: list[list], x: int, y: int):
    result = 0

    try:
        result += matrix[x-1][y]
        result += matrix[x][y-1]
        result += matrix[x-1][y-1]
    except IndexError:
        return False
    return False if result == 3 else True


def dfs(matrix: list[list], x: int, y: int):
    global count
    if x == n and y == 0:
        count += 1
        return
    if y == m:
        next_x = x + 1
        next_y = 0
    else:
        next_x = x
        next_y = y + 1
    if validate(matrix, x, y):
        matrix[x][y] = 1
        dfs(matrix, next_x, next_y)
        matrix[x][y] = 0
    dfs(matrix, next_x, next_y)


dfs(matrix, 0, 0)
print(count)
