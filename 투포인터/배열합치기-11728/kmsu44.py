from collections import deque
a_size, b_size = map(int, input().split())
a = deque(list(map(int, input().split())))
b = deque(list(map(int, input().split())))

result = []

while a and b:
    if a[0] < b[0]:
        result.append(a.popleft())
    elif a[0] == b[0]:
        result.append(a.popleft())
        result.append(b.popleft())
    else:
        result.append(b.popleft())
if a:
    result += a
if b:
    result += b
print(*result)
