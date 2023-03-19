import sys
import itertools as it
inp = sys.stdin.readline
n,m = map(int,inp().split())
mix = [[False] * n for _ in range(n)]
for i in range(m):
    a,b = map(int,inp().split())
    mix[a-1][b-1] = True
    mix[b-1][a-1] = True
    ans = 0
for i in it.combinations(range(n),3):
    if mix[i[0]][i[1]] or mix[i[0]][i[2]] or mix[i[1]][i[2]]:
        continue
    ans += 1
print(ans)
    
