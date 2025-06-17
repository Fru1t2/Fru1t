import sys
import itertools
from collections import defaultdict

N, S = map(int, sys.stdin.readline().split())
alist = list(map(int, sys.stdin.readline().split()))

first_half_list = alist[:N//2]
second_half_list = alist[N//2:]
storage = defaultdict(int)
count = 0

for i in range(0, N//2 + 1):
    iters = itertools.combinations(first_half_list, i)
    for item in iters:
        storage[sum(item)] += 1

for j in range(0, len(second_half_list) + 1):
    for item in itertools.combinations(second_half_list, j):
        sum2 = sum(item)
        need = S - sum2
        if need in storage:
            count += storage[need]

if S == 0:
    count -= 1
print(count)

