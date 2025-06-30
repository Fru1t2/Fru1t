import sys

N = int(sys.stdin.readline())
weight_list = list(map(int, sys.stdin.readline().split()))
num_to_make = int(sys.stdin.readline())
to_make_list = list(map(int, sys.stdin.readline().split()))

dp = [[False] * 40001 for _ in range(N + 1)]
dp[0][0] = True

for i in range(1, N + 1):
    for j in range(40001):
        if dp[i-1][j]:
            dp[i][j] = True
            if j + weight_list[i - 1] <= 40000:
                dp[i][j + weight_list[i - 1]] = True
            dp[i][abs(j - weight_list[i - 1])] = True

for i in range(len(to_make_list)):
    if dp[N][to_make_list[i]]:
        print("Y", end=" ")
    else:
        print("N", end=" ")
