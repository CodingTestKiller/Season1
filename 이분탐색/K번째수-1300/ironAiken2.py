from sys import stdin
input = stdin.readline


n = int(input())
k = int(input())

left, right = 1, n ** 2


def find_k(n: int, v: int) -> int:
    cnt = 0

    for i in range(1, n+1):
        cnt += min(v // i, n)

    return cnt


ans = 0
while left <= right:
    middle = (left + right) // 2

    if find_k(n, middle) < k:
        left = middle + 1
    else:
        right = middle - 1
        ans = middle

print(ans)
