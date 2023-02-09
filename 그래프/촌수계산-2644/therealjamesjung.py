from sys import stdin

input = stdin.readline

n = int(input())

a, b = [int(x) for x in input().split()]

m = int(input())

matrix = [[] for _ in range(n+1)]


for _ in range(m):
    x, y = [int(x) for x in input().split()]
    matrix[x].append(y)
    matrix[y].append(x)


visited = []


def dfs(matrix, visited, current, target, depth):
    if current == target:
        print(depth)
        exit()
    visited.append(current)
    for c in matrix[current]:
        if c not in visited:
            dfs(matrix, visited, c, target, depth+1)


dfs(matrix, visited, a, b, 0)
print(-1)
