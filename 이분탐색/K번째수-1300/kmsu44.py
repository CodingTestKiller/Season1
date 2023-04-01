

n = int(input())
k = int(input())
left = 1
right = min(10**9, n * n)
while left <= right:
    mid = (left + right)//2
    cnt = 0
    for i in range(1, n+1):
        cnt += min(mid // i, n)
    if cnt >= k:
        right = mid - 1
    else:
        left = mid + 1
print(left)
