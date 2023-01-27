from sys import stdin
import copy
input = stdin.readline

r, c, n = [int(x) for x in input().split(' ')]

map = [['.' for _ in range(c)] for _ in range(r)]
bombfull_map = [['O' for _ in range(c)] for _ in range(r)]
map2 = copy.deepcopy(bombfull_map)
cnt = 0

for i in range(r):
    map[i] = [char for char in input()]
    del map[i][-1]

if n == 0:
    for i in range(len(map)):
        print(''.join(s for s in map[i]))
    exit()

cnt += 1

if cnt == n:
    for i in range(len(map)):
        print(''.join(s for s in map[i]))
    exit()

while True:
    cnt += 1

    if cnt == n:
        for i in range(len(bombfull_map)):
            print(''.join(s for s in bombfull_map[i]))
        break

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'O':
                map2[i][j] = '.'
                if i > 0:
                    map2[i - 1][j] = '.'
                if i < r - 1:
                    map2[i + 1][j] = '.'
                if j > 0:
                    map2[i][j - 1] = '.'
                if j < c - 1:
                    map2[i][j + 1] = '.'

    map = copy.deepcopy(map2)
    map2 = copy.deepcopy(bombfull_map)

    cnt += 1

    if cnt == n:
        for i in range(len(map)):
            print(''.join(s for s in map[i]))
        break
