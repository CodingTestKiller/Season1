import sys

N, M = [int(x) for x in sys.stdin.readline().rstrip().split()]
arr= [[int(x) for x in sys.stdin.readline().rstrip().split()] for _ in range(N)]
sum_arr = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        sum_arr[i][j] = arr[i - 1][j - 1] + sum_arr[i - 1][j] + sum_arr[i][j - 1] - sum_arr[i - 1][j - 1]

max_sum = -400000001
for x1 in range(1, N + 1):
	for y1 in range(1, M + 1):
		for x2 in range(x1, N + 1):
			for y2 in range(y1, M + 1):
				max_sum = max(max_sum, sum_arr[x2][y2] - sum_arr[x1 - 1][y2] - sum_arr[x2][y1 - 1] + sum_arr[x1 - 1][y1 - 1])
print(max_sum)
