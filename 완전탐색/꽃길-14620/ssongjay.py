import sys

input_ = sys.stdin.readline

N = int(input_())
ground = [[int(x) for x in input_().rstrip().split()] for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

min_total = 3001


def check(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N or visited[nx][ny]:
            return False
    return True


def calc_price(x, y):
    price = ground[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny]:
            price += ground[nx][ny]
    return price


def dfs(x, total, cnt):
    global min_total

    if cnt == 3:
        min_total = min(min_total, total)
        print(min_total)
        return

    for i in range(x, N):
        for j in range(1, N):
            if check(i, j):
                visited[i][j] = True
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    visited[nx][ny] = True
                dfs(i, total + calc_price(i, j), cnt+1)
                visited[i][i] = False
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    visited[nx][ny] = False


dfs(1, 0, 0)
print(min_total)
