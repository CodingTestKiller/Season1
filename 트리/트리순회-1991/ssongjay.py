import sys

input_ = sys.stdin.readline


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(nodes, index):
    Node = nodes[index]
    print(Node.data, end="")
    if Node.left != None:
        i = ord(Node.left.data) - ord("A")
        preorder(nodes, i)
    if Node.right != None:
        i = ord(Node.right.data) - ord("A")
        preorder(nodes, i)


def inorder(nodes, index):
    Node = nodes[index]
    if Node.left != None:
        i = ord(Node.left.data) - ord("A")
        inorder(nodes, i)
    print(Node.data, end="")
    if Node.right != None:
        i = ord(Node.right.data) - ord("A")
        inorder(nodes, i)


def postorder(nodes, index):
    Node = nodes[index]
    if Node.left != None:
        i = ord(Node.left.data) - ord("A")
        postorder(nodes, i)
    if Node.right != None:
        i = ord(Node.right.data) - ord("A")
        postorder(nodes, i)
    print(Node.data, end="")


N = int(input_().rstrip())
num_A = ord("A")
nodes = [None] * (ord("Z") - ord("A") + 1)
for i in range(N):
    head, left, right = [x for x in input_().rstrip().split()]
    index = ord(head) - num_A
    nodes[index] = Node(head)
    if left != ".":
        left_index = ord(left) - num_A
        if nodes[left_index] == None:
            nodes[left_index] = Node(left)
        nodes[index].left = nodes[left_index]
    if right != ".":
        right_index = ord(right) - num_A
        if nodes[right_index] == None:
            nodes[right_index] = Node(right)
        nodes[index].right = nodes[right_index]


preorder(nodes, 0)
print()
inorder(nodes, 0)
print()
postorder(nodes, 0)