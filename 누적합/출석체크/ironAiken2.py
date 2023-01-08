from sys import stdin

N, K, Q, M = [int(x) for x in stdin.readline().strip().split(' ')]
sleep = [int(x) for x in stdin.readline().strip().split(' ')]
std_num = [int(x) for x in stdin.readline().strip().split(' ')]
arr = list(range(3, N+3))

for num in std_num:
    if(num not in sleep):
        arr = [i for i in arr if i%num != 0]
    for i in sleep:
        if(i not in arr):
            arr.append(i)

for i in range(M):
    S, E = [int(x) for x in stdin.readline().strip().split(' ')]
    new_arr = [a for a in arr if a >= S and a <= E]

    print(len(new_arr))