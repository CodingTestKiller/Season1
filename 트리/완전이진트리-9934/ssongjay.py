import sys
from collections import deque

input_ = sys.stdin.readline


K = int(input_().rstrip())

inorder = [int(x) for x in input_().rstrip().split()]
tree = [[] for _ in range(2 ** K)]
visited = [False] * (2 ** K)


def put_root_node(inorder, tree, parent_node):
    root_index = len(inorder) // 2
    tree[parent_node].append(inorder[root_index])


def get_complete_binary_tree(inorder, tree):
    if len(inorder) < 2:
        return
    root_index = len(inorder) // 2
    put_root_node(inorder[:root_index], tree, inorder[root_index])
    put_root_node(inorder[root_index + 1:], tree, inorder[root_index])
    get_complete_binary_tree(inorder[:root_index], tree)
    get_complete_binary_tree(inorder[root_index + 1:], tree)


def print_node(v, i, total, cnt):
    if i == 0:
        print(v)
        cnt[0] += 1
    elif 2 ** cnt[0] + total[0] == i:
        print(v)
        total[0] = 2 ** cnt[0]
        cnt[0] += 1
    else:
        print(v, end=" ")


def bfs(graph, start, visited):
    cnt = [0]
    total = [0]
    index = 0
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print_node(v, index, total, cnt)
        index += 1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


root_index = len(inorder) // 2
get_complete_binary_tree(inorder, tree)

bfs(tree, inorder[root_index], visited)
