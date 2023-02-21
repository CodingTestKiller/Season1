from sys import stdin
from itertools import permutations
from collections import Counter

input = stdin.readline

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cases = {key: True for key in [
    ''.join(str(y) for y in x) for x in permutations(num, 3)]}

# 3Cs x (3-s)Cb x 10**(3-s-b)

n = int(input())

for _ in range(n):
    guess, strike, ball = [x.strip() for x in input().split()]

    for case in cases.keys():
        strike_cnt = 0
        ball_cnt = 0

        for i in range(3):
            for j in range(3):
                if guess[i] == case[j]:
                    if i == j:
                        strike_cnt += 1
                    else:
                        ball_cnt += 1

        if strike_cnt != int(strike) or ball_cnt != int(ball):
            cases[case] = False

print(Counter(cases.values())[True])
