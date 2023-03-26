from collections import Counter
from sys import stdin
input = stdin.readline

n = int(input())

snow = [int(x) for x in input().split()]
snow.sort()


ans = []

for i in range(2):
    min = snow[1] - snow[0]
    p1 = 0
    p2 = 1
    index = [0, 1]

    while p2 < len(snow):

        if snow[p2] - snow[p1] < min:
            index[1] = p2
            index[0] = p1
            min = snow[p2] - snow[p1]

        p1 += 1
        p2 += 1

    ans.append([snow[index[0]], snow[index[1]]])
    del snow[index[1]]
    del snow[index[0]]

print(ans)
print(abs((ans[0][0] + ans[1][1]) - (ans[0][1] + ans[1][0])))
