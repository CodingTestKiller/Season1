n = int(input())
L = [list(map(int, input().split())) for _ in range(n)]
global res
res = 0


def DFS(pick):
    global res
    if pick == n:
        cnt = 0
        for i in range(n):
            if L[i][0] <= 0:
                cnt += 1
        res = max(res, cnt)
        return
    if L[pick][0] <= 0:
        DFS(pick+1)
        return
    flag = 0
    for i in range(n):
        if i == pick:
            continue
        if L[i][0] > 0:
            flag = 1
            L[pick][0] -= L[i][1]
            L[i][0] -= L[pick][1]
            DFS(pick+1)
            L[pick][0] += L[i][1]
            L[i][0] += L[pick][1]

    # 이부분 솔루션 참고
    if flag == 0:
        DFS(n)
    ####


DFS(0)

print(res)
