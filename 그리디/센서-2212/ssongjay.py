import sys

input_ = sys.stdin.readline

N = int(input_())
K = int(input_())
sensors = [int(x) for x in input_().split()]
sensors.sort()

gaps = []
for i in range(1, N):
    gaps.append(sensors[i] - sensors[i-1])

gaps.sort(reverse=True)
print(sum(gaps[K - 1:]))
