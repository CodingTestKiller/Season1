n = int(input())
Memo = [0 for i in range(11)]
Memo[1] = 1  # 1
Memo[2] = 2  # 1+1 / 2
Memo[3] = 1 + Memo[1] + Memo[2]


for i in range(4, 11):
    Memo[i] = Memo[i-1] + Memo[i-2] + Memo[i-3]

for i in range(n):
    k = int(input())
    print(Memo[k])
