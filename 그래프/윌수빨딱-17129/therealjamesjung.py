from sys import stdin
from collections import deque

input = stdin.readline

n, m = [int(x) for x in input().split()]

start_x, start_y = -1, -1

matrix = [[x for x in input().strip()] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if matrix[i][j] == '2':
            start_x = i
            start_y = j

queue = deque([[start_x, start_y, 0]])
moves = [[-1, 0], [0, -1], [0, 1], [1, 0]]

while queue:
    x, y, move_cnt = queue.popleft()
    move_cnt += 1
    matrix[x][y] = ''
    for dx, dy in moves:
        if x+dx < 0 or y+dy < 0 or x+dx > n-1 or y+dy > m-1 or matrix[x+dx][y+dy] == '':
            continue
        elif matrix[x+dx][y+dy] == '0':
            queue.append([x+dx, y+dy, move_cnt])
        elif matrix[x+dx][y+dy] != '1':
            print('TAK')
            print(move_cnt)
            exit()

print('NIE')
