from sys import stdin
input = stdin.readline
from collections import deque

n, m = [int(x) for x in input().split(' ')]

map1 = [[x for x in input().rstrip()] for _ in range(n)]


move = [[0,1],[0,-1],[1,0],[-1,0]]
visit = [[False for _ in range(m)] for _ in range(n)]

def bfs(x, y):
    q = deque()
    q.append([x,y])
    cnt = 1

    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            visit[x][y] = True
            
            for nx, ny in move:
                if 0 <= x + nx < n and 0 <= y + ny < m and not visit[x+nx][y+ny] and map1[x+nx][y+ny] != '1':
                    if map1[x + nx][y + ny] == '3' or map1[x + nx][y + ny] == '4' or map1[x + nx][y + ny] == '5':
                        print('TAK')
                        print(cnt)
                        exit()
                    q.append([x + nx, y + ny])
        cnt += 1
    
    print('NIE')

for x, value in enumerate(map1):
    for y, value2 in enumerate(value):
        if value2 == '2':
            visit[x][y] = True
            bfs(x, y)