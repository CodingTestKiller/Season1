from sys import stdin
input = stdin.readline

# 1 / 1 1
# 2 / 2 1+1, 2
# 3 / 4 1+1+1, 1+2, 2+1, 3
# 4 / 7 1+1+1+1, 1+1+2, 1+2+1, 1+3, 2+1+1, 2+2, 3+1
# 5 / 12 1+1+1+1+1, 1+2+1+1, 1+1+2+1, 1+1+1+2, 1+2+2, 1+3+1, 1+1+3, 2+1+1+1, 2+2+1, 2+1+2, 2+3, 3+1+1, 3+2

def num_of_case(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return num_of_case(n-1) + num_of_case(n-2) + num_of_case(n-3)
    
t = int(input())

for _ in range(t):
    n = int(input())

    print(num_of_case(n))

    