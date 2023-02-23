import sys

input_ = sys.stdin.readline

N = int(input_())
tmps = list(range(123, 999))
for _ in range(N):
    numbers, strike, ball = [int(x) for x in input_().rstrip().split()]
    for tmp in tmps[:]:
        strike_cnt, ball_cnt = 0, 0
        for j in range(3):
            if str(numbers)[j] == str(tmp)[j]:
                strike_cnt += 1
            elif str(numbers)[j] in str(tmp):
                ball_cnt += 1
        if strike_cnt != strike or ball_cnt != ball:
            tmps.remove(tmp)
            if len(tmps) == 0:
                print(0)
                exit()

for tmp in tmps[:]:
    a = tmp // 100
    b = (tmp % 100) // 10
    c = tmp % 10
    if b == 0 or c == 0:
        tmps.remove(tmp)
    if a == b or b == c or a == c:
        tmps.remove(tmp)
print(len(tmps))
