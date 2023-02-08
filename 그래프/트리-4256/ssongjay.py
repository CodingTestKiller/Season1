import sys

input_ = sys.stdin.readline

T = int(input_().rstrip())


# preorder에서는 root를
# inorder에서는 트리를 나눈다
def get_postorder(preorder, inorder, start, end):
    if start > end:
        return
    root = preorder[0]
    preorder.pop(0)
    root_index = inorder.index(root)
    get_postorder(preorder, inorder, start, root_index - 1)
    get_postorder(preorder, inorder, root_index + 1, end)
    print(root, end=" ")


for _ in range(T):
    N = int(input_().rstrip())
    graph = [[] for _ in range(N + 1)]
    preorder = [int(x) for x in input_().rstrip().split()]
    inorder = [int(x) for x in input_().rstrip().split()]
    get_postorder(preorder, inorder, 0, N - 1)
    print()
