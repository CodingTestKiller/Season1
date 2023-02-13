import sys

input_ = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

class Tree():
    def __init__(self):
        self.root = None
    
    def height(self, root):
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

N = int(input_().rstrip())
tree = Tree()
nodes = [None] + [Node(i) for i in range(1, N + 1)]
for i in range(N):
    now_node, left_data, right_data = [int(x) for x in input_().rstrip().split()]
    # if i == 0:
    #     tree.root = nodes[now_node]
    if left_data != -1:
        nodes[now_node].left = nodes[left_data]
    if right_data != -1:
        nodes[now_node].right = nodes[right_data]
