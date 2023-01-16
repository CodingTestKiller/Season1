from sys import stdin

input = stdin.readline

n = int(input())

room = [[0 for x in range(n)] for y in range(n)]


def vacant_cnt(room, x, y):
    cnt = 0
    if x > 0 and room[x-1][y] == 0:
        cnt += 1
    if y > 0 and room[x][y-1] == 0:
        cnt += 1
    if x < n - 1 and room[x+1][y] == 0:
        cnt += 1
    if y < n - 1 and room[x][y+1] == 0:
        cnt += 1
    return cnt


def like_cnt(room, x, y, likes):
    cnt = 0
    if x > 0 and room[x-1][y] in likes:
        cnt += 1
    if y > 0 and room[x][y-1] in likes:
        cnt += 1
    if x < n - 1 and room[x+1][y] in likes:
        cnt += 1
    if y < n - 1 and room[x][y+1] in likes:
        cnt += 1
    return cnt


cmds = []

for _ in range(n * n):
    cmds.append([int(x) for x in input().split()])

for cmd in cmds:
    max_like = -1
    max_vacant = -1
    max_x = 0
    max_y = 0

    for x in range(n):
        for y in range(n):
            if room[x][y] == 0:
                current_like = like_cnt(room, x, y, cmd[1:])
                current_vacant = vacant_cnt(room, x, y)
                if max_like < current_like or (max_like == current_like and max_vacant < current_vacant):
                    max_y = y
                    max_x = x
                    max_like = current_like
                    max_vacant = current_vacant

    room[max_x][max_y] = cmd[0]
    cmd.append([max_x, max_y])

result = 0

for cmd in cmds:
    cnt = like_cnt(room, cmd[-1][0], cmd[-1][1], cmd[1:-1])
    result += 10 ** (cnt - 1) if cnt != 0 else 0

print(result)
