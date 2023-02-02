from sys import stdin
import copy
input = stdin.readline

r, c, n = [int(x) for x in input().split(' ')]

List = [[char for char in input().rstrip()] for _ in range(r)]
bombfull_List = [['O' for _ in range(c)] for _ in range(r)]
List2 = copy.deepcopy(bombfull_List)
cnt = 0

if n == 0:
    for i in range(len(List)):
        print(''.join(s for s in List[i]))
    exit()

cnt += 1

if cnt == n:
    for i in range(len(List)):
        print(''.join(s for s in List[i]))
    exit()

while True:
    cnt += 1

    if cnt == n:
        for i in range(len(bombfull_List)):
            print(''.join(s for s in bombfull_List[i]))
        break

    for i in range(len(List)):
        for j in range(len(List[i])):
            if List[i][j] == 'O':
                List2[i][j] = '.'
                if i > 0:
                    List2[i - 1][j] = '.'
                if i < r - 1:
                    List2[i + 1][j] = '.'
                if j > 0:
                    List2[i][j - 1] = '.'
                if j < c - 1:
                    List2[i][j + 1] = '.'

    List = copy.deepcopy(List2)
    List2 = copy.deepcopy(bombfull_List)

    cnt += 1

    if cnt == n:
        for i in range(len(List)):
            print(''.join(s for s in List[i]))
        break
