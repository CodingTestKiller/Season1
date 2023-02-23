from sys import stdin

input = stdin.readline

n = int(input())
tree = {}

for _ in range(n):
    p, l, r = [x for x in input().strip().split()]
    tree[p] = [l, r]


def preorder(tree, current):
    try:
        l, r = tree[current]
        print(current, end='')
        if l != '.':
            preorder(tree, l)
        if r != '.':
            preorder(tree, r)
    except KeyError:
        return


def inorder(tree, current):
    try:
        l, r = tree[current]
        if l != '.':
            inorder(tree, l)
        print(current, end='')
        if r != '.':
            inorder(tree, r)
    except KeyError:
        return


def postorder(tree, current):
    try:
        l, r = tree[current]
        if l != '.':
            postorder(tree, l)
        if r != '.':
            postorder(tree, r)
        print(current, end='')
    except KeyError:
        return


preorder(tree, 'A')
print()
inorder(tree, 'A')
print()
postorder(tree, 'A')
