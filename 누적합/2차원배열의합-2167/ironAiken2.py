N, M = map(int, input().split())
# N, M = [int(x) for x in input().split(' ')]
arr = []
for i in range(N):
    arr.append([])
    arr[i] = list(map(int, input().split()))

K = int(input())
for _ in range(K):
    sum = 0
    i, j, x, y = map(int, input().split())
    for I in range(i - 1, x):
        for J in range(j - 1, y):
            sum += arr[I][J]
    print(sum)
