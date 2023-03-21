import sys

A, B = map(int,sys.stdin.readline().split())
cnt = 1
flag = 0

while A != B:
    tmp = B
    if B % 10 == 1:
        B //= 10
        cnt+=1
    elif B % 2 == 0:
        B //= 2
        cnt+=1

    if tmp == B:
        flag = 1
        break

if flag == 0:
    print(cnt)
else:
    print(-1)

#10m
