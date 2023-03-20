from sys import stdin

input = stdin.readline

a, b = [int(x) for x in input().split()]

cnt = 1
while True:
    if b == a:
        print(cnt)
        break
    if b < a:
        print(-1)
        break

    if b % 10 == 1:
        b -= 1
        b //= 10
    elif b % 2 != 0:
        print(-1)
        break
    else:
        b //= 2
    cnt += 1
