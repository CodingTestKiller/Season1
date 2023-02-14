import sys
def quack_check(word,check,start):
    key = ['q','u','a','c','k']
    tmp = [0,0,0,0,0]
    cnt = 0
    flag = 0
    for i in range (start,len(word)):
        if(check[i]):
            continue
        if(key[cnt] == word[i]):
            tmp[cnt] = i
            cnt += 1
        if(cnt == 5):
            for j in range (len(tmp)):
                check[tmp[j]] = 1
            cnt = 0
            flag = 1
    if(flag == 1):
        return 1
    else:
        return 0
            
inp = sys.stdin.readline
word = inp().rstrip()
check = [0]*len(word)
total = 0
for i in range (len(word)):
    if(word[i] == 'q' and check[i] == 0):
        total += quack_check(word,check,i)
if(total == 0 or len(check) != sum(check)):
    print(-1)
else:
    print(total)