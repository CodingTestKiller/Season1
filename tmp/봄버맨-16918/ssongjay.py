import sys

R, C, N = [int(x) for x in sys.stdin.readline().rstrip().split()]

boompos = []
input_map = [list(input()) for _ in range(R)]

for i in range(R):
    for j in range(C):
        if input_map[i][j] == 'O':
            boompos.append([i, j])

def set_boom(bomb_map):
    next_bomb = set()
    for i in range(R):
        for j in range(C):
            if bomb_map[i][j] == '.':
                next_bomb.add((i, j))
                bomb_map[i][j] = 'O'
    return next_bomb

def boom(bomb_map, boompos, next_bomb):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    destroypos = set()
    for x, y in boompos:
        destroypos.add((x, y))
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                destroypos.add((nx, ny))
    for x, y, in destroypos:
        if (x, y) in next_bomb:
            next_bomb.remove((x, y))
        bomb_map[x][y] = '.'

time = 1
while time < N:
    next_bomb = set_boom(input_map)
    time += 1
    if time == N:
        break
    boom(input_map, boompos, next_bomb)
    boompos = next_bomb
    time += 1

for m in input_map:
    print("".join(m))