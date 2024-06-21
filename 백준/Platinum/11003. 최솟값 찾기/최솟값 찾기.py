import sys
from collections import deque

N, L = map(int, sys.stdin.readline().split())
alist = list(map(int, sys.stdin.readline().split()))

deq = deque()

for i in range(N):
    while deq and deq[-1][0] > alist[i]:
        deq.pop()
    deq.append((alist[i], i))
    if deq[0][1] <= i - L:
        deq.popleft()
    print(deq[0][0], end=" ")


