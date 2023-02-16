import sys

N = int(sys.stdin.readline().rstrip())
arr_N = [int(x) for x in sys.stdin.readline().rstrip().split()]
sum_N = [0 for _ in range(N)]

sum_N[0] = arr_N[0]
for i in range(1, N):
    sum_N[i] = sum_N[i - 1] + arr_N[i]

if sum_N[-1] % 4 != 0:
    print(0)
elif sum_N[-1] == 0:
    zero = 0;
    for i in sum_N:
        if i == 0:
            zero += 1
    print((zero - 1) * (zero - 2) * (zero - 3) // 6)
else:
    result = [0 for _ in range(5)]
    result[0] = 1
    base = sum_N[-1] // 4
    for i in range(N - 1):
        if sum_N[i] % base == 0 and 1 <= (sum_N[i] // base) < 4:
            index = sum_N[i] // base
            result[index] += result[index - 1]
    print(result[3])