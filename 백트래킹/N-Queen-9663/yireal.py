
import sys
inp = sys.stdin.readline
n = int(inp())
chess = [0] * n
visit = [False] * n
ans = 0
def attack_range(n):
    for i in range(n):
        if(chess[n] == chess[i]) or (n-i == abs(chess[n] - chess[i])):
            return False
    return True
def nqueen(depth):
    global ans
    if depth == n:
        ans += 1
        returnㅊㅇ 
    for i in range(n):
        if visit[i] == False:
            chess[depth] = i
            if attack_range(depth):
                visit[i] = True
                nqueen(depth + 1)
                visit[i] = False
nqueen(0)
print(ans)