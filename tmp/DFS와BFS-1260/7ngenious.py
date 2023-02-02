from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[False] * (n + 1) for _ in range(n + 1)]

visited_DFS = [0] * (n + 1)
visited_BFS = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = True

def DFS(v):
    visited_DFS[v] = 1
    print(v, end = ' ')
    for i in range(1, n + 1):
        if(visited_DFS[i] == 0 and graph[v][i]):
            DFS(i)
def BFS(v):
    queue = deque([v])
    visited_BFS[v] = 1
    while queue:
        v = queue.popleft()
        print(v, end = ' ')

        for i in range(1, n + 1):
            if(visited_BFS[i] == 0 and graph[v][i]):
                queue.append(i)
                visited_BFS[i] = 1
DFS(v)
print()
BFS(v)
