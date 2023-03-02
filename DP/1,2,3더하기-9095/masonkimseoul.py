import sys

T=int(sys.stdin.readline())
for _ in range(T):
    N=int(sys.stdin.readline())
    numbers=[0]*12
    numbers[1]=1
    numbers[2]=2
    numbers[3]=4
    for i in range(4,N+1):
        numbers[i]=numbers[i-1]+numbers[i-2]+numbers[i-3]
    print(numbers[N])
#10m
