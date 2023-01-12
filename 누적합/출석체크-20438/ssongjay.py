import sys

N, K, Q, M = [int(x) for x in sys.stdin.readline().rstrip().split()]

check_students = [1 for _ in range(N + 3)]

sleep = [int(x) for x in sys.stdin.readline().rstrip().split()]
check = [int(x) for x in sys.stdin.readline().rstrip().split()]

for i in range(N + 3):
	if i in check and i not in sleep:
		for j in range(i, N + 3, i):
			if j not in sleep:
				check_students[j] = 0

sum_student = [0 for _ in range(N + 3)]
for i in range(3, N + 3):
	sum_student[i] = sum_student[i - 1] + check_students[i];

for _ in range(M):
	S, E = [int(x) for x in sys.stdin.readline().rstrip().split()]
	print(sum_student[E] - sum_student[S - 1])
