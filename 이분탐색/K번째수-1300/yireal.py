import sys
inp = sys.stdin.readline
n = int(inp())
k = int(inp())
front = 1
rear = k
while front <= rear:
    piv = (front + rear) // 2
    tmp = 0
    for i in range(1,n+1):
        tmp += min(piv//i,n)
    if tmp >= k:
        ans = piv
        rear = piv - 1
    else:
        front = piv + 1
print(ans)