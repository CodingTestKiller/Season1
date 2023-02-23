import math
from sys import stdin

input = stdin.readline

n = int(input())

tree = {}

root = [0 for _ in range(n+1)]

for _ in range(n):
    p, l, r = [int(x) for x in input().split()]
    root[p] += 1
    if l != -1:
        root[l] += 1
    if r != -1:
        root[r] += 1
    tree[p] = [l, r]

root = root.index(1)

tree_map = [[] for _ in range(n)]
index = 0


def inorder(tree, current, depth):
    global index
    try:
        l, r = tree[current]
        if l != -1:
            inorder(tree, l, depth+1)
        tree_map[depth].append(index)
        index += 1
        if r != -1:
            inorder(tree, r, depth+1)
    except KeyError:
        return


inorder(tree, root, 0)

depth = n
length = 0


for i, row in enumerate(tree_map):
    try:
        current_len = row[-1]-row[0]+1
    except IndexError:
        break
    if length < current_len:
        length = current_len
        depth = i

print(depth+1, length)
