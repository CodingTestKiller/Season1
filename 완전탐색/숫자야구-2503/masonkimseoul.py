from collections import deque
from itertools import permutations
import sys

def judge(x,y):
    x=list(str(x))
    y=list(str(y))
    s=0
    b=0
    for i in x:
        if i in y:
            if i==y[int(x.index(i))]:
                s+=1
            else:
                b+=1
    return (s,b)

N=int(sys.stdin.readline())
answer=[100*i[0]+10*i[1]+i[2] for i in list(permutations([1,2,3,4,5,6,7,8,9],3))]
#0 들어간 케이스를 만들지 않기 위함
tmp=deque()
#answer에서 불가능한 경우의 수 제거용 임시 덱
for i in range(N):
    test,st,bt=map(int,sys.stdin.readline().split())
    for j in range(123,988):
        if judge(test,j)!=(st,bt):
            tmp.append(j)
    while tmp:
        j=tmp.pop()
        if j in answer:
            answer.remove(j)

print(len(answer))