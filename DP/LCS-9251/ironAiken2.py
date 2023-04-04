from sys import stdin
input = stdin.readline

s1 = ['']
s2 = ['']
s1.extend([x for x in input().strip()])
s2.extend([x for x in input().strip()])

#가로 = s2 세로 = s1
#인덱스 에러 방지 위, 왼쪽에 한줄씩 추가

cnt = [[0 for _ in range(len(s2))] for _ in range(len(s1))]

for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        # s1 문자들을 고정하고 s2로 탐색
        # 왼쪽 윗 대각선이 이전까지의 공통 문자를 의미.
        if s1[i] == s2[j]:
            cnt[i][j] = cnt[i-1][j-1] + 1
        else:
            cnt[i][j] = max(cnt[i-1][j], cnt[i][j-1])

print(cnt[-1][-1])