from collections import deque
from sys import stdin
input = stdin.readline

n = int(input())
stones = [int(x) for x in input().split()]

left, right = 0, (n-1) * (abs(stones[0] - stones[-1]) + 1)


def is_possible(stones: list, power: int) -> bool:
    q = deque()
    q.append(0)
    visit = [False] * (n)
    visit[0] = True

    while q:
        index = q.pop()
        if index == n-1:
            return True

        for i in range(index+1, n):
            if (i-index) * (abs(stones[index] - stones[i])+1) <= power and not visit[i]:
                q.append(i)
                visit[i] = True

    return False


ans = 0
while left <= right:
    middle = (left + right) // 2

    if is_possible(stones, middle):
        right = middle - 1
        ans = middle
    else:
        left = middle + 1

print(ans)
