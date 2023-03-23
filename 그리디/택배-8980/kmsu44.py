n, truck_weight = map(int, input().split())
k = int(input())
info = [list(map(int, input().split())) for _ in range(k)]

info.sort(key=lambda x: [x[0], x[1]])
res = 0
# for i in info:
#     print(i)
truck = {i: 0 for i in range(1, n+1)}
for position in range(1, n+1):
    res += truck[position]
    truck[position] = 0
    for info_idx, info_data in enumerate(info):
        s, r, w = info_data
        if s < position:
            continue
        if s > position:
            break
        if s == position:
            t = 0
            for i in truck:
                t += truck[i]
            # 트럭 용량이 남았을 경우 트럭에 짐을 실는다.
            # 전부 담을 수 있으면 전부 담기
            if t + w <= truck_weight:
                truck[r] += w
            # 부분만 담기
            else:
                # 부분적으로 남는 부분이 있으면 담기
                if t < truck_weight:
                    rest = truck_weight - t
                    truck[r] += rest
                    w -= rest
                # 더 나은 경우 배달 취소 하기
                for truck_index in range(n, 0, -1):
                    if w == 0:
                        break
                    if truck[truck_index] > 0:
                        if r < truck_index:
                            if w <= truck[truck_index]:
                                truck[truck_index] -= w
                                truck[r] += w
                                w = 0
                            # w > tw
                            else:
                                tt = truck[truck_index]
                                truck[truck_index] = 0
                                truck[r] += tt
                                w -= tt
    # print(truck)
print(res)
