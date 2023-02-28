import sys

my_input = sys.stdin.readline

t = int(my_input())
for _ in range(t):
    n = int(my_input())
    coins = [int(x) for x in my_input().split()]
    target = int(my_input())
    cases = [[0 for _ in range(target + 1)] for _ in range(n)]
    for i in range(n):
        for j in range(coins[0], target + 1):
            if i == 0:
                if j % coins[i] == 0:
                    cases[i][j] += 1
            else:
                if j < coins[i]:
                    cases[i][j] = cases[i - 1][j]
                else:
                    tmp = j
                    cnt = 0
                    if tmp % coins[i] == 0:
                        cnt += 1
                    while tmp > 0:
                        cnt += cases[i - 1][tmp]
                        tmp -= coins[i]
                    cases[i][j] = cnt
    print(cases[n - 1][target])
