import sys

N= int(sys.stdin.readline())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
for l in range(2, N+1):
    for i in range(N - l + 1):
        j = i + l - 1
        dp[i][j] = float('inf')
        for k in range(i, j):
            cost = (dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1])
            dp[i][j] = min(dp[i][j], cost)

print(dp[0][N-1])
