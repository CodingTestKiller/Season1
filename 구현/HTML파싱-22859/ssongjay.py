import sys

string = str(sys.stdin.readline().rstrip())
divs = string.split('<div title="')
for i in range(1, len(divs)):
    div = divs[i]
    p_list = div.split('<p>')
    title = p_list.pop(0)
    title = title[:-2]
    print('title :', title)
    for p in p_list:
        sentence = ''
        j = 0
        while j < len(p):
            if p[j] == '<':
                for k in range(j+1, len(p)):
                    if p[k] == '>':
                        j = k
                        break
            else:
                sentence += p[j]
            j += 1
        result = sentence.split()
        result = ' '.join(result)
        print(result)
