from sys import stdin
from collections import deque
inp = stdin.readline
que = deque()
k = int(inp().rstrip())
buf = list(map(int,inp().rstrip().split()))
tree = [[] for _ in range(k)]
que.append((buf,0))
while que:
    (buf,i) = que.popleft()
    if(len(buf) == 1):
        tree[i].append(*buf)
        continue
    mid = int((len(buf)/2))
    tree[i].append(buf[mid])
    que.append((buf[:mid],i+1))
    que.append((buf[mid+1:],i+1))
for i in range(k):
    print(*tree[i])
    