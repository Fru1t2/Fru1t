import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
alist = list(map(int, sys.stdin.readline().split()))


LIS = []
for num in alist:
    if len(LIS) == 0 or num > LIS[-1]:
        LIS.append(num)
    else:
        index = bisect_left(LIS, num)
        LIS[index] = num
print(len(LIS))
