from sys import stdin
input = stdin.readline

k = int(input())

ans = [[] for _ in range(k)]
index = -1

def print_building(list, index):
    index += 1

    if len(list) <= 2:
        for num in list:
            ans[index].append(num)
        return
    
    root_id = int(len(list)/2)
    root = list[root_id]

    ans[index].append(root)
    print_building(list[:root_id], index)
    print_building(list[root_id + 1:], index)

order = [int(x) for x in input().split(' ')]

print_building(order, index)

for group in ans:
    for num in group:
        print(num, end = ' ')
    print('')