import sys

input = sys.stdin.readline


def check(index, tree, depth, width, depth_width):
    left = tree[index - 1][0]
    right = tree[index - 1][1]

    if left != -1:
        width = check(left, tree, depth + 1, width, depth_width)
    depth_width[index - 1][0] = depth
    depth_width[index - 1][1] = width
    width += 1
    if right != -1:
        width = check(right, tree, depth + 1, width, depth_width)
    return width


n = int(input())
tree = [[0, 0] for _ in range(n)]
depth_width = [[0, 0] for _ in range(n)]
depth = 0
width = 0
child = []
root = 0

for _ in range(n):
    index, left, right = [int(x) for x in input().split()]
    tree[index - 1][0] = left
    tree[index - 1][1] = right
    child.append(left)
    child.append(right)

for i in range(n + 1):
    if i == 0:
        continue
    if i not in set(child):
        root = i
        break
check(root, tree, depth, width, depth_width)

dic = {}
for row in depth_width:
    key = row[0] + 1
    if key in dic.keys():
        dic[key].append(row[1])
    else:
        dic[key] = [row[1]]

max_width = 1
max_depth = 1
for i in range(len(dic)):
    value = dic[i + 1]
    width = max(value) - min(value) + 1
    if width > max_width:
        max_width = width
        max_depth = i + 1

print(max_depth, max_width)
