from sys import stdin
input = stdin.readline

sound = [str(x) for x in input().strip()]
# strip 은 문자열 앞뒤의 줄바꿈 제거 함수.
check = ['q', 'u', 'a', 'c', 'k']
cnt = 0
index = 0


if len(sound) % 5 != 0:
    print(-1)
    exit()

while True:
    for i in range(len(sound)):
        if sound[i] == check[index]:
            index += 1
            if (index > 4):
                index = 0
            sound[i] = ' '
    cnt += 1
    sound = [i for i in sound if i not in ' ']
    if index != 0 or len(sound) == 0:
        break

if len(sound) == 0:
    print(cnt)
else:
    print(-1)
