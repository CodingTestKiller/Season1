from sys import stdin
input = stdin.readline

t = int(input())

def make_tree():
    while preorder:

        lchild = []
        rchild = []

        root = preorder[0]
        del preorder[0]

        flag = False
        for node in inorder:
            if node == root:
                flag = True
                continue
            if not flag:
                lchild.append(node)
            else:
                rchild.append(node)


        inorder.remove(root)
    
        if len(lchild) != 0:
            if not visit[preorder[0]]:
                tree[root][0] = preorder[0]
                visit[preorder[0]] = True

        if len(rchild) != 0:
            if not visit[preorder[len(lchild)]]:
                tree[root][1] = preorder[len(lchild)]
                visit[preorder[len(lchild)]] = True



def postorder(root):
    if tree[root][0] != 0:
        postorder(tree[root][0])
    if tree[root][1] != 0:
        postorder(tree[root][1])
    output.append(root)

ans = []
for _ in range(t):
    n = int(input())
    output = []
    tree = [[0, 0] for _ in range(n + 1)]
    visit = [0 for _ in range(n + 1)]

    preorder = [int(x) for x in input().strip().split(' ')]
    inorder = [int(x) for x in input().strip().split(' ')]
    
    root = preorder[0]
    visit[root] = True

    make_tree()
    
    postorder(root)
    ans.append(output)

for a in ans:
  print(" ".join(list(map(str, a))))

    