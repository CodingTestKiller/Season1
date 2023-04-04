import sys
N, C = map(int,sys.stdin.readline().split())
M = int(sys.stdin.readline())

delivered = [0]*(N+1)
capacity = [0]*(N+1)
box=[]

for i in range(M):
    S,E,P = map(int, sys.stdin.readline().split())
    box.append([S,E,P])
box.sort(key=lambda x:x[0])
box.sort(key=lambda x:x[1])

for i in range(M):
    j = box[i][0]
    k = box[i][1]
    for l in range(j,k+1):
        if capacity[l]+box[i][2] > C:
            box[i][2] = C - capacity[l]
        capacity[l] = capacity[l] + box[i][2]
    delivered[k]+=box[i][2]
    capacity[k]-=box[i][2]

print(sum(delivered))
#2h