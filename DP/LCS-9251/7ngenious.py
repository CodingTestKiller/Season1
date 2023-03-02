import sys
input = sys.stdin.readline

word1 = input().strip()
word2 = input().strip()

dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

for i in range(1, len(word1) + 1):
    for j in range(1, len(word2) + 1):
        if word1[i - 1] == word2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(word1)][len(word2)])

# 문제접근이 어려워 솔루션 참고 DP에 대한 개념이 아직 많이 부족한 거 같다