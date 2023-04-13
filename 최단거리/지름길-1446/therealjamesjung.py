from sys import stdin

input = stdin.readline

n, d = [int(x) for x in input().split()]

graph = {}


for _ in range(n):
    start, dest, distance = [int(x) for x in input().split()]
    if start > d or dest > d or dest-start < distance:
        continue
    try:
        graph[start].append([dest, distance])
    except KeyError:
        graph[start] = [[dest, distance]]

dp = list(range(d+1))

for i in range(d+1):
    dp[i] = min(dp[i], dp[i-1] + 1)
    try:
        for dest, distance in graph[i]:
            dp[dest] = min(dp[dest], dp[i] + distance)
    except KeyError:
        pass

print(dp[-1])
