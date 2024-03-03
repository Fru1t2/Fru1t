import sys

N = int(sys.stdin.readline())
alist = list(map(int, sys.stdin.readline().split()))

reverse_alist = alist[::-1]

inc = [1]*N
dec = [1]*N

for i in range(N):
    for j in range(i):
        if alist[i] > alist[j]:
            inc[i] = max(inc[i], inc[j] + 1)

        if reverse_alist[i] > reverse_alist[j]:
            dec[i] = max(dec[i], dec[j] + 1)

dec = dec[::-1]

result = []
for i in range(N):
    result.append(dec[i] + inc[i] - 1)

print(max(result))