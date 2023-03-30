import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())

sushi = []
for _ in range(N):
    sushi.append(int(input()))

sushi += sushi[:k-1]
tmp = [0]*(d+1)
tmp[c] = 1

ans, start, end, cnt = 0, 0, 0, 1


while True:
    if end-start == k:
        tmp[sushi[start]] -= 1
        if tmp[sushi[start]] == 0:
            cnt -= 1
        start += 1
        if start == N:
            break
    end += 1
    tmp[sushi[end-1]] += 1
    if tmp[sushi[end-1]] == 1:
        cnt += 1
    
    ans = max(cnt, ans)

print(ans)