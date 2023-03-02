import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1

N, K = map(int, input().split())
ans = factorial(N) // (factorial(N-K) * factorial(K))
print(ans % 10007)