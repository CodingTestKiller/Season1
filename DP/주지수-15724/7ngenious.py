# import sys
# input = sys.stdin.readline

# N,M = map(int, input().split())

# arr = [list(map(int, input().split())) for _ in range(N)]

# K = int(input())

# for _ in range(K):#여기서 O(K)
#     sum = 0
#     x1,y1,x2,y2 = map(int, input().split())

#     for i in range(x1-1,x2):#최악의 경우 O(N)
#       for j in range(y1-1,y2):#최악의 경우 O(M)
#         sum += arr[i][j]
#     print(sum)
# # 현재 방식은 원소를 하나하나 구해서 더하여 출력하는 방식으로  O(K*M*N)의 시간복잡도
# # 따라서 시간초과 발생

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
sum = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
      sum[i][j] = arr[i-1][j-1] + sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1]

K = int(input()) 

for _ in range(K):
    x1,y1,x2,y2 = map(int, input().split())
    ans = sum[x2][y2] - sum[x1-1][y2] - sum[x2][y1-1] + sum[x1-1][y1-1]
    print(ans)
