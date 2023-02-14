import sys
sys.setrecursionlimit(10**6)
inp = sys.stdin.readline
def dfs(tree,ver,vis,parent):
    vis[ver] = True
    for i in tree[ver]:
        if not vis[i]:
            parent[i] = ver
            dfs(tree,i,vis,parent)


n = int(inp().rstrip()) 
tree = [[] for _ in range(n+1)]
parent = [0]*(n+1)
vis=[False]*(n+1)
for _ in range(n-1):
    a,b = map(int,inp().rstrip().split())
    tree[a].append(b)
    tree[b].append(a)
dfs(tree,1,vis,parent)
for i in range(2,len(parent)):
    print(parent[i])

