from sys import stdin
input = stdin.readline

n = int(input())

start = 0
end = 2 ** 32

while start < end:
    mid = (end + start) // 2

    if mid ** 2 < n:
        start = mid + 1
    else:
        end = mid - 1

if start ** 2 >= n:
    print(start)
else:
    print(start + 1)
