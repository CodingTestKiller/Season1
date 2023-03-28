import sys
input = sys.stdin.readline

N, K = map(int, input().split())
numbers = list(map(int, input().split()))

i, j = 0, 0

tmp = [0 for _ in range(max(numbers) + 1)]

ans = 0
while True:
    if i >= N:
        break
    if tmp[numbers[i]] < K:
        tmp[numbers[i]] += 1
        i += 1
    else:
        tmp[numbers[j]] -= 1
        j += 1
    
    ans = max(ans, i - j)
print(ans)