from collections import deque
import sys
input=sys.stdin.readline

def bfs(x):
    cnt=0
    v=[0]*(n+1)
    v[x]=1

    q=deque()
    q.append(x)
    while(q):         
        now=q.popleft()
        cnt+=1
        for nx in g[now]:
            if v[nx]==0:
                v[nx]=1
                q.append(nx)
    return cnt 


n,m=map(int, input().split())
g=[[] for _ in range(n+1)]

for i in range(m):
    a,b=map(int, input().split())
    g[b].append(a)


result=[]
for j in range(1,n+1):
    result.append(bfs(j))
    
ma=max(result)

for k in range(1,n+1):
    if ma==result[k-1]:
        print(k,end=" ")