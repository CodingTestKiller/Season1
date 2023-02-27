import sys

N,K=map(int,sys.stdin.readline().split())
fac=[1]*(N+1)
for i in range(2,N+1):
    fac[i]=fac[i-1]*i
print(int((fac[N]//(fac[K]*fac[N-K]))%10007))
#float 연산과 int 연산 주의하기. int/int: float 반환 나눗셈, int//int: int 반환 나눗셈
#20m