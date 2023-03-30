import sys

N, d, k, c = map(int,sys.stdin.readline().split())
sushi = [int(sys.stdin.readline()) for _ in range(N)]
repeated = [0]*3001
repeated[c] = 1

for i in range(N):
    if i < k:
        repeated[sushi[i]] += 1

cnt = 0
answer = 0
for i in repeated:
    if i != 0:
        cnt+=1

for i in range(k,N+k):
    if i>N-1:
        i%=N
    repeated[sushi[i-k]] -= 1
    if repeated[sushi[i-k]] == 0:
        cnt -= 1
    repeated[sushi[i]] += 1
    if repeated[sushi[i]] == 1:
        cnt += 1
    answer = max(cnt, answer)

print(answer)
#1h