import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0] * (M + 1) for _ in range(N + 1)]
count = 0

def dfs(x, y):
    global count
    if (x, y) == (1, N + 1):
        count += 1
        return
    
    if x == M:
        nx, ny = 1, y + 1
    else:
        nx, ny = x + 1, y
        
    dfs(nx, ny)
    
    if graph[y - 1][x] == 0 or graph[y - 1][x - 1] == 0 or graph[y][x - 1] == 0:
        graph[y][x] = 1
        dfs(nx, ny)
        graph[y][x] = 0
        
dfs(1, 1)

print(count)