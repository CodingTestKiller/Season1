from sys import stdin

input = stdin.readline

[int(x) for x in input().split()]

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

result = []

a_index = 0
b_index = 0

while a_index < len(a) and b_index < len(b):
    if a[a_index] < b[b_index]:
        result.append(a[a_index])
        a_index += 1
    else:
        result.append(b[b_index])
        b_index += 1

result += a[a_index:]
result += b[b_index:]

for _ in result:
    print(_, end=' ')
