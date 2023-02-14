from collections import deque
from platform import node
import sys


class Node:
    def __init__(self, nodeNum):
        self.num = nodeNum
        self.connectedNode = None

    def connect(self, connectedNode):
        current = self
        while current.connectedNode != None:
            current = current.connectedNode
        current.connectedNode = connectedNode


input = sys.stdin.readline

n = int(input())
parent_list = [0 for _ in range(n)]
parent_list[0] = -1
node_list = [Node(i) for i in range(n)]
is_visited = [0 for _ in range(n)]


def bfs():
    queue = deque()
    queue.append(0)

    while queue:
        index = queue.popleft()
        head = node_list[index]
        current = node_list[index]
        is_visited[index] = 1
        while current != None:
            if parent_list[current.num] == 0:
                if parent_list[head.num] != 0:
                    parent_list[current.num] = head.num + 1
            if is_visited[current.num] == 0:
                queue.append(current.num)
            current = current.connectedNode


for i in range(n - 1):
    num1, num2 = [int(x) for x in input().split()]
    node_list[num1 - 1].connect(Node(num2 - 1))
    node_list[num2 - 1].connect(Node(num1 - 1))
bfs()
for index, parent in enumerate(parent_list):
    if index != 0:
        print(parent)
