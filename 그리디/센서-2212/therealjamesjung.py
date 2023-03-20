from sys import stdin

input = stdin.readline

int(input())
k = int(input())

positions = sorted([int(x) for x in input().split()])
distance = sorted([positions[i+1] - positions[i]
                  for i in range(len(positions)-1)])
# print(distance)
distance = distance[:1-k] if k > 1 else distance
print(sum(distance))
