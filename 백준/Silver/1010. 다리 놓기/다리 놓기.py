import sys
import math

def combinations(n, m):
    return math.factorial(n + m - 1) // (math.factorial(m) * math.factorial(n - 1))

a = int(sys.stdin.readline())
for _ in range(a):
    N, M = map(int, sys.stdin.readline().split())
    print(combinations(N+1, M-N))