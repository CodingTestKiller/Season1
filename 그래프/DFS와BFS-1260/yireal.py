import sys
from collections import deque
inp = sys.stdin.readline
def dfs(graph,ver,vis_list):
    vis_list.append(ver)
    graph[ver].sort()
    for i in graph[ver]:
        if i not in vis_list:
            dfs(graph,i,vis_list)
def bfs(graph,ver,vis_list):
    queue = deque([ver])
    vis_list.append(ver)
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if i not in vis_list:
                queue.append(i)
                vis_list.append(i)


n,m,v = map(int,inp().rstrip().split())
graph = [[]for _ in range(n+1)]
for i in range (m):
    start,end = map(int,inp().rstrip().split())
    graph[start].append(end)
    graph[end].append(start)
vis_list_dfs = []
vis_list_bfs = []
dfs(graph,v,vis_list_dfs)
bfs(graph,v,vis_list_bfs)
print(*vis_list_dfs)
print(*vis_list_bfs)