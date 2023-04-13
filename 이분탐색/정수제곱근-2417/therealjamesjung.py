from sys import stdin

input = stdin.readline

n = int(input())
start = 0
end = n

while start < end:
    mid = (start + end) // 2

    if mid ** 2 == n:
        print(mid)
        exit()
    elif mid ** 2 < n:
        start = mid + 1
    else:
        end = mid - 1


# print(start, mid, end)

if start ** 2 <= n:
    print(start + 1)
else:
    print(start)
