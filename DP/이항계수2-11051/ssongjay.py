import sys

input_ = sys.stdin.readline

N, K = [int(x) for x in input_().rstrip().split()]
factorial = [0] * 1001
factorial[0] = 1
factorial[1] = 1

for i in range(2, 1001):
    factorial[i] = factorial[i - 1] * i

def get_binomial_coefficient(factorial, N, K):
    total = 0
    total = factorial[N] // (factorial[K] * factorial[N - K])
    return total

print(get_binomial_coefficient(factorial, N, K) % 10007)
