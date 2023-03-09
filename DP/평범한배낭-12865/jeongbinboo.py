import sys

my_input = sys.stdin.readline

n, k = [int(x) for x in my_input().split()]
stuffs = [[0, 0] for _ in range(n + 1)]
cases = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    w, v = [int(x) for x in my_input().split()]
    stuffs[i][0], stuffs[i][1] = w, v
    for j in range(1, k + 1):
        if w <= j:
            cases[i][j] = max(cases[i - 1][j - w] + v, cases[i - 1][j])
        else:
            cases[i][j] = cases[i - 1][j]

print(cases[-1][-1])
