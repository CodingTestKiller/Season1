from sys import stdin
input = stdin.readline

n, c = [int(x) for x in input().split()]
m = int(input())
info = [[] for _ in range(n)]

for _ in range(m):
    s, e, q = [int(x) for x in input().split()]
    info[s-1].append([e, q])

for data in info:
    data.sort()

current = [0 for _ in range(n)]

ans = 0

for i in range(n):
    ans += current[i]
    current[i] = 0
    if len(info[i]) == 0:
        continue

    for data in info[i]:
        total = sum(current)

        if data[1] <= c-total:
            current[data[0]-1] += data[1]
        else:
            if c-total != 0:
                current[data[0]-1] += c-total
                data[1] -= c-total

            i = -1

            while data[1] != 0 or sum(current[data[0]:]) != 0:
                if len(current[data[0]:]) < abs(i):
                    break
                if current[i] == 0:
                    i -= 1
                    continue
                if data[1] < current[i]:
                    current[data[0]-1] += data[1]
                    current[i] -= data[1]
                    data[1] = 0
                else:
                    current[data[0]-1] += current[i]
                    data[1] -= current[i]
                    current[i] = 0
                i -= 1

print(ans)
