import sys
def count_reverse(N,check_list,range_list):
    tmp = sum(check_list[range_list[0]:range_list[1]+1])
    return range_list[1]-range_list[0]-tmp+1
N,K,Q,M = map(int,sys.stdin.readline().rstrip().split())
sleep_list = [ 0 for _ in range(N+3)]
check_list = [ 0 for _ in range(N+3)]
for i in map(int, sys.stdin.readline().split()):
    sleep_list[i] = 1
for i in map(int,sys.stdin.readline().split()):
    if(sleep_list[i]):
        continue 
    for j in range(i,N+3,i):
        if(sleep_list[j] == 0):
            check_list[j] = 1
for i in range (M):
    range_list = list(map(int,sys.stdin.readline().rstrip().split()))
    print(count_reverse(N,check_list,range_list))