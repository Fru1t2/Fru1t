import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

current_lis_list = []
dp = [0 for _ in range(N)]

for i in range(N):
    len_cur_lis_list = len(current_lis_list)
    opt_index = bisect_left(current_lis_list, num_list[i])
    if opt_index == len_cur_lis_list:
        current_lis_list.append(num_list[i])
    else:
        current_lis_list[opt_index] = num_list[i]
    dp[i] = opt_index + 1


max_value = max(dp)
print(max_value)

result = []
target_len = max_value
last_val = float('inf')

for i in range(N-1, -1, -1):
    if dp[i] == target_len and num_list[i] < last_val:
        result.append(num_list[i])
        last_val = num_list[i]
        target_len -= 1
        if target_len == 0:
            break

print(*reversed(result))
