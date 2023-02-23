import sys
import itertools
inp = sys.stdin.readline
dead = []
unknown = []
ans = [0,0,0]
total = [i for i in range(1,10)]
possible = list(itertools.permutations(total,3))
n = int(inp().rstrip())
for i in range(n):
    buf,st,bl = map(int,inp().rstrip().split())
    buf = list(str(buf))
    cnt = 0
    for i in range(len(possible)):
        st_cnt = 0
        bl_cnt = 0
        i -= cnt
        for j in range(3):
            buf[j] = int(buf[j])
            if buf[j] in possible[i]:
                if j == possible[i].index(buf[j]):
                    st_cnt += 1
                else:
                    bl_cnt += 1
        if st_cnt != st or bl_cnt != bl:
            possible.remove(possible[i])
            cnt += 1
print(len(possible))