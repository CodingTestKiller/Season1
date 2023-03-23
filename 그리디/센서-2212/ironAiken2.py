from sys import stdin
input = stdin.readline

n = int(input())
k = int(input())
tower = [int(x) for x in input().split()]

if k >= n:
    print(0)
    exit()

tower.sort()
dist = []

for i in range(n-1):
    if tower[i+1] - tower[i] == 0:
        continue
    dist.append(tower[i+1] - tower[i])

for i in range(k-1):
    dist.remove(max(dist))

print(sum(dist))
