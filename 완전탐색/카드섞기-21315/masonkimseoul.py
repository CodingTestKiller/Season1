import sys
from collections import deque

def reverse2K(shuffled,K):
    i=0
    tmp1=deque()
    tmp2=deque()
    while i<K:
        for j in range(pow(2,i)):
            tmp1.append(shuffled.popleft())
        for j in range(pow(2,i)):
            tmp2.append(shuffled.popleft())
        while tmp1:
            shuffled.appendleft(tmp1.pop())
        while tmp2:
            shuffled.appendleft(tmp2.pop())
        i+=1
    for j in range(pow(2,i)):
        tmp1.append(shuffled.popleft())
    while tmp1:
        shuffled.append(tmp1.popleft())
    return shuffled

N=int(sys.stdin.readline())
cardsOriginal=deque(map(int,sys.stdin.readline().split()))
cardsShuffled=cardsOriginal.copy()
cardsInitial=list(range(1,N+1))


first=1
second=1
flag=0
while pow(2,first)<N:
    second=1
    while pow(2,second)<N:
        cardsShuffled=reverse2K(cardsShuffled,second)
        cardsShuffled=reverse2K(cardsShuffled,first)
        if list(cardsShuffled)==cardsInitial:
            flag=1
            break
        else:
            second+=1
            cardsShuffled=cardsOriginal.copy()
    if flag!=1:
        first+=1
    else:
        break
print(first,second)