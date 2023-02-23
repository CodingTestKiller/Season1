import copy
import sys
my_input = sys.stdin.readline


def seed(x, y, is_placed, count, n):
    dx = [1, -1, 0, 0, 0]
    dy = [0, 0, 1, -1, 0]
    cost = 0
    min = 0
    is_placed_cpy = copy.deepcopy(is_placed)
    for k in range(5):
        mx = x + dx[k]
        my = y + dy[k]
        if is_placed_cpy[mx][my] == 1 or mx < 0 or my < 0 or mx >= n or my >= n:
            return None
    for k in range(5):
        mx = x + dx[k]
        my = y + dy[k]
        is_placed_cpy[mx][my] = 1
        cost += garden[mx][my]
    count += 1
    if count == 3:
        return cost
    for i in range(x, n - 1):
        for j in range(1, n - 1):
            if i == x:
                j = y
            ret = seed(i, j, is_placed_cpy, count, n)
            if ret == None:
                continue
            if min == 0:
                min = ret
            elif ret < min:
                min = ret
    if min == 0:
        return None
    return min + cost


n = int(my_input())
garden = [list(map(int, my_input().rstrip().split())) for _ in range(n)]
min = 0

for i in range(1, n - 1):
    for j in range(1, n - 1):
        is_placed = [[0 for _ in range(n)] for _ in range(n)]
        ret = seed(i, j, is_placed, 0, n)
        if ret == None:
            continue
        elif min == 0:
            min = ret
        elif ret < min:
            min = ret
print(min)
