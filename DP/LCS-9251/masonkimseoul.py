import sys

str1=list(sys.stdin.readline().rstrip())
str2=list(sys.stdin.readline().rstrip())
len1=len(str1)
len2=len(str2)
dp=[[0]*(len2+1) for _ in range(len1+1)]

for i in range(1,len1+1):
    for j in range(1,len2+1):
        if str1[i-1]==str2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

print(dp[-1][-1])

# 솔루션 참고
# 초기엔 문자열을 직접 만들어서 덱에 저장하면서 풀려 하였으나... 하도 안돼서 참고함
# 개수만 세면 됐던 생각보다 간단한 문제
