import sys

alist = []
check = []
N = int(sys.stdin.readline())
for _ in range(N):
    alist.append(list(map(int, sys.stdin.readline().split())))

alist.sort(key=lambda x:x[0])
for i in range(N):
    check.append(alist[i][1])

inc = [1]*N
for i in range(N):
    for j in range(i):
        if check[i] > check[j]:
            inc[i] = max(inc[i], inc[j] + 1)

print(N - max(inc))
