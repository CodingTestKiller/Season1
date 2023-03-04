import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
dp = [-1] * (n+1)


def DP(k, cnt):
    res = cnt
    for i in graph[k]:
        res = max(res, dp[i])
    dp[k] = res + 1
    return dp[k]


for i in range(1, n+1):
    DP(i, 0)
print(*dp[1:])

exit()
# pypy3 통과 python 3 시간초과

n, m = map(int, input().split())


graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
dp = [-1] * (n+1)


def DFS(k, cnt):
    if dp[k] != -1:
        return dp[k] + 1
    res = cnt
    for i in graph[k]:
        res = max(res, DFS(i, cnt+1))
    dp[k] = res
    return dp[k]


for i in range(1, n+1):
    DFS(i, 1)
print(*dp[1:])
