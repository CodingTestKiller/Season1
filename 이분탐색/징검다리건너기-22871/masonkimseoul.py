import sys

N = int(sys.stdin.readline())
rocks = [0] + list(map(int,sys.stdin.readline().split()))

s, e = 0, (N - 1) * (1 + abs(rocks[N] - rocks[1]))

while s <= e:
    mid = (s + e) // 2
    is_visited = [False] * (N + 1)
    is_visited[1] = True

    for i in range(2, N + 1):
        for j in range(1, i):
            power = (i - j) * (1 + abs(rocks[i] - rocks[j]))
            if is_visited[j] and power <= mid:
                is_visited[i] = True
                break

    if is_visited[N]:
        e = mid - 1
        K = mid
    else:
        s = mid + 1
print(K)
#2h+
