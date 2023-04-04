str1 = input()
str2 = input()
m = len(str1)+1
n = len(str2)+1

Memo = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            continue
        elif str1[j-1] == str2[i-1]:
            Memo[i][j] = Memo[i-1][j-1] + 1
        else:
            Memo[i][j] = max(Memo[i-1][j], Memo[i][j-1])
print(Memo[-1][-1])
