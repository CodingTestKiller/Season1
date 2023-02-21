from sys import stdin
from collections import deque

input = stdin.readline

n, m = [int(x) for x in input().split()]

map = [[int(x) for x in input().split()] for _ in range(n)]
distance_map = [[-1 for _ in range(m)] for __ in range(n)]

flag = False

for i in range(n):
    if flag:
        break
    for j in range(m):
        if map[i][j] == 2:
            start_x = i
            start_y = j
            flag = True
            break

q = deque([[start_x, start_y, 0]])
distance_map[start_x][start_y] = 0

moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]

while q:
    x, y, distance = q.popleft()

    for dx, dy in moves:
        if x+dx < 0 or y+dy < 0 or x+dx > n-1 or y+dy > m-1:
            continue
        if distance_map[x+dx][y+dy] != -1 or map[x+dx][y+dy] == 0:
            continue
        q.append([x+dx, y+dy, distance+1])
        distance_map[x+dx][y+dy] = distance+1

for i in range(n):
    for j in range(m):
        if map[i][j] == 0:
            print(0, end=' ')
        else:
            print(distance_map[i][j], end=' ')
    print()
