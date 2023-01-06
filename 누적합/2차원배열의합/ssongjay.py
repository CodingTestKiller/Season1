import sys

N, M = [int(x) for x in sys.stdin.readline().rstrip().split()]

arr_2D = [[int(x) for x in sys.stdin.readline().rstrip().split()] for i in range(N)]

print(arr_2D)

# K = int(sys.stdin.readline().rstrip())

sum_2D = []

for i in range(1, N + 1):
    for j in range(1, M + 1):
        sum_2D[i][j]

sum_2D = sum(arr_2D)
print(sum_2D)
# for _ in range(K):
#     ijxy = [int(x) for x in sys.stdin.readline().rstrip().split()]
