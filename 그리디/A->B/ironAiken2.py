from sys import stdin
input = stdin.readline

a, b = [int(x) for x in input().split(' ')]

ans = 10000


def find_way(a, b, cnt):
    global ans

    if a > b:
        return
    if a == b:
        ans = min(ans, cnt)

    find_way(a*10+1, b, cnt+1)
    find_way(2*a, b, cnt+1)


find_way(a, b, 0)
if ans == 10000:
    ans = -2

print(ans + 1)
