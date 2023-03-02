import sys
inp = sys.stdin.readline
t = int(inp())
ans = []

for k in range(t):
    n = int(inp())
    coin = list(map(int,inp().split()))
    m = int(inp())
    pos = [0] * (m+1)
    pos[0] = 1
    for i in coin:
        for j in range(1,m+1):
            if j >= i:
                pos[j] += pos[j-i]
    print(pos[m])
