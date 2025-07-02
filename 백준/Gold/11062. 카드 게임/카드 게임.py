import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    cards = list(map(int, sys.stdin.readline().split()))

    dp = [[0] * N for _ in range(N)]
    total = [[0] * N for _ in range(N)]

    for i in range(N):
        total[i][i] = cards[i]
        for j in range(i + 1, N):
            total[i][j] = total[i][j - 1] + cards[j]

    for i in range(N):
        dp[i][i] = cards[i]

    for d in range(2, N + 1):
        for i in range(N - d + 1):
            j = i + d - 1
            dp[i][j] = max(
                cards[i] + (total[i + 1][j] - dp[i + 1][j]),
                cards[j] + (total[i][j - 1] - dp[i][j - 1])
            )

    print(dp[0][N - 1])
