import sys

first_list = sys.stdin.readline().strip()
second_list = sys.stdin.readline().strip()

N = len(first_list)
M = len(second_list)

dp = [[0 for _ in range(N + 1)] for _ in range(M + 1)]

for i in range(1, M + 1):
    for j in range(1, N + 1):
        if second_list[i - 1] == first_list[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[M][N])
i = M
j = N
answer = []

while i > 0 and j > 0:
    if second_list[i - 1] == first_list[j - 1]:
        answer.append(first_list[j - 1])
        i -= 1
        j -= 1
    elif dp[i - 1][j] > dp[i][j - 1]:
        i -= 1
    else:
        j -= 1

for word in reversed(answer):
    print(word, end="")