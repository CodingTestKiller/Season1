import sys
input = sys.stdin.readline

n = int(input())

def int_root(n):
    left = 0
    right = n

    while left <= right:
        mid = (left + right) // 2
        if mid**2 == n:
            return mid
        elif mid**2 < n:
            left = mid + 1
        else:
            right = mid - 1

    return left

ans = int_root(n)
print(ans)