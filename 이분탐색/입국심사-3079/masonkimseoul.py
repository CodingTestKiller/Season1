import sys

N, M = map(int, sys.stdin.readline().split())
immigration = sorted([int(sys.stdin.readline()) for _ in range(N)])
s, e, answer = 1, immigration[-1] * M, float('inf')

while s <= e:
    mid = (s + e) // 2
    cnt = 0
    for i in immigration:
        cnt += mid // i
        #어차피 모든 입국심사 테이블은 동시에 진행됨

    if cnt >= M:
        answer = min(answer, mid)
        e = mid - 1
    else:
        s = mid + 1

print(answer)
#2h

'''
7 10
0 7 10 0
1 0 3 7
2 4 0 10
3 0 6 14
4 1 0 20
5 0 9 21
6 0 2 28

2 3 3 4 6 8 9
0 2 3 3 4 6 8 9 0
1 0 1 1 2 4 6 7 2
  2 1 1 2 4 6 7
3 1 0 0 1 3 5 6 3
  1 3 3 1 3 5 6
5 0 2 2 0 2 4 5 4
  2 2 2 6 2 4 5
9 0 0 0 2 0 2 3 6
  2 3 3 2 6 2 3
10 0 1 1 0 4 6 7 8

'''