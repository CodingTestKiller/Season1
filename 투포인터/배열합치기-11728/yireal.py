import sys
from collections import deque
inp = sys.stdin.readline
n,m = map(int,inp().split())
a = deque(list(map(int,inp().split())))
b = deque(list(map(int,inp().split())))
ans = deque()
while a and b:
    if a[0] < b[0]:
        ans.append(a.popleft())
    else:
        ans.append(b.popleft())

if a:
    ans.extend(a)
else:
    ans.extend(b)
print(*ans)