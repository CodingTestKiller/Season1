from sys import stdin

input = stdin.readline
input()
arr = [int(x) for x in input().split()]

for i in range(1, len(arr)):
    arr[i] += arr[i-1]

if arr[-1] % 4 != 0:
    print(0)
elif arr[-1] == 0:
    zero_cnt = arr.count(0)
    print(int((zero_cnt - 1) * (zero_cnt - 2) * (zero_cnt - 3) / 6))
else:
    i = 0
    q1_index = []
    q2_index = []
    q3_index = []

    while i < len(arr):
        if arr[i] == int(arr[-1] / 4):
            q1_index.append(i)
        elif arr[i] == int(arr[-1] / 2):
            q2_index.append(i)
        elif arr[i] == int(arr[-1] / 4 * 3):
            q3_index.append(i)
        i += 1

    result = 0

    for q1 in q1_index:
        for q2 in q2_index:
            if q2 < q1:
                continue
            for q3 in q3_index:
                if q3 < q2:
                    continue
                if q1 < q2 < q3:
                    result += 1
    print(result)
