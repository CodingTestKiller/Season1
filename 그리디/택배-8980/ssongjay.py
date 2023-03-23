import sys

input_ = sys.stdin.readline

N, C = [int(x) for x in input_().split()]
M = int(input_())

send = []
for _ in range(M):
    send.append([int(x) for x in input_().split()])
send.sort(key=lambda x: x[1])
cnt = 0
box = [C] * (N + 1)
for start_vil, end_vil, box_num in send:
    min_box = C
    for i in range(start_vil, end_vil):
        min_box = min(min_box, box[i])
    min_box = min(min_box, box_num)
    for i in range(start_vil, end_vil):
        box[i] -= min_box
    cnt += min_box

print(cnt)
