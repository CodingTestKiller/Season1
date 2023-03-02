import sys
inp = sys.stdin.readline  
ans_list =[1,2,4]
t = int(inp())
for _ in range(t):
    num = int(inp())
    size = len(ans_list)
    if(num > size):
        for i in range(size-1,num):
            ans_list.append(sum(ans_list[i-2:i+1]))
    print(ans_list[num-1])
