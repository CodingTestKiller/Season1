from sys import stdin
input = stdin.readline

n, m = [int(x) for x in input().split()]
gates = [int(input()) for _ in range(n)]

gates.sort()

start, end = 0, gates[-1] * m


def is_possible(gates: list, limit: int, m: int) -> bool:
    cnt = 0

    for gate in gates:
        if gate > limit:
            break
        cnt += limit // gate
        if cnt >= m:
            return True

    return False


ans = 0

while start <= end:
    middle = (start+end) // 2

    if is_possible(gates, middle, m):
        end = middle-1
        ans = middle
    else:
        start = middle+1

print(ans)
