import math
import sys

N=int(sys.stdin.readline())
q=int(math.sqrt(N))
if q**2<N:
    print(q+1)
else:
    print(q)

#5m
