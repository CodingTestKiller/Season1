from sys import stdin
from collections import deque

input = stdin.readline

n, d, k, c = [int(x) for x in input().split()]

belt = deque([int(input()) for _ in range(n)])
eats = {}
eats_belt = deque()
current_cnt = 0
max_cnt = 0

for i in range(k):
    sushi = belt.popleft()
    eats_belt.append(sushi)
    try:
        eats[sushi] += 1
    except KeyError:
        eats[sushi] = 1
        current_cnt += 1

for _ in range(n):
    last_sushi = eats_belt.popleft()
    belt.append(last_sushi)
    eats[last_sushi] -= 1

    if eats[last_sushi] == 0:
        current_cnt -= 1

    next_sushi = belt.popleft()
    eats_belt.append(next_sushi)

    try:
        if eats[next_sushi] == 0:
            current_cnt += 1
        eats[next_sushi] += 1
    except KeyError:
        eats[next_sushi] = 1
        current_cnt += 1

    if current_cnt >= max_cnt:
        max_cnt = current_cnt
        try:
            if eats[c] == 0:
                max_cnt += 1
        except KeyError:
            max_cnt += 1

print(max_cnt)
