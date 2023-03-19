from sys import stdin
input = stdin.readline

n = int(input())

col = [-1] * n
cnt = 0


def n_queens(index):
    global cnt
    if index == n:
        cnt += 1
        return

    for i in range(n):
        col[index] = i

        if dup_check(index):
            n_queens(index+1)

        col[index] = -1


def dup_check(index):
    for i in range(index):
        if col[i] == col[index]:
            return False
        if abs(i - index) == abs(col[i] - col[index]):
            return False

    return True


n_queens(0)

print(cnt)
