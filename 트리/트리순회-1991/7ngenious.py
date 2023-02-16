import sys
input = sys.stdin.readline

class Node:
    def __init__(data, left, right):
        data.left = left
        data.right = right

tree = dict()
A = ord('A')

def preorder(x):
    if x == -1:
        return
    print(chr(x+A),end='')
    preorder(tree[x].left)
    preorder(tree[x].right)
def inorder(x):
    if x == -1:
        return
    inorder(tree[x].left)
    print(chr(x+A),end='')
    inorder(tree[x].right)
def postorder(x):
    if x == -1:
        return
    postorder(tree[x].left)
    postorder(tree[x].right)
    print(chr(x+A),end='')

n = int(input())

for _ in range(n):
    x, y, z = input().split()
    x = ord(x)-A
    left = -1
    right = -1
    if y != '.':
        left = ord(y)-A
    if z != '.':
        right = ord(z)-A
    tree[x] = Node(left, right)
    
preorder(0)
print()
inorder(0)
print()
postorder(0)
print()
