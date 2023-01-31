from sys import stdin
input = stdin.readline

n, m = [int(x) for x in input().split(' ')]

com = [[] for _ in range(n)]

for _ in range(m):
    a, b = [int(x) for x in input().split(' ')]
    com[b-1].append(a)


def bfs(num):
    cnt = 1
    q = []
    q.append(num)
    visit = [0 for _ in range(n)]
    visit[num-1] = 1

    while len(q) > 0:
        c = q[0]
        cnt += 1
        q.remove(c)

        for nc in com[c-1]:
            if visit[nc-1] == 0:
                q.append(nc)
                visit[nc-1] = 1

    return cnt


max_cnt = 0
ans = []

for i in range(1, n + 1):
    cnt = bfs(i)
    bfs(i)
    if cnt > max_cnt:
        max_cnt = cnt
        ans.clear()
        ans.append(i)
    elif cnt == max_cnt:
        ans.append(i)

print(*ans)
