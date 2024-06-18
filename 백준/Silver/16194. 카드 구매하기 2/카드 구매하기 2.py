import sys
import math

N = int(sys.stdin.readline())
alist = list(map(int, sys.stdin.readline().strip().split()))
answer = [math.inf for _ in range(N)]
answer[0] = alist[0]
for i in range(1, N):
    for j in range(i+1):
        answer[i] = min(answer[i], alist[j] + (answer[i - j - 1] if i - j - 1 >= 0 else 0))

print(answer[N-1])

