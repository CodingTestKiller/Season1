import sys

my_input = sys.stdin.readline


def func(n):
    if stored[n] == 0:
        for i in range(1, 4):
            stored[n] += func(n - i)

    return stored[n]


stored = [0 for _ in range(11)]
stored[1] = 1
stored[2] = 2
stored[3] = 4

t = int(my_input())

for _ in range(t):
    n = int(my_input())
    answer = 0
    print(func(n))
