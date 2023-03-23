import sys
input = sys.stdin.readline

N, C =  map(int, input().split())
M = int(input())

infos = []

# for _ in range(M):
#     s, r, box = map(int, input().split())
#     infos.append((s, r, box))
# infos.sort(key=lambda x :  x[1])
infos = sorted([list(map(int,input().split())) for _ in range(M)],
                key=lambda x: x[1])

cap = [C]*N
ans = 0
for send, receive, box in infos:
    cnt = C
    
    for i in range(send, receive):    
        if cnt > min(cap[i], box) :
            cnt = min(cap[i], box)
    for i in range(send, receive):
        cap[i] -= cnt
    ans += cnt

print(ans)
