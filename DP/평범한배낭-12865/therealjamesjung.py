from sys import stdin

input = stdin.readline

n, k = [int(x) for x in input().split()]

values = []
weights = []

for _ in range(n):
    weight, value = [int(x) for x in input().split()]
    weights.append(weight)
    values.append(value)

n = len(values)
cache = [0] * (k + 1)

for i in range(n):
    for j in range(k, weights[i]-1, -1):
        cache[j] = max(cache[j], cache[j-weights[i]] + values[i])

print(cache[k])
