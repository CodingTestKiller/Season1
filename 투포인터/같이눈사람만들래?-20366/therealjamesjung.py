from sys import stdin
from itertools import combinations

input = stdin.readline

n = int(input())

snowballs = sorted([int(x) for x in input().split()])

min_height = 10000000000

for i in range(n-3):
    for j in range(i+3, n):
        elsa = snowballs[j] + snowballs[i]
        k, l = i+1, j-1

        while k < l:
            anna = snowballs[k] + snowballs[l]
            min_height = min(min_height, abs(elsa - anna))

            if elsa > anna:
                k += 1
            elif elsa < anna:
                l -= 1
            else:
                print(0)
                exit()


print(min_height)
