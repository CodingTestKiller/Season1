n = int(input())
k = int(input())
L = list(map(int, input().split()))
L.sort()

D = []
for i in range(len(L)-1):
    D.append((i, L[i+1] - L[i]))

D.sort(key=lambda x: -x[1])

k_list = []
for i in D:
    if k > 1:
        k_list.append(i[0])
        k -= 1
S = 0
# print(k_list)
if k_list:
    k_list.sort()
    prev = L[0]
    for i in k_list:
        S += L[i] - prev
        prev = L[i+1]
    S += L[-1] - prev

else:
    S += L[-1] - L[0]
print(S)
