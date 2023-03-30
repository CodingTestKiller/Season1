import sys

N, M = map(int,sys.stdin.readline().split())
list_N = list(map(int,sys.stdin.readline().split()))
list_M = list(map(int,sys.stdin.readline().split()))
answer=[]

i = j = 0
while i < N and j < M:
    if list_N[i] < list_M[j]:
        answer.append(list_N[i])
        i += 1
    else:
        answer.append(list_M[j])
        j += 1

while i < N:
    answer.append(list_N[i])
    i += 1
while j < M:
    answer.append(list_M[j])
    j += 1

print(*answer)
#5m