from sys import stdin
input = stdin.readline

n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
visit = [[False for _ in range(n)] for _ in range(n)]

ans = 0

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 0 or visit[i][j] == True:
            continue
        value = matrix[i][j]
        visit[i][j] = True
        visit[j][i] = True

        flag = False
        for k in range(n):
            if k == i or k == j:
                continue
            if matrix[i][k] + matrix[k][j] < value:
                print(-1)
                exit()
            if matrix[i][k] + matrix[k][j] == value:
                flag = True

        if flag == False:
            ans += matrix[i][j] if flag == False else 0


print(ans)
