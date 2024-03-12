import sys

A = int(sys.stdin.readline())
for _ in range(A):
    N = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    sums = [0] * (N + 1)
    dp = [[0] * N for _ in range(N)]


    for i in range(1, N + 1):
        sums[i] = sums[i - 1] + nums[i - 1]

    for l in range(2, N + 1):   #길이길이길이길이
        for i in range(N - l + 1):  #몇번돌래몇번돌래
            j = i + l - 1       # endendendend
            dp[i][j] = float('inf')     #초기화 무한대 걍 여따씀

            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + sums[j + 1] - sums[i])


    print(dp[0][N - 1])

