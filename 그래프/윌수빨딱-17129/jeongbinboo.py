import sys
import copy
from collections import deque

input = sys.stdin.readline

n, m = [int(x) for x in input().split()]
island_list = [[0 for _ in range(m)] for _ in range(n)]
is_visited = [[0 for _ in range(m)] for _ in range(n)]
startI, startJ = 0, 0
cnt = 0


def bfs():
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    queue = deque()
    queue.append([startI, startJ])
    is_visited[startI][startJ] = 1
    cnt = [[0 for _ in range(m)] for _ in range(n)]
    while queue:
        currentI, currentJ = queue.popleft()
        for i in range(4):
            nextI = currentI + di[i]
            nextJ = currentJ + dj[i]
            if nextI < 0 or nextI >= n or nextJ < 0 or nextJ >= m:
                continue
            if is_visited[nextI][nextJ] == 0 and island_list[nextI][nextJ] != 1:
                cnt[nextI][nextJ] = cnt[currentI][currentJ] + 1
                if island_list[nextI][nextJ] >= 3 and island_list[nextI][nextJ] <= 5:
                    return cnt[nextI][nextJ]
                is_visited[nextI][nextJ] = 1
                queue.append([nextI, nextJ])
    return None


for i in range(n):
    row = input()
    for j in range(m):
        island_list[i][j] = int(row[j])
        if island_list[i][j] == 2:
            startI = i
            startJ = j
answer = bfs()
if answer == None:
    print("NIE")
else:
    print("TAK")
    print(answer)
