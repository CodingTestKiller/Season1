import sys
sys.setrecursionlimit(10**4)
inp = sys.stdin.readline
n,k = map(int,inp().split())
bin = dict()
def binomial(n,k):
    if (n,k) in bin.keys():
        ans = bin[(n,k)]
    else:
        if k == 0 or k == n:
            ans = bin[(n,k)] = 1
        else:
            ans = bin[(n,k)] = binomial(n-1,k-1) + binomial(n-1,k)
            
    return ans
print(binomial(n,k)%10007)