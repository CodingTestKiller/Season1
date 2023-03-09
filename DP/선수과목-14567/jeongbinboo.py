import sys

my_input = sys.stdin.readline

n, m = [int(x) for x in my_input().split()]

classes = [1 for _ in range(n + 1)]
info = []
for i in range(m):
    pre, post = [int(x) for x in my_input().split()]
    info.append([pre, post])

info.sort()
for data in info:
    pre, post = data[0], data[1]
    classes[post] = max(classes[pre] + 1, classes[post])

for i in range(1, n + 1):
    print(classes[i], end=' ')
