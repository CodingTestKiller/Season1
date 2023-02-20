from sys import stdin

input = stdin.readline


def shuffle(target: list, k: int) -> list:
    tmp = target[-2**k:]
    remainder = target[:-2**k]
    k -= 1
    while k >= 0:
        tmp_remainder = tmp[2**(k+1):]
        tmp = tmp[:2**(k+1)]
        tmp = tmp[-2**k:] + tmp[:-2**k] + tmp_remainder
        k -= 1
    return tmp + remainder


n = int(input())
result = [int(x) for x in input().split()]

cases = [(x, y) for x in range(1, 10) for y in range(1, 10)]

for x, y in cases:
    result1 = shuffle(list(range(1, n+1)), x)
    result2 = shuffle(result1, y)

    if result2 == result:
        print(x, y)
        break
