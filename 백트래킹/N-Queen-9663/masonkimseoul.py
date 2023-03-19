import sys

N=int(sys.stdin.readline())
board=[-1]*N

def is_safe(x):
    for i in range(x):
        if board[x] == board[i] or abs(board[x]-board[i]) == x-i:
            return False
        #1. 1차원 배열을 사용하므로 같은 row에 존재하는 queen을 배제, 즉 i번째 원소는 i번째 row 위에 있는 것
        #2. index로 row를 표시하였으니 배열의 원소로 column을 표시한다. 값이 같으면 같은 column 위에 있는 것
        #3. 대각선상의 판단은 기울기가 -1, 1인 경우로 판단
    return True

def DFS(x):
    cnt = 0
    if x==N:
        cnt += 1
    else:
        for i in range(N):
            board[x] = i
            if is_safe(x):
                cnt += DFS(x+1)
    return cnt
print(DFS(0))

#2h