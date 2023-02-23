# 솔루션 봄

import sys

input_ = sys.stdin.readline

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
        self.parent = -1


def inorder(node, level):
    global level_depth, x
    level_depth = max(level_depth, level)
    
    if node.left != -1:
        inorder(tree[node.left], level + 1)
    level_min[level] = min(level_min[level], x)
    level_max[level] = max(level_max[level], x)
    x += 1
    if node.right != -1:
        inorder(tree[node.right], level + 1)

N = int(input_().rstrip())
tree = {}
level_min = [N]
level_max = [0]
root = -1
x = 1
level_depth = 1

for i in range(1, N + 1):
    tree[i] = Node(i, -1, -1)
    level_min.append(N)
    level_max.append(0)
    
for _ in range(N):
    number, left_node, right_node = [int(x) for x in input_().rstrip().split()]
    tree[number].left = left_node
    tree[number].right = right_node
    
    if left_node != -1:
        tree[left_node].parent = number
    if right_node != -1:
        tree[right_node].parent = number
        
for i in range(1, N + 1):
    if tree[i].parent == -1:
        root = i
        
inorder(tree[root], 1)

result_level = 1
result_width = level_max[1] - level_min[1] + 1

for i in range(2, level_depth + 1):
    width = level_max[i] - level_min[i] + 1
    if result_width < width:
        result_level = i
        result_width = width
        
print(result_level, result_width)