import sys

N,M=map(int,sys.stdin.readline().split())
graph=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
visited=[[0]*M for _ in range(N)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
maxVal=max(map(max,graph))
answer=0
#'ㅗ' 모양을 제외한 다른 모양들은 4개 짜리 걍 한줄 늘어뜨린 것과 같음
def DFS(x, y, index, total):
    global answer
    if answer>=total+maxVal*(3-index):
        return
    # 남은 게 최대라도 answer 이하면 컷
    if index==3:
        answer=max(answer,total)
        return
    # total:지금 dfs값
    # 블록 처리
    else:
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<N and ny>=0 and ny<M and visited[nx][ny]==0:
                #'ㅗ' 모양
                if index==1:
                    visited[nx][ny]=1
                    DFS(x,y,index+1,total+graph[nx][ny])
                    visited[nx][ny]=0
                visited[nx][ny]=1
                DFS(nx,ny,index+1,total+graph[nx][ny])
                visited[nx][ny]=0

for x in range(N):
    for y in range(M):
        visited[x][y]=1
        DFS(x,y,0,graph[x][y])
        visited[x][y]=0
print(answer)