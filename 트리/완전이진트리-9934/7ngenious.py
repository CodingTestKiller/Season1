import sys
input = sys.stdin.readline

K = int(input())
num = list(map(int,input().split()))

ans = [[] for _ in range(K)]

def visit_tree(K, start, end):
    if start == end:
        ans[K].append(num[start])
        return

    m = (start + end) // 2

    ans[K].append(num[m])
    visit_tree(K+1, start, m-1)
    visit_tree(K+1, m+1, end) 

visit_tree(0, 0, len(num)-1)
for i in ans:
    for j in i:
        print(j,end=' ')
    print()