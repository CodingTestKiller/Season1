#솔루션 봄
import sys
input = sys.stdin.readline

N = int(input())
parent = [False] * (N + 1)
children = [[] for _ in range(N + 1)]
root = 0
left_col_for_level = [0] *(N + 1)  
max_width = [N, 0]  

for _ in range(N):
    p, c1, c2 = map(int, input().split())
    if c1 != -1:
        parent[c1] = True
    if c2 != -1:
        parent[c2] = True
    children[p] = (c1, c2)

for i in range(1, N + 1):
    if not parent[i]:
        root = i
        break

def save_col(level, col):
    global max_width
    
    if not left_col_for_level[level]:
        left_col_for_level[level] = col
    
    diff = col - left_col_for_level[level] + 1
    if diff > max_width[1]:
        max_width = [level, diff]
    elif diff == max_width[1] and max_width[0] > level:
        max_width = [level, diff]

def inorder(v, col, level):
    left, right = children[v]
    if left != -1:
        col = inorder(left, col, level + 1)

    save_col(level, col)
    col += 1

    if right != -1:
        col = inorder(right, col, level + 1)

    return col


inorder(root, 1, 1)

print(*max_width)
