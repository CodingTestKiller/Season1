import sys            
inp = sys.stdin.readline
def push(train):
    if(train[-1] == 1):
        train[-1] = 0
    for j in range(len(train)-1,0,-1):
        train[j] = train[j-1]
    train[0] = 0
def pull(train):
    if(train[0] == 1):
        train[0] = 0
    for j in range(len(train)-1):
        train[j] = train[j+1]
    train[-1] = 0
def list_to_bin(train):
    total = 0
    for i in range(len(train)):
        if(train[i]):
            total+=2**i
    return total
N,M = map(int,inp().rstrip().split())
bit_mask = list()
train = [[0] * 20 for i in range(N)]
for _ in range (M):
    arg = list(map(int,inp().rstrip().split()))
    if(arg[0] == 1):
        train[arg[1]-1][arg[2]-1] = 1
    elif(arg[0] == 2):
        train[arg[1]-1][arg[2]-1] = 0
    elif(arg[0] == 3):
        push(train[arg[1]-1])
    elif(arg[0] == 4):
        pull(train[arg[1]-1])
ans = 0
for i in range (N):
    bit = list_to_bin(train[i])
    if bit in bit_mask:
        continue
    else:
        bit_mask.append(bit)
        ans += 1
print(ans)

    

