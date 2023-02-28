from sys import stdin

input = stdin.readline

cache = [[None for _ in range(1001)] for _ in range(1001)]

cache[0][0] = 1
cache[1][0] = 1
cache[1][1] = 1

for i in range(1001):
    for j in range(1001):
        if i < j:
            break
        elif i == 0 or j == 0 or i == j:
            cache[i][j] = 1
        elif j == 1:
            cache[i][j] = i
        else:
            cache[i][j] = cache[i-1][j-1] + cache[i-1][j]

n, k = [int(x) for x in input().split()]

print(cache[n][k] % 10007)
