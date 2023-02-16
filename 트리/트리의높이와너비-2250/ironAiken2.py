from sys import stdin
input = stdin.readline
from collections import deque

n = int(input())
tree = [[] for _ in range(n + 1)]
child = []

for _ in range(n):
    root, left, right = [int(x) for x in input().split(' ')]
    tree[root].append(left)
    tree[root].append(right)

    if left != -1:
        child.append(left)
    if right != -1:
        child.append(right)

for i in range(1, len(tree)):
    if i not in child:
        r = i
        break

print(i)


order = []

def inorder(root):
    if tree[root][0] != -1:
        inorder(tree[root][0])
    order.append(root)    
    if tree[root][1] != -1:
        inorder(tree[root][1])

level = [[]]

def levelorder(root):
    q = deque()
    q.append(root)
    depth = 0

    while q:
        depth += 1
        level.append([])
        length = len(q)
        for _ in range(length):
            node = q.popleft()
            level[depth].append(node)
            if tree[node][0] != -1:
                q.append(tree[node][0])
            if tree[node][1] != -1:
                q.append(tree[node][1])
            
inorder(r)
levelorder(r)

print(tree)
print(level)
print(r)

ans = []

for nodes in level[1:]:
    min_index = order.index(nodes[0]) + 1
    max_index = order.index(nodes[0]) + 1

    for node in nodes:
        i = order.index(node) + 1
        if i > max_index:
            max_index = i
        if i < min_index:
            min_index = i
    
    ans.append(max_index - min_index + 1)

print(ans.index(max(ans)) + 1, max(ans))