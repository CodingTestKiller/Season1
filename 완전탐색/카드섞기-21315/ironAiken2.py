from sys import stdin
input = stdin.readline
import math

n = int(input())
result = [int(x) for x in input().split(' ')]
card = [i for i in range(1, n+1)]

def mix_card(k, card):
    amount = 2**k
    recent = amount

    card = card[len(card)-amount:] + card[:len(card)-amount]
    
    for i in range(2, k+2):
        sep = card[:recent]
        next = 2**(k-i+1)
        sep = sep[len(sep)-next:] + sep[:len(sep)-next]

        card = sep[:] + card[recent:]
        recent = len(sep) - next

    return card        
    
M = int(math.log2(n))

for i in range(1, M + 1):
    shuffled_card = mix_card(i, card[:])
    for j in range(1, M + 1):
        shuffled_card2 = mix_card(j, shuffled_card)

        if result == shuffled_card2:
            print(i, j)
            exit()

# shuffled_card = mix_card(2, card)
# shuffled_card = mix_card(2, shuffled_card)

# print(shuffled_card)


# 2^k 2^(k - i + 1)
# 1 2 3 4 5 6 7 8
# k = 2 / 5 6 7 8 1 2 3 4
# 7 8 5 6 1 2 3 4
# 8 7 5 6 1 2 3 4
# 1 2 3 4 8 7 5 6
# 3 4 1 2 8 7 5 6
# 4 3 1 2 8 7 5 6