import sys

input = sys.stdin.readline

n = int(input())

guess_list = [[0, 0, 0] for _ in range(n)]
ans = 0

for i in range(n):
    num, strike, ball = [int(x) for x in input().rstrip().split()]
    guess_list[i][0] = num
    guess_list[i][1] = strike
    guess_list[i][2] = ball

for i in range(1, 10):
    for j in range(1, 10):
        if i == j:
            continue
        for k in range(1, 10):
            if j == k or i == k:
                continue
            flag = 1
            for guess in guess_list:
                strike_cnt = 0
                ball_cnt = 0
                hund = guess[0] // 100
                ten = guess[0] % 100 // 10
                one = guess[0] % 10
                if i == hund:
                    strike_cnt += 1
                elif i == ten or i == one:
                    ball_cnt += 1
                if j == ten:
                    strike_cnt += 1
                elif j == hund or j == one:
                    ball_cnt += 1
                if k == one:
                    strike_cnt += 1
                elif k == hund or k == ten:
                    ball_cnt += 1
                if strike_cnt != guess[1] or ball_cnt != guess[2]:
                    flag = 0
                    break
            if flag == 1:
                ans += 1
print(ans)
