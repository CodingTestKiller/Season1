import sys
inp = sys.stdin.readline
first = list(inp().rstrip())
second = list(inp().rstrip())
f_size = len(first)
s_size = len(second)
ans = [[0]*(s_size+1) for _ in range(f_size+1)]
for i in range(1,f_size+1):
    for j in range(1,s_size+1):
        if(first[i-1] == second[j-1]):
            ans[i][j] = ans[i-1][j-1] + 1
        else:
            ans[i][j] = max(ans[i-1][j],ans[i][j-1])
print(ans[f_size][s_size])