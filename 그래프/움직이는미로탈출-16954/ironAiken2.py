import sys
from sys import stdin
from collections import deque

chess = deque(list(input().rstrip()) for _ in range(8))

move = [[0, 0], [0, -1], [0, 1], [-1, 0],
        [1, 0], [-1, -1], [1, -1], [1, 1], [-1, 1]]


def bfs():
    q = deque([(7, 0)])
    cnt = 0
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            if chess[x][y] == '#':
                continue
            if (x, y) == (0, 7):
                return 1

            for i in range(9):
                nx = x + move[i][0]
                ny = y + move[i][1]

                if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
                    continue
                if chess[nx][ny] == '#':
                    continue

                q.append((nx, ny))

        chess.pop()
        chess.appendleft(['.' for _ in range(8)])

        cnt += 1
        if cnt == 9:
            return 1

    return 0


print(bfs())
