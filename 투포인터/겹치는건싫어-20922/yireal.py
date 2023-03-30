import sys
from collections import defaultdict
inp = sys.stdin.readline
n,k = map(int,inp().split())
seq = list(map(int,inp().split()))
off_set = defaultdict(int)
front = 0
rear = 0
cnt = 0
ans = 0
while rear < n:
    if off_set[seq[rear]] < k:
        off_set[seq[rear]] += 1
        rear += 1
    else:
        off_set[seq[front]] -= 1
        front += 1
    ans = max(ans,rear-front)         
print(ans)

