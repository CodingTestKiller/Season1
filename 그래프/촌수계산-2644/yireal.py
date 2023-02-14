from sys import stdin
inp = stdin.readline

total = 0
def dfs(graph,ver,vis,des,cnt):
    global total
    vis.append(ver)
    for i in graph[ver]:
        if i not in vis:
            if(i == des):
                total = cnt
                return
            dfs(graph,i,vis,des,cnt+1)


n = int(inp().rstrip())
a,b = map(int,inp().rstrip().split())
m = int(inp().rstrip())
graph = [[] for _ in range(n+1)]
for i in range(m):
    x,y = map(int,inp().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)
for i in range(1,n+1):
    graph[i].sort()
vis = list()
dfs(graph,a,vis,b,1)
if(total == 0):
    print(-1)
else:
    print(total)

