import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(N)]
from_list = [i for i in range(N)]

for i in range(1, N):
    for j in range(0, i):
        if num_list[j] < num_list[i]:
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                from_list[i] = j
max_index = dp.index(max(dp))
print(max(dp) + 1)
current = max_index
answer_list = []
while True:
    answer_list.append(num_list[current])
    if current == from_list[current]:
        break
    current = from_list[current]

print(*reversed(answer_list))
