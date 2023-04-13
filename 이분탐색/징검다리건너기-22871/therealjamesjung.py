# 미완성

from sys import stdin

input = stdin.readline


def jump_stone(pos1: int, pos2: int, stones: list):
    # print('jump', pos1, pos2, (pos2 - pos1) * (1 + abs(stones[pos1] - stones[pos2])))
    return (pos2 - pos1) * (1 + abs(stones[pos1] - stones[pos2]))


n = int(input())
stones = [int(x) for x in input().split()]
dp = [0, jump_stone(0, 1, stones)] + [0] * (n-2)


for i in range(2, n):
    dp[i] = jump_stone(0, i, stones)
    for j in range(i):
        print(j, i, jump_stone(j, i, stones))
        dp[i] = min(jump_stone(j, i, stones), dp[j])
    # print(dp)

print(stones)
print(dp)
print(dp[-1])
