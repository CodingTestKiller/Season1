# 넴모넴모 (Easy)

n, m = map(int, input().split())

sqare_list = [
    [(0, -1), (-1, 0), (-1, -1)],
    [(-1, 0), (-1, 1), (0, 1)],
    [(0, -1), (1, -1), (1, 0)],
    [(0, 1), (1, 0), (1, 1)]
]

visit = [[True] * m for _ in range(n)]


def DFS(x, y):
    global cnt
    for i in range(n):
        for j in range(m):
            if i == x and j == y:
                continue
            if visit[i][j]:
                flag = 0
                for sqare in sqare_list:
                    a, b, c = sqare
                    try:
                        if visit[i+a[0]][j+a[1]] == False and visit[i+b[0]][j+b[1]] == False and visit[i+c[0]][j+c[1]] == False:
                            flag = 1
                            return
                    except IndexError:
                        continue
                if flag == 1:
                    continue
                else:
                    visit[i][j] = False
                    DFS(i, j)
                    visit[i][j] = True


global cnt
DFS(0, 0)
