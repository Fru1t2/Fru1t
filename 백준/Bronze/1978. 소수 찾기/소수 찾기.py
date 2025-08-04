

import sys

N = int(sys.stdin.readline())
alist = list(map(int, sys.stdin.readline().split()))

answer = 0
for x in alist:
    for i in range(2, x+1):
        if x % i == 0:
            if x == i:
                answer += 1

            break

print(answer)