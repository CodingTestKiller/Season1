from collections import deque
import sys


class Node:
    def __init__(self, nodeNum):
        self.num = nodeNum
        self.left = None
        self.right = None


input = sys.stdin.readline
t = int(input())


def make_tree(head, pre_list, in_list):
    if len(pre_list) <= 1:
        return
    left_pre = deque()
    right_pre = deque()
    left_in = deque()
    right_in = deque()
    start_node = pre_list[0]
    break_point = in_list.index(start_node)
    for i, value in enumerate(in_list):
        if i < break_point:
            left_in.append(value)
        elif i > break_point:
            right_in.append(value)
    for value in pre_list:
        if value in left_in:
            left_pre.append(value)
        elif value in right_in:
            right_pre.append(value)
    if len(left_pre) != 0:
        left_node = Node(left_pre[0])
        head.left = left_node

    if len(right_pre) != 0:
        right_node = Node(right_pre[0])
        head.right = right_node
    make_tree(head.left, left_pre, left_in)
    make_tree(head.right, right_pre, right_in)


def post_order(node):
    if node.left:
        post_order(node.left)
    if node.right:
        post_order(node.right)
    print(node.num, end=' ')


for _ in range(t):
    n = int(input())
    pre_list = [0 for _ in range(n)]
    in_list = [0 for _ in range(n)]
    for i in range(2):
        nodes = [int(x) for x in input().split()]
        for j in range(n):
            if i == 0:
                pre_list[j] = nodes[j]
            else:
                in_list[j] = nodes[j]
    head = Node(pre_list[0])
    make_tree(head, pre_list, in_list)
    post_order(head)
