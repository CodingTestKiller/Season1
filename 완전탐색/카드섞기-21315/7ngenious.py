import sys
input = sys.stdin.readline

N = int(input())
initial = [x for x in range(1,N+1)]
mixed = list(map(int, input().split()))

def shuffle(arr, k, i):
    if len(arr) == 1 :
        return arr[:]

    back = arr[:len(arr) - 2**(k-i+1)]
    front = shuffle(arr[len(arr) - 2**(k-i+1):], k, i+1)
    cnt = front + back
    return cnt

for k1 in range(1, 10):
    if 2**k1 > N:
        break
    cnt1 = shuffle(initial, k1, 1)
    flag = False

    for k2 in range(1, 10):
        if 2**k2 > N:
            break
        cnt2 = shuffle(cnt1, k2, 1)
        if cnt2 == mixed:
            flag = True
            print(k1, k2)
            break
    if flag:
        break