# DP풀이
import sys
n = int(input())
L = [0] + list(map(int, input().split()))
dp = [0] * (n+1)
for i in range(n-1, 0, -1):
    M = sys.maxsize
    for j in range(i+1, n):
        M = min(M, max((j-i) * (1 + abs(L[i] - L[j])), dp[j]))
    M = min(M, (n-i) * (1 + abs(L[i]-L[n])))
    dp[i] = M
print(dp[1])

# DFS 풀이 (재귀)
sys.setrecursionlimit(10**6)
n = int(input())
L = [0] + list(map(int, input().split()))
left = 0
right = (n-1) * (1 + abs(L[n] - L[1]))


def DFS(i, mid):
    global flag
    if i == n:
        flag = 1
        return True
    for j in range(i+1, n+1):
        t = (j-i) * (1 + abs(L[i] - L[j]))
        if t <= mid and visit[j]:
            DFS(j, mid)
            visit[j] = False
        if flag == 1:
            return True
    return False


while left <= right:
    mid = (left+right)//2
    flag = 0
    stack = [1]
    visit = [True] * (n+1)
    visit[1] = False
    flag = 0
    DFS(1, mid)
    if flag == 1:
        right = mid-1
    else:
        left = mid + 1
print(left)

# DFS 스택 활용
n = int(input())
L = [0] + list(map(int, input().split()))
left = 0
right = (n-1) * (1 + abs(L[n] - L[1]))
while left <= right:
    mid = (left+right)//2
    flag = 0
    stack = [1]
    visit = [True] * (n+1)
    visit[1] = False

    while stack:
        i = stack.pop()
        if i == n:
            flag = 1
            break
        for j in range(i+1, n+1):
            t = (j-i) * (1 + abs(L[i] - L[j]))
            if t <= mid and visit[j]:
                stack.append(j)
                visit[j] = False
    if flag == 1:
        right = mid-1
    else:
        left = mid + 1
print(left)
