def count_ways(N: int) -> int:
    count = 0
    m = 1
    while m * (m - 1) // 2 < N:
        if (N - m * (m - 1) // 2) % m == 0:
            count += 1
        m += 1
    return count

import sys

N = int(sys.stdin.readline().strip())
print(count_ways(N))