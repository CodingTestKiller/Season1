from sys import stdin

input = stdin.readline

n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

result = 0

for start in range(n):
    for dest in range(start):
        flag = True
        for i in range(n):
            if dest == i or start == i:
                continue
            if matrix[start][dest] < matrix[start][i] + matrix[i][dest]:
                pass
            elif matrix[start][dest] > matrix[start][i] + matrix[i][dest]:
                print(-1)
                exit()
            else:
                flag = False
        if flag:
            result += matrix[start][dest]


print(result)
