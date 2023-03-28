from sys import stdin

input = stdin.readline

result = {}

n, k = [int(x) for x in input().split()]

li = [int(x) for x in input().split()]

start = 0
max_len = 1

for end, l in enumerate(li):
    try:
        result[l] += 1
    except KeyError:
        result[l] = 1

    if result[l] > k:
        max_len = max(end-start, max_len)
        while result[l] > k:
            result[li[start]] -= 1
            start += 1

max_len = max(end-start+1, max_len)
print(max_len)
