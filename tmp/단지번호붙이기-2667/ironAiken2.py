from sys import stdin
input = stdin.readline

n = int(input())

map1 = [[x for x in input().rstrip()] for _ in range(n)]

dx = [-1, 1, 0, 0]  # 상하
dy = [0, 0, -1, 1]  # 좌우

cnt = 0
danji = []


def dfs(x, y):
    global cnt

    cnt += 1
    map1[x][y] = '0'

    for i in range(4):
        if x + dx[i] < 0 or x + dx[i] >= n or y + dy[i] < 0 or y + dy[i] >= n:
            continue
        else:
            if map1[x+dx[i]][y+dy[i]] == '1':
                dfs(x+dx[i], y+dy[i])


for i in range(n):
    for j in range(n):
        if map1[i][j] == '1':
            cnt = 0
            dfs(i, j)
            danji.append(cnt)

danji.sort()

print(len(danji))
for ans in danji:
    print(ans)
