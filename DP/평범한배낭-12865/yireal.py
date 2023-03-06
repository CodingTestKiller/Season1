import sys
inp = sys.stdin.readline
n,k = map(int,inp().split())
bag = [[0]*(k+1) for _ in range(n+1)]
item = []
for i in range(n):
    w,v = map(int,inp().split())
    item.append((w,v))
for i in range(1,n+1):
    for j in range(1,k+1):
        if(item[i-1][0] <= j):
            bag[i][j] = max(item[i-1][1] + bag[i-1][j-item[i-1][0]],bag[i-1][j])
        else:
            bag[i][j] = bag[i-1][j]
print(bag[i][j])
