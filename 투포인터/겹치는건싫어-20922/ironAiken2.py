from collections import Counter
from sys import stdin
input = stdin.readline

n, k = [int(x) for x in input().split()]

a = [int(x) for x in input().split()]

count = {}
for data in Counter(a):
    count[data] = 0
# 이부분 set 사용 가능
# set 함수는 unique 한 값을 가지기 때문


start = 0
end = 0
ans = 0


while end < n:

    if count[a[end]] < k:
        count[a[end]] += 1
        end += 1

    else:
        count[a[start]] -= 1
        start += 1
    ans = max(end-start, ans)


print(ans)
