import sys
from collections import defaultdict
inp = sys.stdin.readline
N,d,k,c = map(int,inp().split())
sushi = []
front = 0
rear = k-1
cnt = 0
max_cnt = 0
check = defaultdict(int)
check[c] += 1
for i in range(N):
    sushi.append(int(inp()))
for i in range(rear+1):
    check[sushi[i]] += 1
while front < N:
    max_cnt = max(len(check),max_cnt)
    check[sushi[front]] -= 1
    if(check[sushi[front]] == 0):
        del check[sushi[front]]
    front += 1
    rear += 1
    check[sushi[rear%N]] += 1
print(max_cnt)