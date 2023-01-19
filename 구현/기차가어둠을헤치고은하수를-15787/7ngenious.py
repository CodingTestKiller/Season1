import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trains = [[0] * 20 for _ in range(N)]
temp = []

for _ in range(M):
    operand = list(map(int, input().split()))
    if operand[0] == 1:
        trains[operand[1]-1][operand[2]-1] = 1
    elif operand[0] == 2:
        trains[operand[1]-1][operand[2]-1] = 0
    elif operand[0] == 3:
        del trains[operand[1]-1][-1]
        a = [0]
        a.extend(trains[operand[1]-1])
        trains[operand[1]-1] = a
    elif operand[0] == 4:
        del trains[operand[1]-1][0]
        trains[operand[1]-1].extend([0])

for t in trains:
    if not temp:
        temp.append(t)
    else:
        if t not in temp: temp.append(t)

print(len(temp))