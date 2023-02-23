import sys


def dfs(i, j, n, m, paper_list, is_visited, count):
    if i >= n or i < 0 or j >= m or j < 0:
        return None
    if count == 4:
        return paper_list[i][j]
    di = [-1, 1, 0, 0]
    dj = [0, 0, 1, -1]
    maximum = 0
    for k in range(4):
        if i + di[k] < 0 or i + di[k] >= n or j + dj[k] < 0 or j + dj[k] >= m or is_visited[i + di[k]][j + dj[k]] == 1:
            continue
        is_visited[i + di[k]][j + dj[k]] = 1
        ret = dfs(i + di[k], j + dj[k], n, m,
                  paper_list, is_visited, count + 1)
        is_visited[i + di[k]][j + dj[k]] = 0
        if ret != None and ret > maximum:
            maximum = ret
    return maximum + paper_list[i][j]


def chk_ou(i, j, n, m, paper_list):
    cost = 0
    up = 0
    down = 0
    for k in range(3):
        if j + k >= m:
            return None
        else:
            cost += paper_list[i][j + k]
    if i - 1 >= 0:
        up = paper_list[i - 1][j + 1]
    if i + 1 < n:
        down = paper_list[i + 1][j + 1]
    return cost + max([up, down])


def chk_uhah(i, j, n, m, paper_list):
    cost = 0
    left = 0
    right = 0
    for k in range(3):
        if i + k >= n:
            return None
        else:
            cost += paper_list[i + k][j]
    if j - 1 >= 0:
        left = paper_list[i + 1][j - 1]
    if j + 1 < m:
        right = paper_list[i + 1][j + 1]
    return cost + max([left, right])


my_input = sys.stdin.readline
n, m = [int(x) for x in my_input().rstrip().split()]
paper_list = [list(map(int, my_input().rstrip().split())) for _ in range(n)]
is_visited = [[0 for _ in range(m)] for _ in range(n)]
maximum = 0
for i in range(n):
    for j in range(m):
        if is_visited[i][j] == 1:
            continue
        is_visited[i][j] = 1
        ret = dfs(i, j, n, m, paper_list, is_visited, 1)
        is_visited[i][j] = 0
        if ret != None and ret > maximum:
            maximum = ret
        ret2 = chk_ou(i, j, n, m, paper_list)
        if ret2 != None and ret2 > maximum:
            maximum = ret2
        ret3 = chk_uhah(i, j, n, m, paper_list)
        if ret3 != None and ret3 > maximum:
            maximum = ret3
print(maximum)
