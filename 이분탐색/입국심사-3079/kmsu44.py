import sys
n, m = map(int, input().split())

T_list = []
for i in range(n):
    T_list.append(int(input()))

left = 0
right = sys.maxsize
while left <= right:
    mid = (left + right) // 2
    num = 0
    for i in T_list:
        num += mid // i
    if num >= m:
        right = mid - 1
    else:
        left = mid + 1
print(left)
