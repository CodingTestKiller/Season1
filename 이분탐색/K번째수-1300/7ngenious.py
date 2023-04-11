import sys
input = sys.stdin.readline

N, K = map(int, input().split())

def find_num(N, K):
  left , right = 1 , K
  while left <= right:
      mid = (left + right) // 2
      cnt = sum(min(mid //i, N) for i in range(1, N+1))
      
      if cnt < K:
          left = mid + 1
      else:
          answer = mid
          right = mid - 1
  return answer

ans = find_num(N,K)
print(ans)