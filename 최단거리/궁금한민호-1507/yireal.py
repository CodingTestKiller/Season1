import sys
import heapq
inp = sys.stdin.readline
n = int(inp())
graph = []
check = [[1]*n for i in range(n)]
result = 0
for _ in range(n):
    graph.append(list(map(int,inp().split())))
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == k or j == k or i == j:
                continue
            if graph[i][j] == graph[k][j] + graph[i][k]:
                check[i][j] = 0
            elif graph[i][j] > graph[k][j] + graph[i][k]:
                result = -1
if result != -1:
    for i in range(n):
        for j in range(i,n):    
            if check[i][j]:
                result += graph[i][j]
print(result)