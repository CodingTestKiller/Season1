from sys import stdin
input = stdin.readline
from collections import deque

n = int(input())

tree = [[] for _ in range(n + 1)]
parent = [[] for _ in range(n + 1)]
visit = [False for _ in range(n + 1)]

visit[1] = True

for _ in range(n - 1):
    x, y = [int(x) for x in input().split(' ')]
    tree[x].append(y)
    tree[y].append(x)


def bfs():
    q = deque()
    q.append(1)
    visit[1] = True

    while q:
        v = q.popleft()
        
        for num in tree[v]:
            if visit[num] == False:
                q.append(num)
                parent[num].append(v)
                visit[num] = True

bfs()

for nodes in parent[2:]:
    for value in nodes:
        print(value)