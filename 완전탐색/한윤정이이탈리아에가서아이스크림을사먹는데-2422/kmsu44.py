
n, m = map(int, input().split())
# index 0 ~ n-1
L = [[True] * (n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    L[a][b] = False
    L[b][a] = False
cnt = 0
for i in range(1, n-1):
    for j in range(i+1, n):
        if L[i][j]:
            for k in range(j+1, n+1):
                if L[j][k] and L[i][k]:
                    cnt += 1
print(cnt)
