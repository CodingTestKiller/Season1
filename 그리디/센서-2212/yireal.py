import sys
inp = sys.stdin.readline
n = int(inp())
k = int(inp())
sens = list((map(int,inp().split())))
if n <= k:
    print(0)
    sys.exit()
sens.sort()
ran = []
for i in range(1,n):
    ran.append(sens[i] - sens[i-1])
ran.sort()
print(sum(ran[:n-k]))
     