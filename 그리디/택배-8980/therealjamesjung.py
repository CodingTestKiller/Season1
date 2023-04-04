from sys import stdin

input = stdin.readline

n, c = [int(x) for x in input().split()]
m = int(input())
request = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    sender, receiver, amount = [int(x) for x in input().split()]
    request[sender][receiver] += amount

truck = [0] * (n+1)
result = 0

for truck_position in range(1, n+1):
    result += truck[truck_position]
    truck[truck_position] = 0
    remainder = c
    for i in range(1, n+1):
        if remainder <= 0:
            truck[i] = 0
        else:
            if remainder > truck[i] + request[truck_position][i]:
                truck[i] += request[truck_position][i]
            else:
                truck[i] = remainder
            remainder -= truck[i]

print(result)
