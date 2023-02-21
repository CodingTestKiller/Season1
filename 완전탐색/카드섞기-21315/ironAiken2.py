from sys import stdin
input = stdin.readline

n = int(input())
result = [int(x) for x in input().split(' ')]
card = [i for i in range(1, n+1)]

def mix_card(k, card):
    amount = 2**k

    if amount >= n:
        return
    
    recent = amount

    card = card[len(card)-amount:] + card[:len(card)-amount]
    
    for i in range(2, k+2):
        sep = card[:recent]
        next = 2**(k-i+1)
        sep = sep[len(sep)-next:] + sep[:len(sep)-next]

        card = sep[:] + card[recent:]
        recent = len(sep) - next

    return card        
    
for i in range(1, 1000):

    shuffled_card = mix_card(i, card)
    for j in range(1, 1000):
        shuffled_card = mix_card(j, shuffled_card)

        if result == shuffled_card:
            print(i, j)
            exit()