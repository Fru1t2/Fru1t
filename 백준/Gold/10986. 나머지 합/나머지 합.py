import sys

N, M = map(int, sys.stdin.readline().split())
alist = list(map(int, sys.stdin.readline().split()))
blist = [0]*M
output = 0
result = 0

for i in range(N):
    output += alist[i]
    blist[output % M] += 1

result = blist[0]

for i in range(M):
    result += (blist[i]*(blist[i]-1))//2

print(result)
