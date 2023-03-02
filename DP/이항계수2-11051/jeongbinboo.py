import sys

my_input = sys.stdin.readline


def storing(n):
    for i in range(3, n + 1):
        target = (stored[i - 1][0] * 10007 + stored[i - 1][1]) * i
        stored[i][0] = target // 10007
        stored[i][1] = target % 10007


def ret_numb(n):
    return stored[n][0] * 10007 + stored[n][1]


stored = [[0 for _ in range(2)] for _ in range(1001)]
stored[1][0] = 0
stored[1][1] = 1
stored[2][0] = 0
stored[2][1] = 2
n, k = [int(x) for x in my_input().split()]
storing(n)
try:
    print(ret_numb(n) // (ret_numb(k) * ret_numb(n - k)) % 10007)
except ZeroDivisionError:
    print(1)
