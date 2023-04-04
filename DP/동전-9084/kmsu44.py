
T = int(input())
for i in range(T):
    n = int(input())
    kind_list = list(map(int, input().split()))
    goal = int(input())
    Memo = [0 for _ in range(goal + 1)]
    Memo[0] = 1
    for kind in kind_list:
        for i in range(1, goal+1):
            if i >= kind:
                Memo[i] += Memo[i-kind]
    print(Memo[goal])
