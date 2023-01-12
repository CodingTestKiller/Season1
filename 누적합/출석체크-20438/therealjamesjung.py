from sys import stdin


n, k, q, m = [int(x) for x in stdin.readline().split(' ')]
sleeping = [int(x) for x in stdin.readline().split(' ')]
codes = [int(x) for x in stdin.readline().split(' ')]

students = [-1 if x in sleeping else 1 for x in range(n+3)]


for code in codes:
    i = code
    if students[i] == -1:
        continue
    while i < len(students):
        if students[i] != -1:
            students[i] = 0
        i += code

for i in range(1, len(students)):
    if students[i] == -1:
        students[i] = 1
    students[i] += students[i-1]


for _ in range(m):
    s, e = [int(x) for x in stdin.readline().split(' ')]
    print(students[e] - students[s-1])
