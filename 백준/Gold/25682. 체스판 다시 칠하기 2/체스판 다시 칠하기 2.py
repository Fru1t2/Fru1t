import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())  # 행, 열, 크기

maps = [list(map(str, input().strip())) for _ in range(N)]

alist = [[0] * (M + 1) for _ in range(N + 1)]

for r in range(1, N + 1):
    for c in range(1, M + 1):
        if (r + c) % 2 == 0:
            if maps[r - 1][c - 1] == 'B':
                alist[r][c] = alist[r - 1][c] + alist[r][c - 1] - alist[r - 1][c - 1]
            else:
                alist[r][c] = alist[r - 1][c] + alist[r][c - 1] - alist[r - 1][c - 1] + 1
        else:
            if maps[r - 1][c - 1] == 'W':
                alist[r][c] = alist[r - 1][c] + alist[r][c - 1] - alist[r - 1][c - 1]
            else:
                alist[r][c] = alist[r - 1][c] + alist[r][c - 1] - alist[r - 1][c - 1] + 1

amax = -10000000
amin = 10000000
for r in range(K, N + 1):
    for c in range(K, M + 1):
        amax = max(alist[r][c] - alist[r - K][c] - alist[r][c - K] + alist[r - K][c - K], amax)
        amin = min(alist[r][c] - alist[r - K][c] - alist[r][c - K] + alist[r - K][c - K], amin)

print(min(amin, amax, K * K - amin, K * K - amax))