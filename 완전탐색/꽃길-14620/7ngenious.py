import sys
import itertools
input = sys.stdin.readline
C = itertools.combinations

N = int(input())
result = 20001

entire = [list(map(int, input().split())) for _ in range(N)]
tmp = [(x, y) for x in range(1, N-1) for y in range(1, N-1)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def visit(area, result):
    ans = result
    visited = [] 
    sum = 0

    for x, y in area:
        visited.append((x, y)) 
        sum += entire[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx, ny) not in visited:
                visited.append((nx, ny))
                sum += entire[nx][ny]
            else:
                return ans

    ans = min(ans, sum)
    return ans

for area in C(tmp, 3):
    result = visit(area, result)

print(result)