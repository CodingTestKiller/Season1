from sys import stdin
input = stdin.readline

N, M = [int(x) for x in input().split(' ')]
matrix = [[int(x) for x in input().split(' ')] for _ in range(N)]

sum_data = [[0] * (M + 1) for i in range(N + 1)]


for i in range(1, N + 1):
    for j in range(1, M + 1):
        sum_data[i][j] = sum_data[i][j-1] + sum_data[i-1][j] - \
            sum_data[i-1][j-1] + matrix[i-1][j-1]

max = matrix[0][0]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        # i and j is start index
        for a in range(i, N + 1):
            for b in range(j, M + 1):
                # a and b is end index
                sum = sum_data[a][b] - sum_data[i-1][b] - \
                    sum_data[a][j-1] + sum_data[i-1][j-1]

                if (max < sum):
                    max = sum

print(max)
