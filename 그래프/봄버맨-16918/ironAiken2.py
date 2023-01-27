from sys import stdin
import copy
input = stdin.readline

r, c, n = [int(x) for x in input().split(' ')]

map = [['.' for _ in range(c)] for _ in range(r)]
bombfull_map = [['O' for _ in range(c)] for _ in range(r)]
map2 = copy.deepcopy(bombfull_map)


for i in range(r):
    map[i] = [char for char in input()]
    del map[i][-1]

n -= 1

if n == 0:
    print(*map, sep='\n')
    exit()


while True:
    n -= 1
    if n == 0:
        print(*bombfull_map, sep='\n')
        break

    for i in range(r):
        for j in range(c):
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

    n -= 1
    if (n == 0):
        print(*map, sep='\n')
        break
