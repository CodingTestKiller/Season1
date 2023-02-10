from sys import stdin

input = stdin.readline

n = int(input())


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(inorder: list, preorder: list, current: int):
    root = Node(current)
    root_index = inorder.index(current)

    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index+1:]

    left_preorder = preorder[1:len(left_inorder)+1]
    right_preorder = preorder[len(left_inorder)+1:]

    if left_preorder:
        root.left = build_tree(left_inorder, left_preorder, left_preorder[0])
    if right_preorder:
        root.right = build_tree(
            right_inorder, right_preorder, right_preorder[0])
    return root


def postorder(root: Node):
    if root.left:
        postorder(root.left)
    if root.right:
        postorder(root.right)
    print(root.data, end=' ')


for _ in range(n):
    _ = input()
    preorder = [int(x) for x in input().split()]
    inorder = [int(x) for x in input().split()]
    root = build_tree(inorder, preorder, preorder[0])
    postorder(root)
    print()
