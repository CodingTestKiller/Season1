# 넴모넴모 (Easy)

n, m = map(int, input().split())
move = []
for i in range(n):
    for j in range(n):
        move.append((i, j))
sqare_move = [
    # 좌상
    [(-1, -1), (-1, 0), (0, -1)],
    # 우상
    [(-1, 0), (-1, 1), (0, 1)],
    # 좌하
    [(0, -1),  (1, -1), (1, 0)],
    # 우하
    [(0, 1), (1, 0), (1, 1)]
]


cnt = 0


visit = [[True] * (m) for _ in range(n)]
for i in range(n):
    for j in range(n):
        visit[i][j] = False
        cnt += 1
        flag = 0
        for x, y in move:
            if x == i and y == j:
                continue
            if visit[x][y]:
                for sqare in sqare_move:
                    a, b, c = sqare
                    try:
                        if visit[x+a[0]][y+a[1]] is False and visit[x+b[0]][y+b[1]] is False and visit[x+c[0]][y+c[1]] is False:
                            flag = 1
                            break
                    except IndexError:
                        continue
                if flag == 1:
                    continue
                cnt += 1
                print(x, y)
print(cnt)
