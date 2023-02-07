from sys import stdin
input = stdin.readline


def DFS(vertice, visit_list, n):
    print(n, end=' ')
    visit_list[n-1] = 1

    for node in vertice[n-1][1]:
        if visit_list[node - 1] == 0:
            DFS(vertice, visit_list, node)


def BFS(vertice, visit_list, n):
    q = []
    q.append(n)
    visit_list[n-1] = 1
    while len(q) > 0:
        n = q[0]
        print(n, end=' ')
        q.remove(n)

        for node in vertice[n-1][1]:
            if (visit_list[node-1] == 0):
                q.append(node)
                visit_list[node-1] = 1


n, m, v = [int(x) for x in input().split(' ')]

vertice = [[i + 1, []] for i in range(n)]
visit_list = [0 for _ in range(n)]
visit_list2 = [0 for _ in range(n)]


for _ in range(m):
    v1, v2 = [int(x) for x in input().split(' ')]

    vertice[v1 - 1][1].append(v2)
    vertice[v2 - 1][1].append(v1)

for node in vertice:
    node[1].sort()


DFS(vertice, visit_list, v)
print()
BFS(vertice, visit_list2, v)
