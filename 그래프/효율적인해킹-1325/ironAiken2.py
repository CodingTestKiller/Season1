from collections import deque
from sys import stdin
input = stdin.readline

n, m = [int(x) for x in input().split(' ')]

com = [[] for _ in range(n)]

for _ in range(m):
    a, b = [int(x) for x in input().split(' ')]
    com[b-1].append(a)


def bfs(num):
    cnt = 1
    q = deque()
    q.append(num)
    visit = [False for _ in range(n)]
    visit[num-1] = True

    while len(q) > 0:
        c = q.popleft()
        cnt += 1

        for nc in com[c-1]:
            if visit[nc-1] == 0:
                q.append(nc)
                visit[nc-1] = True

    return cnt


max_cnt = 0
ans = []

for i in range(1, n + 1):
    cnt = bfs(i)
    if cnt > max_cnt:
        max_cnt = cnt
        ans.clear()
        ans.append(i)
    elif cnt == max_cnt:
        ans.append(i)

print(*ans)

# https://velog.io/@aurora_97/%EB%B0%B1%EC%A4%80-1325%EB%B2%88-%ED%9A%A8%EC%9C%A8%EC%A0%81%EC%9D%B8-%ED%95%B4%ED%82%B9-Python
