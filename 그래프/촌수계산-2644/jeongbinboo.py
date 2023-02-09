import sys

input = sys.stdin.readline

n = int(input())
a, b = [int(x) - 1 for x in input().split()]
m = int(input())
person_list = [[0 for _ in range(n)] for _ in range(n)]
visit_list = [0 for _ in range(n)]
result = 0


def dfs(start, target, person_list, visit_list, result):
    ret = 0
    if visit_list[start] == 1:
        return -1
    visit_list[start] = 1
    row = person_list[start]
    result += 1

    for index, person in enumerate(row):
        if person == 1:
            if index == target:
                return result
            else:
                ret = dfs(index, target, person_list, visit_list, result)
                if (ret != -1):
                    return ret
    return -1


for _ in range(m):
    parent_num, child_num = [int(x) - 1 for x in input().split()]
    person_list[parent_num][child_num] = 1
    person_list[child_num][parent_num] = 1

print(dfs(a, b, person_list, visit_list, result))
