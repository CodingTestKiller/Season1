import sys
inp = sys.stdin.readline
a,b = map(int,inp().split())
ans = 1
while(b!=a):
    ans += 1
    tmp = b
    if b%10 == 1:
        b //= 10
    elif b%2 == 0:
        b //= 2
    if tmp == b:
        ans = -1
        break
print(ans)