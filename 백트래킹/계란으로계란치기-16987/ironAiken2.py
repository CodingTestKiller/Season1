from sys import stdin
input = stdin.readline

n = int(input())
durability = []
weight = []

for _ in range(n):
    s, w = [int(x) for x in input().split()]
    durability.append(s)
    weight.append(w)

if len(durability) == 1:
    print(0)
    exit()

ans = 0


def find_max(durability: list, weight: list, index: int, n: int, cnt: int):
    global ans

    ans = max(ans, cnt)

    if index == n:
        return
    if durability[index] <= 0:
        find_max(durability, weight, index+1, n, cnt)
        return

    for i in range(n):
        tmp = 0

        if i == index:
            continue
        if durability[i] <= 0:
            continue

        durability[index] -= weight[i]
        if durability[index] <= 0:
            tmp += 1
        durability[i] -= weight[index]
        if durability[i] <= 0:
            tmp += 1
        find_max(durability, weight, index+1, n, cnt + tmp)

        durability[index] += weight[i]
        durability[i] += weight[index]


find_max(durability, weight, 0, n, 0)
print(ans)
