# 솔루션에 있는 로직을 참고하였습니다.
import sys
input = sys.stdin.readline

N = int(input())

snow = sorted(list(map(int, input().split())))

ans = 4000000001
for i in range(N):
    for j in range(i+3, N):

        left, right = i+1, j-1

        while left <= right:
            sum = (snow[i] + snow[j]) - (snow[left] + snow[right])
            ans = min(ans, abs(sum))
            if sum < 0:
                right -= 1
            else:
                left += 1
print(ans)
