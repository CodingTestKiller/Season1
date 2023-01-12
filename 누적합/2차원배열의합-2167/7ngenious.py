# 동적계획법없는 버전 메모리 문제발생
# n, m = map(int,input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]

# k=int(input())

# for _ in range(k):
#     x1, x2, y1, y2 = map(int,input().split())
#     result = 0
#     for i in range(x1-1,y1):
#       for j in range(x2-1,y2):
#         result += arr[i][j]
#     print(result)

n, m = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

k=int(input())
dp = [[0] * (m+1) for _ in range(n+1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = arr[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

for _ in range(k):
    i, j, x, y = map(int,input().split())
    print(dp[x][y] - dp[i-1][y] - dp[x][j-1] + dp[i-1][j-1])