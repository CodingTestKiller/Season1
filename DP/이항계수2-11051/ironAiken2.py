from sys import stdin
input = stdin.readline

# (N K) -> N!/K!(N-K)!
# bottom-up 방식으로 구현

n, k = [int(x) for x in input().split()]

d = [0] * 1001
d[0] = 1
d[1] = 1

for i in range(2,n+1):
    d[i] = d[i - 1] * i

print(int((d[n]//(d[k]*d[n-k]))%10007))