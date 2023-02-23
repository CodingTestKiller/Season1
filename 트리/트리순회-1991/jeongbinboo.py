import sys

input = sys.stdin.readline


def preorder(tree_unit):
    print(tree_unit[0], end='')
    if tree_unit[1] != '.':
        preorder(node_list[ord(tree_unit[1]) - ord('A')])
    if tree_unit[2] != '.':
        preorder(node_list[ord(tree_unit[2]) - ord('A')])


def inorder(tree_unit):
    if tree_unit[1] != '.':
        inorder(node_list[ord(tree_unit[1]) - ord('A')])
    print(tree_unit[0], end='')
    if tree_unit[2] != '.':
        inorder(node_list[ord(tree_unit[2]) - ord('A')])


def postorder(tree_unit):
    if tree_unit[1] != '.':
        postorder(node_list[ord(tree_unit[1]) - ord('A')])
    if tree_unit[2] != '.':
        postorder(node_list[ord(tree_unit[2]) - ord('A')])
    print(tree_unit[0], end='')


n = int(input())
node_list = [['.' for _ in range(3)] for _ in range(n)]
for _ in range(n):
    row = [c for c in input().rstrip().split()]
    i = ord(row[0]) - ord('A')
    for j in range(3):
        node_list[i][j] = row[j]

preorder(node_list[0])
print('')
inorder(node_list[0])
print('')
postorder(node_list[0])
