import sys

# 이해 잘 안됨
# 좋은 풀이 있으면 공유 해주세요
N = int(sys.stdin.readline().rstrip())

students = [[int(x) for x in sys.stdin.readline().rstrip().split()] for _ in range(N * N)]
arr = [[0 for _ in range(N)] for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for index in range(N * N):
	student = students[index]
	tmp = []
	for i in range(N):
		for j in range(N):
			if arr[i][j] == 0:
				like = 0
				blank = 0
				for k in range(4):
					num_x = i + dx[k]
					num_y = j + dy[k]
					if 0 <= num_x < N and 0 <= num_y < N:
						if arr[num_x][num_y] in student[1:]:
							like += 1
						if arr[num_x][num_y] == 0:
							blank += 1
				tmp.append([like, blank, i, j])
	tmp.sort(key = lambda x:(-x[0], -x[1], x[2], x[3]))
	arr[tmp[0][2]][tmp[0][3]] = student[0]

result = 0
students.sort()

for i in range(N):
	for j in range(N):
		ans = 0
		for k in range(4):
			num_x = i + dx[k]
			num_y = j + dy[k]
			if 0 <= num_x < N and 0 <= num_y < N:
				if arr[num_x][num_y] in students[arr[i][j] - 1]:
						ans += 1
		if ans != 0:
			result += 10 ** (ans -1)
print(result)
