n, m = [int(x) for x in input().split(' ')]

arr = [[int(x) for x in input().split(' ')] for _ in range(int(n))]

for i in range(n):
    for j in range(m):
        arr[i][j] += arr[i][j-1] if j > 0 else 0
        arr[i][j] += arr[i-1][j] if i > 0 else 0
        arr[i][j] -= arr[i-1][j-1] if i > 0 and j > 0 else 0

k = int(input())

for _ in range(k):
    x1, y1, x2, y2 = [int(x) - 1 for x in input().split(' ')]
    s = arr[x2][y2]
    s -= arr[x2][y1-1] if y1 > 0 else 0
    s -= arr[x1-1][y2] if x1 > 0 else 0
    s += arr[x1-1][y1-1] if x1 > 0 and y1 > 0 else 0
    print(s)
