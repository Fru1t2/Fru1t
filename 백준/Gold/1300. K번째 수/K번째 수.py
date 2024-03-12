import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

start, end = 1, K

while start <= end:
    mid = (start + end) // 2

    val = 0
    for i in range(1, N + 1):
        val += min(mid // i, N)

    if val >= K:
        value = mid
        end = mid - 1
    else:
        start = mid + 1
print(value)