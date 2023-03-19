import sys

input_ = sys.stdin.readline

max_broken = 0
N = int(input())
egg = [list(map(int, input().split())) for _ in range(N)]


def dfs(idx):
    global max_broken
    if idx == N:
        count = 0
        for j in egg:
            if j[0] <= 0:
                count += 1
        if max_broken < count:
            max_broken = count
        return
    if egg[idx][0] <= 0:
        dfs(idx + 1)
    else:
        flag = False
        for i in range(N):
            if idx != i and egg[i][0] > 0:
                egg[idx][0] -= egg[i][1]
                egg[i][0] -= egg[idx][1]
                flag = True
                dfs(idx + 1)
                egg[idx][0] += egg[i][1]
                egg[i][0] += egg[idx][1]
        if not flag:
            dfs(idx + 1)


dfs(0)
print(max_broken)
