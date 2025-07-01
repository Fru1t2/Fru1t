import sys
n, k = map(int, sys.stdin.readline().split())
coin_list = [int(sys.stdin.readline()) for _ in range(n)]

dp = [0] * (k + 1)
dp[0] = 1 

for coin in coin_list:
    for amount in range(coin, k + 1):
        dp[amount] += dp[amount - coin]

print(dp[k])