import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
p1, p2 = [int(x) for x in input().split(' ')]
m = int(input())

chon = [[] for _ in range(n+1)]
visit = [False for _ in range(n+1)]

for _ in range(m):
    x, y = [int(x) for x in input().split(' ')]
    chon[x].append(y)
    chon[y].append(x)
      

def bfs(p1, p2):
    q = deque()
    q.append(p1)
    cnt = 1

    while q:
        if cnt > n:
            print(-1)
            exit()
        for _ in range(len(q)):
            per = q.popleft()
            if p2 in chon[per]:
                print(cnt)
                exit()
            else:
                for p in chon[per]:
                    if visit[p] == False:
                        visit[p] = True
                        q.append(p)
            
        cnt += 1

    print(-1)

bfs(p1,p2)