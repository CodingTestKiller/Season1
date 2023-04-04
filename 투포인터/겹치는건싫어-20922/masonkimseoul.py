import sys

N, K = map(int,sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

cnt = 0
flag = [0]*200001
repeated = [0]*200001
recorded = []
answer = 0
i = 0
while i < N:
    repeated[numbers[i]] += 1

    if repeated[numbers[i]] == 1:
        flag[numbers[i]] = i

    if repeated[numbers[i]] <= K:
        cnt += 1
        recorded.append(numbers[i])
    else:
        answer = max(answer, cnt)

        for j in range(len(recorded)):
            repeated[recorded[j]] = 0
        recorded.clear()
        #repeated 리스트를 모두 0으로 다시 초기화 시켜주려 했으나 시간초과가 나서 순회한 만큼만 0으로 초기화해줌

        cnt = 0
        i = flag[numbers[i]]
    i += 1

print(max(answer,cnt))
#30m