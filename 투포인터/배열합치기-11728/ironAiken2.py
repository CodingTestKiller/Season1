from sys import stdin
input = stdin.readline

n, m = [int(x) for x in input().split()]

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

a_index = 0
b_index = 0

a_len = len(a)
b_len = len(b)

ans = []

while a_index < a_len and b_index < b_len:
    if a[a_index] < b[b_index]:
        ans.append(a[a_index])
        a_index += 1
    else:
        ans.append(b[b_index])
        b_index += 1

if a_index != a_len:
    ans += a[a_index:]
if b_index != b_len:
    ans += b[b_index:]

print(*ans)
