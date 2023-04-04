import sys

N,M=map(int,sys.stdin.readline().split())
territory=[[0]*(M+1)]+[[0]+list(map(int,sys.stdin.readline().split())) for _ in range(N)]
T=int(sys.stdin.readline())

for i in range(1,N+1):
    for j in range(1,M+1):
        territory[i][j]+=territory[i][j-1]
    for j in range(1,M+1):
        territory[i][j]+=territory[i-1][j]

for _ in range(T):
    xy=list(map(int,sys.stdin.readline().split()))
    print(territory[xy[2]][xy[3]]-territory[xy[2]][xy[1]-1]-territory[xy[0]-1][xy[3]]+territory[xy[0]-1][xy[1]-1])

#20m