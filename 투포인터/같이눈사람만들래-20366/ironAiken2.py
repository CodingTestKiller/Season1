from sys import stdin
input = stdin.readline

n = int(input())

snow = [int(x) for x in input().split()]
snow.sort()

ans = 10000000000

for i in range(n-3):
    for j in range(i+3, n):
        snow1 = snow[i] + snow[j]

        p1, p2 = i+1, j-1

        while p1 < p2:
            snow2 = snow[p1] + snow[p2]

            ans = min(abs(snow1 - snow2), ans)

            if snow1 > snow2:
                p1 += 1
            elif snow1 < snow2:
                p2 -= 1
            else:
                print(0)
                exit()

print(ans)
