import sys
input = sys.stdin.readline

A, B = map(int,input().split())

cnt = 0

while(B != A):
    if B < A:
        cnt = -2
        break
    elif B % 10 == 1:
        B //= 10
        cnt += 1
    elif B % 2 == 0:
        B //= 2
        cnt+= 1
    else:
        cnt = -2
        break
print(cnt+1)