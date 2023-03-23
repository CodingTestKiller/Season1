import sys
inp = sys.stdin.readline
n = int(inp())
if n == 3 or n == 1 :
    print(-1)
    exit()
big_coin = n//5
left = n%5
if left % 2 != 0:
    big_coin -= 1
    left += 5
small_coin = left//2
print(big_coin + small_coin)