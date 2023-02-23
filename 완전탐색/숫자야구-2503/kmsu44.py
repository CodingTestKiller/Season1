import itertools
n = int(input())
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
think_list = list(itertools.permutations(num_list, 3))
for _ in range(n):
    answer, strike, ball = input().split()
    tmp = []
    for think in think_list:
        strike_sum = 0
        ball_sum = 0
        for i in range(3):
            if int(answer[i]) == think[i]:
                strike_sum += 1
            elif int(answer[i]) in think:
                ball_sum += 1
        if strike_sum == int(strike) and ball_sum == int(ball):
            tmp.append(think)
    think_list = tmp
print(len(think_list))
