from sys import stdin
input = stdin.readline

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

n = int(input())
cmd = [[str(x) for x in input().rstrip().split(' ')] for _ in range(n)]

root = node('A')
    
def make_tree(root):
    for Node in cmd:
        if Node[0] == root.data:
            if Node[1] != '.':
                left = node(Node[1])
                root.left = left
                make_tree(root.left)
            if Node[2] != '.':
                right = node(Node[2])
                root.right = right
                make_tree(root.right)

make_tree(root)


def preorder(root):
    print(root.data, end='')
    if root.left:
        preorder(root.left)
    if root.right:
        preorder(root.right)

def inorder(root):
    if root.left:
        inorder(root.left)
    print(root.data, end='')
    if root.right:
        inorder(root.right)

def postorder(root):
    if root.left:
        postorder(root.left)
    if root.right:
        postorder(root.right)
    print(root.data, end='')


preorder(root)
print('')
inorder(root)
print('')
postorder(root)

