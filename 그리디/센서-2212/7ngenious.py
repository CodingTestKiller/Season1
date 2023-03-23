import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
sensor = list(map(int, input().split()))
sensor.sort()

if K >= N:
    print(0)
else:

  dis = []# 센서사이거리 리스트

  for i in range(1, N):
      dis.append(sensor[i] - sensor[i - 1])

  dis.sort(reverse=True)
  print(sum(dis[K - 1:]))
  
# for _ in range(K-1):
#     dist.pop(0)
# print(sum(dist))