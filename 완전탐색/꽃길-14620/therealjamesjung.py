from sys import stdin
from itertools import combinations

input = stdin.readline

n = int(input())
flower_map = [[int(x) for x in input().split()] for _ in range(n)]


def check_intersection(point1, point2):
    if abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]) < 3:
        return True
    return False


def get_price(flower_map, point):
    price = flower_map[point[0]][point[1]]
    price += flower_map[point[0]-1][point[1]]
    price += flower_map[point[0]+1][point[1]]
    price += flower_map[point[0]][point[1]-1]
    price += flower_map[point[0]][point[1]+1]

    return price


cases = list(combinations([(x, y)
                          for x in range(1, n-1) for y in range(1, n-1)], 3))

price = 3001

for point1, point2, point3 in cases:
    if check_intersection(point1, point2) or check_intersection(point2, point3) or check_intersection(point3, point1):
        continue
    current_price = get_price(
        flower_map, point1) + get_price(flower_map, point2) + get_price(flower_map, point3)
    price = min(price, current_price)

print(price)
