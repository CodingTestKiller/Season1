from sys import stdin
input = stdin.readline

N = int(input())

seat = [[0 for _ in range(N)] for _ in range(N)]

def have_like_std (seat, like_std):
    for i in range(N):
        for j in range(N):
            if seat[i][j] in like_std:
                return 1
            else:
                continue

    return 0

def poss_seat_cnt (seat, x, y):
    cnt = 0

    if x > 0 and seat[x-1][y] == 0:
        cnt += 1
    if y > 0 and seat[x][y-1] == 0:
        cnt += 1
    if x < N - 1 and seat[x+1][y] == 0:
        cnt += 1
    if y < N - 1 and seat[x][y+1] == 0:
        cnt += 1
    return cnt

def like_std_cnt (seat, x, y, like_std):
    cnt = 0

    if x > 0 and seat[x-1][y] in like_std:
        cnt += 1
    if y > 0 and seat[x][y-1] in like_std:
        cnt += 1
    if x < N - 1 and seat[x+1][y] in like_std:
        cnt += 1
    if y < N - 1 and seat[x][y+1] in like_std:
        cnt += 1
    return cnt

cmds = []

for _ in range(N*N):
    cmds.append([int(x) for x in input().split()])

for cmd in cmds:

    x = 0
    y = 0
    like_std = -1
    poss_seat = -1

    if have_like_std(seat, cmd[1::]) == 1:
        for i in range(N):
            for j in range(N):
                if seat[i][j] != 0:
                    continue
                else:
                    if like_std < like_std_cnt(seat, i, j, cmd[1::]):
                        like_std = like_std_cnt(seat, i, j, cmd[1::])
                        poss_seat = poss_seat_cnt(seat, i, j)
                        x = i
                        y = j
                
                    elif like_std == like_std_cnt(seat, i, j, cmd[1::]):
                        if poss_seat < poss_seat_cnt(seat, i, j):
                            poss_seat = poss_seat_cnt(seat, i, j)
                            x = i
                            y = j
                        else:
                            continue

                    else:
                        continue

    else:
        for i in range(N):
            for j in range(N):
                if seat[i][j] != 0:
                    continue
                if poss_seat < poss_seat_cnt(seat, i, j):
                    poss_seat = poss_seat_cnt(seat, i, j)
                    x = i 
                    y = j

    seat[x][y] = cmd[0]
    cmd.append(x)
    cmd.append(y)


print(seat)


result = 0

for cmd in cmds:
    cnt = like_std_cnt(seat, cmd[5], cmd[6], cmd[1:5])

    if cnt == 1:
        result += 1
    elif cnt == 2:
        result += 10
    elif cnt == 3:
        result += 100
    elif cnt ==  4:
        result += 1000
    else:
        continue

print(result)
