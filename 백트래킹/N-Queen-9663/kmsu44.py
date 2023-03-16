N = int(input())

col_visit = [True] * N
up_diagonal = [True] * (N+N-1)
down_diagonal = [True] * (N+N-1)
global res
res = 0


def DFS(col):
    global res
    if col >= N:
        res += 1
        return
    for row in range(N):
        up = col+row
        if col - row < 0:
            down = 2 * N - 1 + (col-row)
        else:
            down = col-row
        if down_diagonal[down] and up_diagonal[up] and col_visit[row]:
            down_diagonal[down] = False
            up_diagonal[up] = False
            col_visit[row] = False
            DFS(col+1)
            col_visit[row] = True
            down_diagonal[down] = True
            up_diagonal[up] = True


DFS(0)

print(res)
