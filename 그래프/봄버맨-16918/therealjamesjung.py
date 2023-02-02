from sys import stdin

input = stdin.readline

r, c, n = [int(x) for x in input().split()]


def invert(c):
    if c == '.':
        return 'O'
    else:
        return '.'


initial_matrix = [[x for x in input().strip()] for _ in range(r)]
initial_explode_matrix = [[invert(x) for x in line] for line in initial_matrix]

bombs = [[i, j] for i in range(r)
         for j in range(c) if initial_matrix[i][j] == 'O']

for bomb_x, bomb_y in bombs:
    if bomb_x > 0:
        initial_explode_matrix[bomb_x-1][bomb_y] = '.'
    if bomb_x < r - 1:
        initial_explode_matrix[bomb_x+1][bomb_y] = '.'
    if bomb_y > 0:
        initial_explode_matrix[bomb_x][bomb_y-1] = '.'
    if bomb_y < c - 1:
        initial_explode_matrix[bomb_x][bomb_y+1] = '.'
    initial_explode_matrix[bomb_x][bomb_y] = '.'


inverse_matrix = [[invert(x) for x in line] for line in initial_explode_matrix]

bombs = [[i, j] for i in range(r)
         for j in range(c) if inverse_matrix[i][j] == '.']


for bomb_x, bomb_y in bombs:
    if bomb_x > 0:
        inverse_matrix[bomb_x-1][bomb_y] = '.'
    if bomb_x < r - 1:
        inverse_matrix[bomb_x+1][bomb_y] = '.'
    if bomb_y > 0:
        inverse_matrix[bomb_x][bomb_y-1] = '.'
    if bomb_y < c - 1:
        inverse_matrix[bomb_x][bomb_y+1] = '.'


if n < 2:
    [print(''.join(x)) for x in initial_matrix]
elif n % 4 == 1:
    [print(''.join(x)) for x in inverse_matrix]
elif n % 4 == 3:
    [print(''.join(x)) for x in initial_explode_matrix]
elif n % 2 == 0:
    [print('O' * c) for _ in range(r)]
