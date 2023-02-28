import sys

my_input = sys.stdin.readline

str1, str2 = [my_input().rstrip() for _ in range(2)]
len1 = len(str1)
len2 = len(str2)

result = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]
for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if str1[i - 1] == str2[j - 1]:
            result[i][j] = result[i - 1][j - 1] + 1
        else:
            result[i][j] = max(result[i - 1][j], result[i][j - 1])
print(result[len1][len2])
