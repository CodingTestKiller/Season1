from collections import deque

import sys
input = sys.stdin.readline

R, C, N = map(int, input().strip().split())
arr = [list(input()) for _ in range(R)]
q = deque()
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
def bfs(q, arr):
    while q:
        x, y = q.popleft()
        arr[x][y] = '.'
        for k in range(4):
            ny, nx = y+dy[k], x+dx[k]
            if 0<=ny<C and 0<=nx<R and arr[nx][ny] == 'O':
                arr[nx][ny] = '.'
def bomb(n):
    global q, arr
    if n == 1:
        for i in range(R):
            for j in range(C):
                if arr[i][j] == 'O':
                    q.append((i, j))
    elif n%2 == 1:
        bfs(q, arr)
        for i in range(R):
            for j in range(C):
                if arr[i][j] == 'O':
                    q.append((i, j))
    else:
        arr = [['O']*C for _ in range(R)]
for n in range(N):
    bomb(n+1)
for r in range(R):
    for c in range(C):
        print(arr[r][c], end="")
    print()