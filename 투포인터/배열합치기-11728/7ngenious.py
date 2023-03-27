import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
sum = []
sum = A + B

sum.sort()
print (*sum)