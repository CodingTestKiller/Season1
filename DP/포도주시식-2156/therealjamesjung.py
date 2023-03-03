from sys import stdin

input = stdin.readline

n = int(input())

wines = [int(input()) for _ in range(n)]

if n < 3:
    print(sum(wines))
    exit()

cache = [0] * n
cache[0] = wines[0]
cache[1] = wines[0] + wines[1]
cache[2] = sum(wines[:3]) - min(wines[:3])

# print(wines)
# print(cache)

for i in range(3, n):
    cache[i] = max(cache[i-3] + wines[i] + wines[i-1],
                   cache[i-2] + wines[i], cache[i-1])

print(cache[-1])


# 6, 10, 13, 9, 8, 1
# 6, 16, 23, 28, 33, 33

# 6, 10, 50, 70, 100
# 6, 16, 60, 126, 186


# -2까지의 합 + -1 값이 -1까지 합이면 -1까지 합이랑 -2까지의 합 + 현재값 비교해서 큰거
# 아니면


#  6 10 9 8 = 33
#  6 13 9 1 = 29
#  6 10 9 1 = 26
# 10 13 8 1 = 32
#  6 10 8 1 = 25
#  6 13 8 1 = 28
