import sys

N=int(sys.stdin.readline())
eggs=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

def dfs(hand):
    cnt = 0
    if hand == N:
        broken=0
        for i in range(N):
            if eggs[i][0]<=0:
                broken+=1
        cnt = max(cnt,broken)
        return cnt

    if eggs[hand][0]<=0:
        cnt = max(cnt,dfs(hand+1))
        return cnt

    flag = False
    for i in range(N):
        if hand != i and eggs[i][0]>=0:
            flag = True
            eggs[hand][0] -= eggs[i][1]
            eggs[i][0] -= eggs[hand][1]
            cnt = max(cnt,dfs(hand+1))
            eggs[hand][0] += eggs[i][1]
            eggs[i][0] += eggs[hand][1]
    if flag == False:
        cnt = max(cnt,dfs(N))
    return cnt

print(dfs(0))

#1h 30m