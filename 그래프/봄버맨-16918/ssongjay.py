import sys

R, C, N = [int(x) for x in sys.stdin.readline().rstrip().split()]

bomb_map = [[1 for _ in range(C)] for _ in range(R)]

input_map = []

for _ in range(R):
    input_map.append(str(sys.stdin.readline().rstrip().split()))

for i in range(R):
    for j in range(C):
        if input_map[i][j] == 'O':
            bomb_map[i][j - 2] = 0
        

print(bomb_map)