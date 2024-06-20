import sys

N, M = map(int, sys.stdin.readline().split())
alist = list(map(int, sys.stdin.readline().split()))
blist = [0 for _ in range(N+1)]
for i in range(N):
    if (i == 0):
        blist[0] = 0
        blist[1] = alist[0]
    blist[i+1] = blist[i] + alist[i]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(blist[j]-blist[i-1])