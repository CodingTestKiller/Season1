import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

def check_out(n, m, arr):
  left, right = min(arr), max(arr) * m
  ans = right

  while left <= right:
      total = 0
      mid = (left + right) // 2
      for i in range(n):
          total += mid // arr[i]
      if total >= m:
          right = mid - 1
          ans = min(mid, ans)
      else:
          left = mid + 1
  return ans
  
result = check_out(n, m, arr)
l, r = 0, max(arr) * m
print(result)

# while left < right:
#     mid = (left + right) // 2
#     total = sum(mid // x for x in arr)

#     if total < m:
#         left = mid + 1
#     else:
#         right = mid
# return l
#솔루션 참고 아래처럼 줄여서 풀 수도 있다.
