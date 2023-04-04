import sys

my_input = sys.stdin.readline

n = int(my_input())
wine = [0 for _ in range(n + 1)]
storing = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    wine[i] = int(my_input())

storing[1] = wine[1]
if n >= 2:
    storing[2] = wine[1] + wine[2]

if n >= 3:
    for i in range(3, n + 1):
        storing[i] = max(storing[i - 1], wine[i] + storing[i - 2],
                         wine[i] + wine[i - 1] + storing[i - 3])

print(storing[-1])
