from sys import stdin

input = stdin.readline

n = int(input())
durabilities = []
weights = []

for _ in range(n):
    d, w = [int(x) for x in input().split()]
    durabilities.append(d)
    weights.append(w)

max_cnt = 0


def dfs(durabilities: list, weights: list, index: int, cnt: int):
    global max_cnt
    max_cnt = max(max_cnt, cnt)
    if index == n:
        return
    if durabilities[index] <= 0:
        dfs(durabilities, weights, index+1, cnt)
    for i in range(n):
        if i == index or durabilities[index] <= 0 or durabilities[i] <= 0:
            continue
        tmp = 0
        durabilities[index] -= weights[i]
        durabilities[i] -= weights[index]
        if durabilities[index] <= 0:
            tmp += 1
        if durabilities[i] <= 0:
            tmp += 1
        dfs(durabilities, weights, index+1, cnt+tmp)
        durabilities[index] += weights[i]
        durabilities[i] += weights[index]


dfs(durabilities, weights, 0, 0)
print(max_cnt)
