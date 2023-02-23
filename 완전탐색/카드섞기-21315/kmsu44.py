# 시간 1초 N -> 1000 => O(N^2)정도 까지
# 메모리 제한 1024MB -> 메모리 충분?
# 1 <= K, 2^K < N(1000) -> K < 10
# 1 -> 밑에서 2^k개의 카드를 더미의 맨 위로 올린다.
# 2 ~ k+1 -> 올린 카드 중 밑에서 2^(k-i+1)개의 카드를 더미의 맨 위로 올린다.
import math
n = int(input())
L = list(map(int, input().split()))


def suffle(cardlist, index):
    if index == 0:
        return cardlist
    divide_cardlist = cardlist[len(cardlist)-index:]
    return suffle(divide_cardlist, index//2) + cardlist[:len(cardlist)-index]


result = []
M = int(math.log2(n))
for k1 in range(1, M+1):
    for k2 in range(1, M+1):
        card_list = [i for i in range(1, n+1)]
        if suffle(suffle(card_list, 2**k1), 2**k2) == L:
            # print(k1, k2) -> 이렇게 출력하면 왜 점수가 안뜨지..
            result.append((k1, k2))
print(*result[0])
