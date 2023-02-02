import sys
from collections import deque
inp = sys.stdin.readline
def dfs(graph,ver,vis):
    cnt = 1
    vis.append(ver)
    graph[ver].sort()
    for i in graph[ver]:
        if i not in vis:
            cnt += dfs(graph,i,vis)
    return cnt


def bfs(graph,ver,vis):
    cnt = 1
    queue = deque([ver])
    vis.append(ver)
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if i not in vis:
                queue.append(i)
                vis.append(i)
                cnt+=1
    return cnt
                
            
n,m = map(int,inp().rstrip().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,inp().rstrip().split())
    graph[b].append(a)
max = 0
ans = []

for i in range(1,n+1):
    vis = []
    tmp = dfs(graph,i,vis)
    if (max > tmp):
        continue
    elif(max == tmp):
        ans.append(i)
    else:
        max = tmp
        ans.clear()
        ans.append(i)

print(*ans)
