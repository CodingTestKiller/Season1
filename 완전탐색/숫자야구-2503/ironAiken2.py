#머리로 똥싸다가 솔루션 봤습니다 너무 어렵네요,.
from sys import stdin
input = stdin.readline
from itertools import permutations

n = int(input())
num = list(permutations([1,2,3,4,5,6,7,8,9], 3))

for _ in range(n):
    test, s, b = map(int, input().split())
    test = list(str(test))
    remove_cnt = 0

    for i in range(len(num)):
        s_cnt = b_cnt = 0
        i -= remove_cnt

        for j in range(3):
            test[j] = int(test[j])
            if test[j] in num[i]:
                if j == num[i].index(test[j]):
                    s_cnt += 1
                else:
                    b_cnt += 1
    
        if s_cnt != s or b_cnt != b:
            num.remove(num[i])
            remove_cnt += 1

print(len(num))