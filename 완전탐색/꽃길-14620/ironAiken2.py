from sys import stdin
input = stdin.readline

n = int(input())
ground = [[int(x) for x in input().split(' ')] for _ in range(n)]
cost = [[0 for _ in range(n)] for _ in range(n)]

move = [[1, 0], [-1, 0], [0, 1], [0, -1]]

for i in range(1,n-1):
    for j in range(1,n-1):
        c = ground[i][j]
        for m in move:
            nx = i + m[0]
            ny = j + m[1]
            c += ground[nx][ny]
        cost[i][j] = c

min_cost = 3001

for i in range(1,n-1):
    for j in range(1,n-1):
        visit = [[0 for _ in range(n)] for _ in range(n)]
        # 첫번째 땅 고정
        cost1 = cost[i][j]
        visit[i][j] = 1
        
        for m in move:
            nx = i + m[0]
            ny = j + m[1]
            visit[nx][ny] = 1
        
        for ii in range(1, n-1):
            for jj in range(1, n-1):
                visit2 = [row[:] for row in visit]
                # 두번째 땅 고정
                if visit2[ii][jj] == 1:
                    continue
                flag = 0
                for m in move:
                    if visit2[ii+m[0]][jj+m[1]] == 1:
                        flag = 1
                        break
                if flag == 1:
                    continue
                cost2 = cost[ii][jj]
                visit2[ii][jj] = 1
                for m in move:
                    nx = ii + m[0]
                    ny = jj + m[1]
                    visit2[nx][ny] = 1
                
                for iii in range(1, n-1):
                    for jjj in range(1, n-1):
                        # 세번째 땅 탐색
                        if visit2[iii][jjj] == 1:
                            continue
                        flag = 0
                        for m in move:
                            if visit2[iii+m[0]][jjj+m[1]] == 1:
                                flag = 1
                                break
                        if flag == 1:
                            continue

                        if cost1 + cost2 + cost[iii][jjj] < min_cost:
                            min_cost = cost1 + cost2 + cost[iii][jjj]

print(min_cost)
                        