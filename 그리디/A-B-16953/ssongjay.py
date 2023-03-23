import sys

input_ = sys.stdin.readline

A, B = [int(x) for x in input_().split()]

cnt = 1
while True:
    if A == B:
        print(cnt)
        break
    elif A > B:
        print(-1)
        break
    elif B % 2 == 0:
        B = B // 2
        cnt += 1
    elif B % 10 == 1:
        B = B // 10
        cnt += 1
    else:
        print(-1)
        break
