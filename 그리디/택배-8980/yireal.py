import sys
inp = sys.stdin.readline
n,c = map(int,inp().split())
m = int(inp())
box = [list(map(int,inp().split())) for _ in range(m)]
box.sort(key=lambda x:x[1])
cnt = 0
contain = [c]*(n+1)
for i in range(m):
    tmp = c
    for j in range(box[i][0],box[i][1]):
        tmp = min(tmp,contain[j])
    tmp = min(tmp,box[i][2])
    for j in range(box[i][0],box[i][1]):
        contain[j] -= tmp
    cnt += tmp
print(cnt)
