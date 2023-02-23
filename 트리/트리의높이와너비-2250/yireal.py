from sys import stdin
from typing import OrderedDict
inp = stdin.readline
n = int(inp().rstrip())
def in_order(ver):
    global num
    if ver:
        in_order(tree[ver][0])
        tree[ver][4] = num
        num += 1
        in_order(tree[ver][1])
def dfs(ver,depth):
    global max_depth
    vis[ver] = True
    tree[ver][3] = depth
    if max_depth < depth:
        max_depth = depth
    for i in range(2):
        if not vis[tree[ver][i]]:
            dfs(tree[ver][i],depth + 1)

tree = [[0,0,0,0,0] for _ in range(n+1)]
# left,right,parent,depth,wide
for _ in range(n):
    ver,left,right = map(int,inp().rstrip().split())
    if left == -1: left = 0
    if right == -1 : right = 0

    tree[ver][0] = left
    tree[ver][1] = right
    tree[left][2] = ver
    tree[right][2] = ver
vis = [False] * (n+1)
vis[0] = True

for i in range(1, n + 1):
    if tree[i][2] == 0:
        root = i
max_depth = 0
dfs(root,1)
num = 1
in_order(root)
depth_list = [[] for _ in range(max_depth + 1)]
for j in range(1,n+1):
    depth_list[tree[j][3]].append(tree[j][4])
result = []
for i in range(len(depth_list)):
    if len(depth_list[i]) <= 1:
        result.append(1)
    else:
        result.append(max(depth_list[i]) - min(depth_list[i]) + 1)
print(result.index(max(result),1),max(result))