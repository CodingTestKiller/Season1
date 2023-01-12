import sys
inp = sys.stdin.readline

def check_root(sum_list,i,N,key,avg):
    total = 0
    if(i == N):
        return 1
    for j in range(i,N+1):
        if(sum_list[j] == key):
            total += check_root(sum_list,j,N,key+avg,avg)
    return total
    
    
N = int(inp().rstrip())
sum_list = [0]*(N+1)
check_list = [0]*(N+1)
num_list = list(map(int,inp().rstrip().split()))
for i in range(1,N+1):
    sum_list[i] = sum_list[i-1]+num_list[i-1]
avg_val = int(sum_list[N]/4)
print(check_root(sum_list,0,N,avg_val,avg_val))

