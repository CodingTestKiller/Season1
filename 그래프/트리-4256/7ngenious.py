import sys
input = sys.stdin.readline

def postorder(root, start, end):
    for i in range(start, end):
        if inorder[i] == preorder[root]:
            postorder(root+1 ,start, i)
            postorder(root+1+(i-start) , i+1 , end)
            ans.append(preorder[root])

for i in range(int(input())):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    ans = []
    postorder(0, 0, n)
    print(*ans)