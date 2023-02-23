import sys
inp = sys.stdin.readline
def post_order(pre_order,in_order):
    if len(pre_order) == 0:
        return
    elif len(pre_order) == 1:
        print(pre_order[0],end=' ')
        return
    elif len(pre_order) == 2:
        print(pre_order[1],pre_order[0],end=' ')
        return
    root = in_order.index(pre_order[0])
    left_in = in_order[0:root]
    left_pre = pre_order[1:1+len(left_in)]
    post_order(left_pre,left_in)
    right_in = in_order[root+1:]
    right_pre = pre_order[len(left_pre)+1:]
    post_order(right_pre, right_in)

    print(pre_order[0], end=' ')
    
t = int(inp().rstrip())
for i in range(t):
    ans = []
    n = inp().rstrip().split()
    pre_order = list(map(int, input().split()))
    in_order = list(map(int, input().split()))
    
    post_order(pre_order,in_order)
    print()