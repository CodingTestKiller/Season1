import sys

T=int(sys.stdin.readline())
for _ in range(T):
    N=int(sys.stdin.readline())
    coins=list(map(int,sys.stdin.readline().split()))
    cost=int(sys.stdin.readline())
    methods=[0]*(cost+1)
    methods[0]=1
    #각 동전의 액면가에 경우의 수를 미리 1로 설정하면 중복 발생
    for i in range(N):
        for j in range(1,cost+1):
            if j-coins[i]>=0:
                methods[j]+=methods[j-coins[i]]
                #작은 동전으로 만드는 경우의 수에 큰 동전으로 만드는 경우의 수 첨가
    print(methods[cost])


'''
1,2
1원 -> 1
2원 -> 2 (11,2)
3원 -> 2 (111, 12)
4원 -> 3 (1111, 22, 112)
5원 -> 3 (11111, 1112, 122)
6원 -> 4 (111111, 11112, 1122, 222)
7원 -> 4 (1111111, 111112, 11122, 1222)
8원 -> 5 (11111111, 1111112, 111122, 11222, 2222)

1,5,10
1원 -> 1
2원 -> 1
3원 -> 1
4원 -> 1
5원 -> 2
6원 -> 2
7원 -> 2
8원 -> 2
9원 -> 2
10원 -> 3 (1111111111, 55, 10)

5, 7
1원 -> 1
2원 -> 1
3원 -> 1
4원 -> 1
5원 -> 1
6원 -> 1
7원 -> 1



'''
