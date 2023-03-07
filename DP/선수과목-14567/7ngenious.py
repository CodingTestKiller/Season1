import sys
input = sys.stdin.readline

N,M = map(int,input().split())

arr = [1] * (N+1)

A = [0] * (M+1)
B = [0] * (M+1)
tmp = []

for i in range(M):
    A[i],B[i] = map(int,input().split())
    tmp.append((A[i],B[i]))
tmp.sort()

for a,b in tmp:
    if arr[b] <= arr[a]:
        arr[b] = arr[a] + 1

print(*arr[1:])
#리스트가 아닌 값을 출력하기 위해서