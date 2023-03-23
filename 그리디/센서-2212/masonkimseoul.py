import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
sensors = list(map(int,sys.stdin.readline().split()))
sensors.sort()
distances = [sensors[i+1]-sensors[i] for i in range(N-1)]
distances.sort(reverse=True)
print(sum(distances[K-1:]))
#1h
