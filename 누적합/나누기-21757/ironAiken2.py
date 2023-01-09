from sys import stdin
input = stdin.readline

N = int(input())
matrix = [int(x) for x in input().split()]
sum_matrix = matrix
ret = 0
dp = [0 for _ in range(5)]

for i in range(1, N):
    sum_matrix[i] += sum_matrix[i-1]

if (sum_matrix[-1] % 4 > 0):
    ret = 0
else:
    if (sum_matrix[-1] == 0):
        zero = sum_matrix.count(0)
        ret = int((zero-1)*(zero-2)*(zero-3)/6)

    else:
        dp[0] = 1
        val = int(sum_matrix[-1]/4)

        for i in range(0, N):
            t = int(sum_matrix[i]/val)
            if (sum_matrix[i] % val != 0 or t < 1 or t > 4):
                continue
            dp[t] += dp[t-1]
        ret = dp[4]

print(ret)
