import sys
inp = sys.stdin.readline
n = int(inp())
snow = list(map(int,inp().split()))
snow.sort()
ans = sys.maxsize
for i in range(n-3):
    for j in range(i+3,n):
        key = snow[i] + snow[j]
        front,rear = i + 1,j - 1 
        while  front < rear :
            tmp = (snow[front] + snow[rear])
            if ans > abs(tmp - key):
                ans = abs(tmp - key)
            if tmp < key:
                front += 1
            elif tmp > key:
                rear -= 1
            else:
                print(0)
                exit(0)
print(ans)