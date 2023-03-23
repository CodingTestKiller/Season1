from sys import stdin
input = stdin.readline

n, m = [int(x) for x in input().split()]

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

a += b
a.sort()

print(*a)
