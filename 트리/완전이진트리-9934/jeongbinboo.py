"""
상근이가 중위탐색으로 댕김
주어진 입력값도 중위탐색임
중간값들을 출력하자
"""

from collections import deque
import sys

input = sys.stdin.readline
queue = deque()
k = int(input())
node_arr = [int(i) for i in input().split()]
queue.append(node_arr)
prev_len = len(node_arr)
while queue:
    target = queue.popleft()
    target_len = len(target)
    mid_index = target_len // 2
    if target_len != prev_len:
        print("")
        prev_len = target_len
    print(target[mid_index], end=' ')
    if target_len == 1:
        continue
    left = target[0: mid_index]
    right = target[mid_index + 1: target_len]
    queue.append(left)
    queue.append(right)
