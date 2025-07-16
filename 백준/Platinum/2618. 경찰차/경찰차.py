import sys
from collections import deque

N = int(sys.stdin.readline())
W = int(sys.stdin.readline())
accidents = [tuple(map(int, sys.stdin.readline().split())) for _ in range(W)]

def calc_distance(pos1, pos2) -> int:
    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x1 - x2) + abs(y1 - y2)

dp = [[float("inf") for _ in range(W+1)] for _ in range(W+1)]
dp[0][0] = 0
trace_list = [[(0, 0) for _ in range(W+1)] for _ in range(W+1)]

first_police = (1,1)
second_police = (N,N)

queue = deque([(0,0)])

while queue:
    m, n = queue.popleft()
    next_event = max(m, n) + 1

    if next_event <= W:
        if dp[next_event][n] > dp[m][n] + calc_distance(accidents[next_event - 1],
                                                        accidents[m - 1] if m > 0 else first_police):
            dp[next_event][n] = dp[m][n] + calc_distance(accidents[next_event - 1],
                                                         accidents[m - 1] if m > 0 else first_police)
            trace_list[next_event][n] = (m, n)
            queue.append((next_event, n))

        if dp[m][next_event] > dp[m][n] + calc_distance(accidents[next_event - 1],
                                                        accidents[n - 1] if n > 0 else second_police):
            dp[m][next_event] = dp[m][n] + calc_distance(accidents[next_event - 1],
                                                         accidents[n - 1] if n > 0 else second_police)
            trace_list[m][next_event] = (m, n)
            queue.append((m, next_event))

f_min_value = min(dp[W])
first_num_index = dp[W].index(f_min_value)

s_min_value = min(dp[i][W] for i in range(W+1))
second_num_index = next(i for i in range(W+1) if dp[i][W] == s_min_value)

min_value = min(f_min_value, s_min_value)
print(min_value)

path = []
if min_value == f_min_value:
    m, n = W, first_num_index
else:
    m, n = second_num_index, W

while (m, n) != (0, 0):
    if m > n:
        path.append(1)
        m, n = trace_list[m][n]
    else:
        path.append(2)
        m, n = trace_list[m][n]

for p in reversed(path):
    print(p)