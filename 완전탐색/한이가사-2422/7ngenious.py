import sys
input=sys.stdin.readline

N,M = map(int,input().split())
arr = [[] for _ in range(N+1)]

for i in range(M):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

count=0

for i in range(1, N+1):
    for j in range(i+1, N+1):
        if i<j and j not in arr[i]:
            for k in range(j+1, N+1):
                if k not in arr[i] and k not in arr[j]:
                    count += 1

print(count)
