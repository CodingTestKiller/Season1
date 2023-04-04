import sys

N = int(sys.stdin.readline())
snowman=list(map(int,sys.stdin.readline().split()))
snowman.sort()
answer = float('inf')
for i in range(N-1):
    for j in range(N-1,i,-1):
        elza = snowman[i] + snowman[j]
        s, e = 0, N-1

        while s < e:
            if s == i or s == j:
                s += 1
                continue
            if e == i or e == j:
                e -= 1
                continue

            anna = snowman[s] + snowman[e]
            answer = min(answer, abs(elza - anna))

            if elza < anna:
                e-=1
            if elza > anna:
                s+=1
            if elza == anna:
                break
print(answer)
#1h 30m
