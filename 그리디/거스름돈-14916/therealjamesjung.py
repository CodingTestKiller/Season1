from sys import stdin
input = stdin.readline

n = int(input())

five_cnt = n // 5 - 1
five_cnt = 0 if five_cnt < 0 else five_cnt
answer = [0, -1, 1, -1, 2, 1, 3, 2, 4, 3]

print(five_cnt + answer[n - five_cnt * 5]
      ) if answer[n - five_cnt * 5] != -1 else print(-1)
