# 문제 제한 시간 2초
# 그래프 최대 크기 10 * 10 - > 100
# 그래프 탐색시 대충 O(n^3)까지 가능
from collections import deque
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]


# 심을 수 있는 곳 가격리스트 (좌표, 가격)
place_price = []

# 중심 상 하 좌 우
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

# 가격 구하기 O(n^2)
for i in range(1, n-1):
    for j in range(1, n-1):
        price = 0
        for k in range(5):
            x = i + dx[k]
            y = j + dy[k]
            price += graph[x][y]
        place_price.append((i, j, price))

# 가격순으로 내림 차순정렬
place_price.sort(key=lambda x: x[2])

# 주위 + 상하좌우
nx = [-1, -1, -1, 0, 0, 0, 1, 1, 1, -2, 2, 0, 0]
ny = [-1, 0, 1, -1, 0, 1, -1, 0, 1, 0, 0, -2, 2]
result = []

for a in place_price:
    die_place = []
    ax = a[0]
    ay = a[1]
    aprice = a[2]
    for i in range(13):
        if 0 <= ax+nx[i] < n and 0 <= ay+ny[i] < n:
            die_place.append((ax+nx[i], ay+ny[i]))
    for b in place_price:
        bx = b[0]
        by = b[1]
        bprice = b[2]
        if (bx, by) in die_place:
            continue
        for i in range(13):
            if 0 <= bx+nx[i] < n and 0 <= by+ny[i] < n:
                die_place.append((bx+nx[i], by+ny[i]))
        for c in place_price:
            cx = c[0]
            cy = c[1]
            cprice = c[2]
            if (cx, cy) in die_place:
                continue
            else:
                result.append(aprice+bprice+cprice)

result.sort()
print(result[0])
