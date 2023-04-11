from sys import stdin, maxsize

input = stdin.readline

n = int(input())
m = int(input())

distances = [[maxsize] * (n+1) for _ in range(n+1)]

for _ in range(m):
    start, dest, cost = [int(x) for x in input().split()]
    distances[start][dest] = min(distances[start][dest], cost)
    distances[start][start] = 0
    distances[dest][dest] = 0


for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if k == i or j == i or j == k:
                continue
            distances[j][k] = min(
                distances[j][k], distances[j][i] + distances[i][k])

for distance in distances[1:]:
    for d in distance[1:]:
        print(d, end=' ') if d != maxsize else print(0, end=' ')
    print()
