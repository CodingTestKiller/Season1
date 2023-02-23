import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer = 0

paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
max_val = max(map(max, paper))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, dsum, cnt):
    global answer
    if answer >= dsum + max_val * (4 - cnt):
        return
        
    if cnt == 4:
        answer = max(answer, dsum)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if cnt == 2:
                visited[nx][ny] = True
                dfs(x, y, dsum + paper[nx][ny], cnt + 1)
                visited[nx][ny] = False
            visited[nx][ny] = True
            dfs(nx, ny, dsum + paper[nx][ny], cnt + 1)        
            visited[nx][ny] = False

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, paper[i][j], 1)
        visited[i][j] = False

print(answer)