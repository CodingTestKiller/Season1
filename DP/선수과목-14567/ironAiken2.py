# bottom-up 방식으로 구현
# 모든 필드 1로 초기화.
# 점화식, s1, s2 일때, dp[s2] = sp[s1] + 1
# 최대값 비교해서 최대값으로 넣기

from sys import stdin
input = stdin.readline

n, m = [int(x) for x in input().split(' ')]

sub = [[int(x) for x in input().split(' ')] for _ in range(m)]

relation = [[] for _ in range(n + 1)]
dp = [0 for _ in range(n + 1)]

for s1, s2 in sub:
    relation[s2].append(s1)

for i in range(1, n + 1):
    if len(relation[i]) == 0:
        dp[i] = 1
        print(dp[i], end=' ')
    else:
        max = 0

        for s in relation[i]:
            if max < dp[s] + 1:
                max = dp[s] + 1

        dp[i] = max
        print(dp[i], end=' ')
