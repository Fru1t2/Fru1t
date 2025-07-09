import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
INF = int(1e9)
dp = [INF] * 100001
from_list = [-1] * 100001
queue = deque([N])
dp[N] = 0

while queue:
    node = queue.popleft()

    for next_node in [node - 1, node + 1, node * 2]:
        if 0 <= next_node <= 100000 and dp[next_node] > dp[node] + 1:
            dp[next_node] = dp[node] + 1
            from_list[next_node] = node
            queue.append(next_node)

print(dp[K])

path = []
cur = K
while cur != -1:
    path.append(cur)
    cur = from_list[cur]
print(*reversed(path))
