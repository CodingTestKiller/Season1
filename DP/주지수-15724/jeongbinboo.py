import sys

my_input = sys.stdin.readline

n, m = [int(x) for x in my_input().split()]

storing = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
area = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    num_arr = [int(x) for x in my_input().split()]
    for j in range(1, m + 1):
        area[i][j] = num_arr[j - 1]
        storing[i][j] = storing[i - 1][j] + storing[i][j - 1] - \
            storing[i - 1][j - 1] + area[i][j]

k = int(my_input())

for _ in range(k):
    si, sj, ei, ej = [int(x) for x in my_input().split()]
    print(storing[ei][ej] - storing[si - 1][ej] -
          storing[ei][sj - 1] + storing[si - 1][sj - 1])
