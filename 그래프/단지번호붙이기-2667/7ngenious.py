from collections import deque 
import sys 
input = sys.stdin.readline
n = int(input())

elements = [
    input().rstrip()
    for _ in range(n)
]

# 상하좌우
dxs = [1, -1, 0, 0]
dys = [0, 0, -1, 1]

# queue 
q = deque()


board = [
    []
    for _ in range(n)
]

# make board with int variable 
for idx,element in enumerate(elements) :
    for elem in element :
        board[idx].append(int(elem))

visited = [
    [False] * n 
    for _ in range(n)
]

home = [
    [0] * n
    for _ in range(n)
]

def in_range(x, y) :
    return x>=0 and x<n and y>=0 and y<n 

def can_go(x, y) :
    if not in_range(x, y) :
        return False 
    if visited[x][y] :
        return False 
    if board[x][y] == 0 :
        return False 
    return True 

def bfs() :
    global cnt 

    while q :
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys) :
            nx, ny = x+dx, y+dy 

            if can_go(nx, ny) :
                visited[nx][ny] = True 
                q.append((nx, ny))
                home[nx][ny] = cnt 

# 집들이 있는 위치만 추출
home_pos = []

for i in range(n) :
    for j in range(n) :
        if board[i][j] == 1 :
            home_pos.append((i, j))

# 방문되지 않은 집일 때 bfs()실행
# bfs()를 통해 인접한 집들을 모두 방문처리 
# bfs가 끝난 후 cnt += 1

cnt = 0
for x, y in home_pos :
    if not visited[x][y] :
        cnt += 1
        visited[x][y] = True 
        q.append((x, y))
        home[x][y] = cnt 
        bfs()

print(cnt)

cnt_lst = []
for k in range(1, cnt+1) :
    each_cnt = 0
    for i in range(n) :
        for j in range(n) :
            if home[i][j] == k :
                each_cnt += 1
    cnt_lst.append(each_cnt)

# 오름차순
cnt_lst.sort()

for elem in cnt_lst :
    print(elem)