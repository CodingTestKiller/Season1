import sys

arr = str(sys.stdin.readline().rstrip())
quack = "quack"
len_arr = len(arr)
check = [0 for _ in range(len_arr)]
cnt = 0

if len(arr) % 5 != 0 or arr[0] != 'q':
    print(-1)
else:
    for i in range(len_arr):
        index = 0
        check_first_q = False
        if not check[i] and arr[i] == quack[index]:
            check[i] = 1
            index += 1
            for j in range(i, len_arr):
                if not check[j] and quack[index] == arr[j]:
                    check[j] = 1
                    if quack[index] == 'k' and not check_first_q:
                        cnt += 1
                        index = 0
                        check_first_q = True
                    elif quack[index] == 'k' and check_first_q:
                        index = 0
                    else:
                        index += 1
            if index != 0:
                break
    if index != 0:
        print(-1)
    else:
        print(cnt)