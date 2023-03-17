from collections import deque
a, b = map(int, input().split())


def BFS(a, b):
    q = deque()
    q.append((a, b, 1))
    while q:
        a, b, cnt = q.popleft()
        if a == b:
            return cnt
        if b <= 0:
            break
        if b % 10 == 1:
            q.append((a, b//10, cnt+1))
        if b % 2 == 0:
            q.append((a, b//2, cnt + 1))
    return -1


print(BFS(a, b))
