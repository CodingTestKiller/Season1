from sys import stdin

input = stdin.readline
n = int(input())

queen_positions = [-1 for _ in range(n)]
cnt = 0


def validate(queen_positions: list, index: int, position: int):
    for i in range(index):
        if queen_positions[i] == position:
            return False
        if abs(queen_positions[i] - position) == abs(index-i):
            return False
    return True


def dfs(queen_positions: list, index: int):
    if index == n:
        global cnt
        cnt += 1
        return

    for i in range(n):
        if not validate(queen_positions, index, i):
            continue
        queen_positions[index] = i
        dfs(queen_positions, index+1)


dfs(queen_positions, 0)
print(cnt)
