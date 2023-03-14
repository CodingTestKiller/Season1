import sys
from itertools import combinations

N, M = map(int,sys.stdin.readline().split())
flavors=list(range(1,N+1))
all_combi = set(tuple(combinations(flavors,3)))

for i in range(M):
    a, b = map(int,sys.stdin.readline().split())
    for j in range(1,N+1):
        if a != j and b != j:
            tmp = tuple(sorted([a, b, j]))
            all_combi.discard(tmp)
#tuple로 넣어야 set 가능
#set에서 discard를 통해 버림 가능, remove는 만약 그 값이 없으면 key error발생

print(len(all_combi))

#2h