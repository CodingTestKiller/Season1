n, k = map(int, input().split())
Memo = [[1 for i in range(n+1)] for _ in range(n+1)]
Memo[1][0] = 1
Memo[1][1] = 1

for i in range(2, n+1):
    for j in range(1, i):
        Memo[i][j] = Memo[i-1][j-1] + Memo[i-1][j]
print(Memo[n][k] % 10007)
