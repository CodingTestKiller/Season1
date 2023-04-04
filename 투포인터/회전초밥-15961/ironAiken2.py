from collections import Counter
from sys import stdin
input = stdin.readline

n, d, k, c = [int(x) for x in input().split()]

rail = [int(input()) for _ in range(n)]

dic = {}

for data in Counter(rail):
    dic[data] = 0

start = 0
end = 0
cnt = 0

for i in range(k):
    if dic[rail[end]] == 0:
        cnt += 1
    dic[rail[end]] += 1
    end += 1

    if end == n:
        end = 0

if start == end:
    try:
        if dic[c] == 0:
            cnt += 1
    except:
        cnt += 1

    print(cnt)
    exit()

ans = 0

while start < n:
    ans = max(ans, cnt)

    if end == n:
        end = 0

    try:
        if dic[c] == 0:
            ans = max(ans, cnt + 1)
    except:
        ans = max(ans, cnt + 1)

    dist = end - start if end >= start else end - start + n

    if dist < k:
        if dic[rail[end]] == 0:
            cnt += 1
        dic[rail[end]] += 1
        end += 1
    else:
        dic[rail[start]] -= 1
        if dic[rail[start]] == 0:
            cnt -= 1
        start += 1

print(ans)
