money = int(input())
if money < 2:
    print(-1)
    exit()
cnt_5, money = divmod(money, 5)
# print(cnt_5, money)
if cnt_5 > 0 and money % 2 != 0:
    cnt_5 -= 1
    money += 5
cnt_2, money = divmod(money, 2)
# print(cnt_2, money)

res = cnt_5 + cnt_2

if money != 0:
    print(-1)
else:
    print(res)
