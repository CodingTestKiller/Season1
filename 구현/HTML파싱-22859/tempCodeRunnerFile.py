# 제대로 풀지 못한 것 같습니다. 
# 제가 하려던 풀이로 참고하여 제출합니다.
import sys
input = sys.stdin.readline

html = input()
tmp = ''
i = 0

while i < len(html):
    if html[i] == '<':
        while html[i] != '>':
            if html[i] == '"':
                i += 1
                tmp = 'title : '
                while html[i] != '"':
                    tmp += html[i]
                    i += 1
                tmp = tmp.strip()
                print(tmp)
                tmp = ''
            i += 1
    if html[i] != '>':
        tmp += html[i]
    elif html[i-3:i+1] == '</p>':
        tmp = tmp.strip().split()
        print(' '. join(tmp))
        tmp = ''
    i += 1