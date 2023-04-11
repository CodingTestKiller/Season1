import sys

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

s, e = 1, N**2
while s <= e:
    mid = (s + e) // 2
    cnt = 0

    for i in range(1, N + 1):
        cnt += min(mid // i, N)

    if cnt >= k:
        e = mid - 1
    else:
        s = mid + 1
print(s)
#2h+