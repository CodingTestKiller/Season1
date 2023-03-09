n = int(input())
L = [0]
for i in range(n):
    L.append(int(input()))
# 0 가능 1 불가능 2 이전까지 최대값
Memo = [[0] * (n+1) for _ in range(3)]

if n == 1:
    print(L[1])
    exit()

Memo[0][1] = L[1]
Memo[2][1] = L[1]

if n == 2:
    print(L[1]+L[2])
    exit()
Memo[0][2] = L[2]
Memo[1][2] = L[1] + L[2]
Memo[2][2] = L[1] + L[2]
for i in range(3, n+1):
    Memo[0][i] = Memo[2][i-2] + L[i]
    Memo[1][i] = Memo[0][i-1] + L[i]
    Memo[2][i] = max(Memo[0][i], Memo[1][i], Memo[2][i-1])
print(Memo[2][n])
