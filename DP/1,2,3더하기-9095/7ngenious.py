import sys
input = sys.stdin.readline

n = int(input())

for i in range(n) :
    x = int(input())
    num = [0] * (x+3)
    num[1] = 1
    num[2] = 2
    num[3] = 4
    if x > 3 : 
      for j in range(4,x+1) :
        num[j] = num[j-3] + num[j-2] + num[j-1]
    print(num[x])
