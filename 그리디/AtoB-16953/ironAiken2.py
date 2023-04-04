from sys import stdin
input = stdin.readline

a, b = [int(x) for x in input().split(' ')]
cnt = 0


r = 1
while (b != a):
    r += 1
    temp = b
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2

    if temp == b:
        print(-1)
        break
else:
    print(r)
