import sys
input = sys.stdin.readline

N = int(input().strip())
std = [list(map(int, input().strip().split())) for _ in range(N**2)]
board = [[0] * N for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for i in std:
    s = i[0] 
    tmp = [] 
    for j in range(N):
        for k in range(N):
            if board[j][k]==0:
                like = 0
                blank = 0
                for l in range(4):
                    nr = j + dr[l]
                    nc = k + dc[l]
                    if 0 <= nr < N and 0 <= nc < N:
                        if board[nr][nc] in i[1:]:
                            like += 1
                        if board[nr][nc] == 0:
                            blank += 1
                tmp.append([like, blank, j, k])
    tmp.sort(key=lambda x:(-x[0], -x[1], x[2], x[3]))
    board[tmp[0][2]][tmp[0][3]] = s

res = 0
std.sort()

for i in range(N):
    for j in range(N):
        ans = 0
        for k in range(4):
            nr = i + dr[k]
            nc = j + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] in std[board[i][j]-1][1:]:
                    ans += 1
        if ans != 0:
            res += 10 ** (ans-1)
            
print(res)