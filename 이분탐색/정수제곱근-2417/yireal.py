import sys
inp = sys.stdin.readline
n = int(inp())
small = 0
big = n
while small <= big:
    piv = (small + big)//2
    if piv ** 2 < n:
        small = piv + 1
    else:
        big = piv -1
print(small)