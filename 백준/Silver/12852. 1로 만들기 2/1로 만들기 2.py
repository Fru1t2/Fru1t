import sys

N = int(sys.stdin.readline())

dp = [0 for _ in range(N + 1)]
from_list = [0 for _ in range(N + 1)]

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    from_list[i] = i - 1

    if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
        dp[i] = dp[i // 2] + 1
        from_list[i] = i // 2

    if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
        dp[i] = dp[i // 3] + 1
        from_list[i] = i // 3

path = []
current = N
while current != 0:
    path.append(current)
    current = from_list[current]

print(dp[N])
print(*path)