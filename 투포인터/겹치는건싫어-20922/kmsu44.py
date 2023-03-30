from collections import deque
n, k = map(int, (input().split()))
L = [0] + list(map(int, input().split()))
count_dict = {i: 0 for i in range(200001)}
P1 = 1
res = 1
for index in range(1, n+1):
    num = L[index]
    count_dict[num] += 1
    if count_dict[num] > k:
        res = max(res, index - P1)
        while L[P1] != num:
            P1_num = L[P1]
            count_dict[P1_num] -= 1
            P1 += 1
        P1 += 1
        count_dict[num] -= 1
res = max(res, index - P1 + 1)
print(res)
