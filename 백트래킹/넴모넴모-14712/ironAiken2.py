from sys import stdin
input = stdin.readline

n, m = [int(x) for x in input().split()]
board = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

cnt = 0


def find_all_way(x, y):
    global cnt

    if x == n + 1 and y == 1:
        cnt += 1
        return

    flag = 0
    if board[x-1][y]:
        flag += 1
    if board[x][y-1]:
        flag += 1
    if board[x-1][y-1]:
        flag += 1

    if flag != 3:
        board[x][y] = 1
        if y == m:
            find_all_way(x+1, 1)
        else:
            find_all_way(x, y+1)
        board[x][y] = 0
    if y == m:
        find_all_way(x+1, 1)
    else:
        find_all_way(x, y+1)


find_all_way(1, 1)
print(cnt)
