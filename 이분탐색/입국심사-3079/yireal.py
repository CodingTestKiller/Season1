import sys
inp = sys.stdin.readline
n,m = map(int,inp().split())
gate = [int(inp()) for _ in range(n)]
fast,slow = min(gate),max(gate) * m
ans = slow
while fast <= slow:
    fin = 0
    piv = (slow + fast) // 2
    for i in gate :
        fin += piv // i
        if fin >= m:
            break
    if fin >= m:
        ans = piv   
        slow = piv -1
    else:
        fast = piv +1
print(ans)