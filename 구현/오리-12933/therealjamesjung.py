from sys import stdin

input = stdin.readline

sound = input().strip()
check = [False for _ in range(len(sound))]
sound_len = len(sound)

cnt = 0
validate = 0

if sound_len % 5 != 0:
    print(-1)
    exit()


def search(sound, check, index, sound_len, value):
    while index < sound_len:
        if sound[index] == value and check[index] == False:
            check[index] = True
            return index
        index += 1
    return -1


cnt = 0
while True:
    index = 0
    validate = check.count(False)
    while index < sound_len:
        index = search(sound, check, index, sound_len, 'q') + 1
        if index == 0:
            break
        index = search(sound, check, index, sound_len, 'u') + 1
        if index == 0:
            break
        index = search(sound, check, index, sound_len, 'a') + 1
        if index == 0:
            break
        index = search(sound, check, index, sound_len, 'c') + 1
        if index == 0:
            break
        index = search(sound, check, index, sound_len, 'k') + 1
        if index == 0:
            break
    cnt += 1
    if validate == check.count(False):
        if check.count(False) == 0:
            print(cnt-1)
            break
        else:
            print(-1)
            break
    elif (validate - check.count(False)) % 5 != 0:
        print(-1)
        break
