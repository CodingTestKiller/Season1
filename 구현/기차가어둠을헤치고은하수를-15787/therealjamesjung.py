from sys import stdin

input = stdin.readline

n, m = [int(x) for x in input().split()]
trains = [0 for _ in range(n)]

for _ in range(m):
    cmd = [int(x) for x in input().split()]
    if cmd[0] == 1:
        seat = 2 ** (20 - cmd[2])
        trains[cmd[1]-1] += seat if trains[cmd[1]-1] & seat != seat else 0
    elif cmd[0] == 2:
        seat = 2 ** (20 - cmd[2])
        trains[cmd[1]-1] -= seat if trains[cmd[1]-1] & seat == seat else 0
    elif cmd[0] == 3:
        trains[cmd[1]-1] = trains[cmd[1]-1] >> 1
    elif cmd[0] == 4:
        trains[cmd[1]-1] = trains[cmd[1]-1] << 1
        trains[cmd[1]-1] = trains[cmd[1]-1] & (2 ** 20) - 1
    else:
        break

print(len(set(trains)))
