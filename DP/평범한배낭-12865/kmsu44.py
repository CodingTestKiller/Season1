n, k = map(int, (input().split()))
L = [list(map(int, input().split())) for _ in range(n)]
M = [[0] * (k+1) for i in range(n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        if L[i-1][0] <= j:
            M[i][j] = max(M[i-1][j], L[i-1][1] + M[i-1][j-L[i-1][0]])
        else:
            M[i][j] = M[i-1][j]
print(M[-1][-1])
