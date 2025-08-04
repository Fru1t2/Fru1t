import sys
from collections import deque

A, B = map(int, sys.stdin.readline().split())

queue = deque([(A, 1)])
while queue:
    num, trial = queue.popleft()
    if num == B:
        print(trial)
        exit(0)
    if num > B:
        continue
    queue.append((num * 2, trial + 1))
    queue.append((int(str(num)+"1"), trial + 1))

print(-1)