import sys

N = int(sys.stdin.readline())

dp = [[0]*2 for _ in range(N)]
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    dp[i][0] = a
    dp[i][1] = b

dp.sort(key = lambda x: (x[1], x[0]))

cnt = 1
end_time = dp[0][1]
for i in range(1, N):
    if dp[i][0] >= end_time:
        cnt += 1
        end_time = dp[i][1]

print(cnt)