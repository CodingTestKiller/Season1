import sys
inp = sys.stdin.readline
r,c,n = map(int,inp().rstrip().split())
field = [list(inp().rstrip())for _ in range(r)]
ran = [(-1,0),(1,0),(0,-1),(0,1)]
bomb = []
find_bomb = lambda li : [(i,j) for j in range(c) for i in range(r) if li[i][j] == 'O']

def bomb_expl():
    global field,bomb
    for bx,by in bomb:
        field[bx][by] = '.'
        for i in range (4):
            cx,cy = bx + ran[i][0], by + ran[i][1]
            if cx in range(r) and cy in range(c):
                field[cx][cy] = '.'

def bomb_set():
    global field
    field = [['O']*c for _ in range(r)]

for sec in range(1,n):
    if sec % 2 == 1:
        bomb = find_bomb(field)
        bomb_set()
    else:
        bomb_expl()

for i in field:
        print(''.join(i))
