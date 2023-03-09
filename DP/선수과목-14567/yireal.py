import sys
from collections import deque
inp = sys.stdin.readline
n,m = map(int,inp().split())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
dp = [0] * (n+1)
for i in range(m):
    a,b = map(int,inp().split())
    graph[a].append(b)
    indegree[b] += 1

result = [1]*(n+1)
queue = deque()
for i in range(1,n+1):
    if indegree[i] == 0 :
        queue.append(i)
while queue:
    do = queue.popleft()
    for i in graph[do]:
        indegree[i] -= 1
        if indegree[i] == 0:
            result[i] = result[do] + 1
            queue.append(i)
print(*result[1:])