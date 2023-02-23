
import sys
inp = sys.stdin.readline
n = int(inp().rstrip())
deck = [i for i in range(1,n+1)]
shuffled = [x for x in map(int,inp().rstrip().split())]
def shuffle(deck,k,ran):
    hand_deck = deck[:ran]
    index = 2**k
    temp_front = hand_deck[-index:]
    temp_back = hand_deck[:-index]
    deck = temp_front + temp_back + deck[ran:]
    if(k>0):
        deck = shuffle(deck,k-1,index)
    return deck
for i in range(n):
    if(2**i >= n):
        max_k = i-1
        break
for i in range(1,max_k+1):    
    first = shuffle(deck,i,n)
    for j in range(1,max_k+1):
        second = shuffle(first,j,n)
        if(second == shuffled):
            print(i,j)
            exit()
