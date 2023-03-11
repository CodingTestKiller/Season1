# 넴모넴모 (Easy)

n, m = map(int, input().split())

sqare_list = [(0, -1), (-1, 0), (-1, -1)]

visit = [[True] * m for _ in range(n)]


def DFS():
    global cnt
    cnt += 1
    for i in range(n):
        for j in range(m):
            if visit[i][j]:
                a, b, c = sqare_list
                if visit[i+a[0]][j+a[1]] == False and visit[i+b[0]][j+b[1]] == False and visit[i+c[0]][j+c[1]] == False:
                    return
                visit[i][j] = False
                DFS()


global cnt
cnt = 0
DFS()
print(cnt)
