import sys
from collections import deque
inp = sys.stdin.readline
n,m,k,x = map(int,inp().split())
graph = [[0] for _ in range(n+1)]
visit = [0]
distance = [0]*(n+1)
def bfs():
    cnt = 0
    queue = deque([x])
    while queue :
        ver = queue.popleft()
        cnt += 1
        if cnt > k : break
        for i in graph[ver]:
            if i not in visit:
                queue.append(i)
                visit.append(i)
                distance[i] = cnt
    
for i in range(m):
    a,b = map(int,inp().split())
    graph[a].append(b)
bfs()
if k in distance:  
    for i in range(1,n+1):
        if k == distance[i]:
            print(i)
else:
    print(-1)