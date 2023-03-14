# 넴모넴모 (Easy)

n, m = map(int, input().split())
visit = [[True] * (m+1) for _ in range(n+1)]


def DFS(x, y):
    global cnt
    if (x, y) == (n+1, 1):
        cnt += 1
        return
    if y == m:
        nx = x + 1
        ny = 1
    else:
        nx = x
        ny = y + 1
    DFS(nx, ny)

    if visit[x-1][y] or visit[x-1][y-1] or visit[x][y-1]:
        visit[x][y] = False
        DFS(nx, ny)
        visit[x][y] = True


global cnt
cnt = 0
DFS(1, 1)
print(cnt)
