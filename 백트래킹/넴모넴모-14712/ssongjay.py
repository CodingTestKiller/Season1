import sys

input_ = sys.stdin.readline

N, M = [int(x) for x in input_().split()]

visited = [[False] * M for _ in range(N)]
cnt = 0
def is_visited(i, j):
    if visited[i][j]:
        return False
    if i > 0 and j > 0 and visited[i - 1][j - 1] and visited[i - 1][j] and visited[i][j - 1]:
        return False
    return True

def dfs(i, j):
    global cnt
    if j == M:
        i += 1
        j = 0
    if i == N:
        cnt += 1
        return
    if is_visited(i, j):
        visited[i][j] = True
        dfs(i, j + 1)
        visited[i][j] = False
    dfs(i, j + 1)

dfs(0, 0)
print(cnt)
