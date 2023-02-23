import sys
from collections import deque

input = sys.stdin.readline
queue = deque()

n, m = [int(x) for x in input().split()]
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
map_list = [[int(x) for x in input().split()] for _ in range(n)]
is_visited = [[0 for _ in range(m)] for _ in range(n)]
answer = [[-1 for _ in range(m)] for _ in range(n)]
flag = 0

for i in range(n):
    for j in range(m):
        if map_list[i][j] == 2:
            answer[i][j] = 0
            queue.append([i, j])
            is_visited[i][j] = 1
            flag = 1
            break
    if flag == 1:
        break

while queue:
    current_i, current_j = queue.popleft()
    for x in range(4):
        moved_i = current_i + di[x]
        moved_j = current_j + dj[x]
        if moved_i < 0 or moved_i >= n or moved_j < 0 or moved_j >= m or is_visited[moved_i][moved_j] == 1:
            continue
        if map_list[moved_i][moved_j] == 1:
            queue.append([moved_i, moved_j])
            is_visited[moved_i][moved_j] = 1
            answer[moved_i][moved_j] = answer[current_i][current_j] + 1
        else:
            answer[moved_i][moved_j] = 0
for i in range(n):
    for j in range(m):
        if map_list[i][j] == 0:
            print(0, end=' ')
        else:
            print(answer[i][j], end=' ')
    print()
