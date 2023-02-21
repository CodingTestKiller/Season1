from copy import deepcopy
import sys
from collections import deque


def mix_card(card_list, k):
    for_mix = deque()
    for_store = deque()
    1, 2, 3, 4, 5

    for i in range(k + 1):
        if i != 0:
            for _ in range(len(card_list) - 2 ** (k - i + 1)):
                card = card_list.pop()
                for_store.appendleft(card)
        for _ in range(2 ** (k - i)):
            card = card_list.pop()
            for_mix.appendleft(card)
        if len(for_store) != 0:
            while len(for_store) != 0:
                card = for_store.popleft()
                card_list.append(card)
        if len(for_mix) != 0:
            while len(for_mix) != 0:
                card = for_mix.pop()
                card_list.appendleft(card)


my_input = sys.stdin.readline
n = int(input())
card_list = deque([x + 1 for x in range(n)])
card_res = deque(list(map(int, my_input().rstrip().split())))
tmp = 2
k_limit = 1

while tmp < n:
    tmp *= 2
    k_limit += 1

k_limit -= 1

for i in range(1, k_limit + 1):
    for j in range(1, k_limit + 1):
        card_list = deque([x + 1 for x in range(n)])
        mix_card(card_list, i)
        mix_card(card_list, j)
        if (card_list == card_res):
            print(i, j)
            break
