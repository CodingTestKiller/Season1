from sys import stdin
input = stdin.readline

N, M = [int(x) for x in input().split(' ')]
train = [[0 for _ in range(20)] for _ in range(N)]

for _ in range(M):
    cmd = [int(x) for x in input().split(' ')]
    match cmd[0]:
        case 1:
            train[cmd[1] - 1][cmd[2] - 1] = 1
        case 2:
            train[cmd[1] - 1][cmd[2] - 1] = 0
        case 3:
            for x in range(18, -1, -1):
                train[cmd[1] - 1][x + 1] = train[cmd[1] - 1][x]
                train[cmd[1] - 1][x] = 0
        case 4:
            for x in range(0, 19):
                train[cmd[1] - 1][x] = train[cmd[1] - 1][x + 1]
                train[cmd[1] - 1][x + 1] = 0

cnt = 1

for i in range(1, N):
    check = 0
    for j in range(0, i):
        if (train[i] == train[j]):
            check = 1
            break
        else:
            continue
    if (check == 1):
        continue
    else:
        cnt += 1

print(cnt)
