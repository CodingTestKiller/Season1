n = int(input())
left = 0
right = 2**63


while left <= right:
    mid = (left + right) // 2

    if mid * mid >= n:
        right = mid - 1
    else:
        left = mid + 1
print(left)
