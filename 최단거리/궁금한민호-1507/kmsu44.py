from itertools import combinations
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]


edge_list = list(combinations([i for i in range(n)], 2))
alive = []
answer = 0
for idx, edge in enumerate(edge_list):
    i, j = edge
    w = graph[i][j]
    flag = 0
    for k in range(n):
        if i == k or k == j:
            continue
        if w == graph[i][k] + graph[k][j]:
            flag = 1
        if w > graph[i][k] + graph[k][j]:
            print(-1)
            exit()
    if flag == 0:
        answer += graph[i][j]

print(answer)
