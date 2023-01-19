import sys

N, M = [int(x) for x in sys.stdin.readline().rstrip().split()]

train = [[0 for _ in range(21)] for _ in range(N + 1)]
check = []
for _ in range(M):
    command = [int(x) for x in sys.stdin.readline().rstrip().split()]
    if command[0] == 1:
        train[command[1]][command[2]] = 1
    elif command[0] == 2:
        train[command[1]][command[2]] = 0
    elif command[0] == 3:
        for j in range(20, 1, -1):
            train[command[1]][j] = train[command[1]][j - 1]
        train[command[1]][0] = 0
        train[command[1]][1] = 0
    elif command[0] == 4:
        for j in range(1, 20):
            train[command[1]][j] = train[command[1]][j + 1]
        train[command[1]][20] = 0

cnt = 0
for i in range(1, N + 1):
    if train[i] not in check:
        check.append(train[i])
        cnt += 1
print(cnt)