from sys import stdin
from bisect import bisect

input = stdin.readline

n = int(input())
tree_len = 2**n-1

tree = [int(x) for x in input().split()]


def print_tree(tree, depth, tree_len, n, result):
    if depth == n:
        return
    result[depth].append(tree[int(tree_len / 2)])
    print_tree(tree[:int(tree_len / 2)], depth+1, int(tree_len / 2), n, result)
    print_tree(tree[int(tree_len / 2)+1:], depth +
               1, int(tree_len / 2), n, result)


result = [[] for _ in range(n)]
print_tree(tree, 0, tree_len, n, result)
[print(' '.join(str(y) for y in x)) for x in result]
