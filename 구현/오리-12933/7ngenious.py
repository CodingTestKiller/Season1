import sys
input = sys.stdin.readline

sound = input()
if sound[0] !='q' : 
    print(-1)
    exit(0)
duck=['q']
for i in sound[1:] :
    flag = True
    if i == 'q':
        for j in range(len(duck)):
            if duck[j] == 'k':
                duck[j] = 'q'
                flag = False
                break 
        if flag:
            duck.append('q')
    elif i == 'u':
        for j in range(len(duck)):
            if duck[j] == 'q':
                duck[j] = 'u'
                flag = False
                break 
        if flag:
            print(-1)
            exit(0)
    elif i =='a':
        for j in range(len(duck)):
            if duck[j] == 'u':
                duck[j] = 'a'
                flag = False
                break 
        if flag:
            print(-1)
            exit(0)
    elif i =='c':
        for j in range(len(duck)):
            if duck[j] == 'a':
                duck[j] = 'c'
                flag = False
                break 
        if flag:
            print(-1)
            exit(0)
    elif i == 'k':
        for j in range(len(duck)):
            if duck[j] == 'c':
                duck[j] = 'k'
                flag = False
                break 
        if flag:
            print(-1)
            exit(0)

for i in duck :
    if i != 'k':
        print(-1)
        exit(0)

print(len(duck))