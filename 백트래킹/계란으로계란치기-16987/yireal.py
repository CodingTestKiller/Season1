import sys
inp = sys.stdin.readline
n = int(inp())
ans = 0
egg = []
for i in range(n):
    s,w = map(int,inp().split())
    egg.append([s,w])
def egg_crash(index):
    global ans
    if index == n:
        break_egg = 0
        for i in range(n):
            if egg[i][0] <= 0:
                break_egg += 1
        ans = max(ans,break_egg)
        return
    if egg[index][0] <= 0:
        egg_crash(index+1)
        return
    flag = True
    for i in range(n):
        if i  == index : continue
        if egg[i][0] > 0:
            flag = False
            break
    if flag:
        ans = max(ans,n-1)
        return
    for i in range(n):
        if i == index : continue
        if egg[i][0] <= 0 : continue
        egg[index][0] -= egg[i][1]
        egg[i][0] -= egg[index][1]
        egg_crash(index+1)
        egg[index][0] += egg[i][1]
        egg[i][0] += egg[index][1]
egg_crash(0)
print(ans)