N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

dp = [0]*(K+1)

for i in range(N):
    for j in range(K, 0, -1):
        if items[i][0] <= j:
            dp[j] = max(dp[j], dp[j-items[i][0]] + items[i][1])

print(dp[K])