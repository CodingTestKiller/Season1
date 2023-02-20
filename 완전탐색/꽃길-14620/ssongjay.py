import sys

input_ = sys.stdin.readline

N = int(input_())
ground = [[int(x) for x in input_().rstrip().split()] for _ in range(N)]
visited = [([False] * N + 1)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

min_total = 20001

for i in range(3):
    for 