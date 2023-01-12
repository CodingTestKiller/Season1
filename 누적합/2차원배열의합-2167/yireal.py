import sys
N,M = map(int,sys.stdin.readline().rstrip().split())
table = list()
for i in range (N):
    table.append([])
    table[i] = list(map(int,sys.stdin.readline().rstrip().split()))
K = int(sys.stdin.readline().rstrip())
total = list()
for k in range(K):
    total.append(0)
    I,J,X,Y = map(int,sys.stdin.readline().rstrip().split())
    for i in range(I-1,X):
        total[k] += sum(table[i][J-1:Y])
print(*total,sep='\n')