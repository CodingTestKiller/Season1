from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
check = [list(map(int, input().strip())) for _ in range(n)]


def BFS():
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    queue = deque()
    
    for i in range(n):
        for j in range(m):
            if check[i][j] == 2:
                queue.append([i, j, 0])
                check[i][j] = 1
                break

    while queue:
        x, y, depth = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny>= m or check[nx][ny] == 1:
                continue
            if check[nx][ny] > 2:
                print("TAK")
                print(depth + 1)
                return
            queue.append([nx, ny, depth + 1])
            check[nx][ny] = 1

    print("NIE")

BFS()
