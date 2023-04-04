from sys import stdin
input = stdin.readline

n, m = [int(x) for x in input().split()]

ic = [[] for _ in range(n + 1)]

for _ in range(m):
    i1, i2 = [int(x) for x in input().split()]
    ic[i1].append(i2)
    ic[i2].append(i1)

cnt = 0

for i1 in range(1, n-1):
    for i2 in range(i1+1, n):
        if i2 in ic[i1]:
            continue
        for i3 in range(i2+1, n+1):
            if i3 in ic[i2]:
                continue
            if i3 in ic[i1]:
                continue
            cnt += 1

print(cnt)
            