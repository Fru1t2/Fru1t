import sys
from collections import defaultdict

N = int(sys.stdin.readline())
dp = [[0, 1] for _ in range(N + 1)]
graph = defaultdict(list)
for _ in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def iterative_dfs(start):
    stack = [(start, 0, False)]  # (node, parent, visited)
    while stack:
        node, parent, visited = stack.pop()
        if visited:
            for child in graph[node]:
                if child != parent:
                    dp[node][0] += dp[child][1]
                    dp[node][1] += min(dp[child][0], dp[child][1])
        else:
            stack.append((node, parent, True))
            for child in graph[node]:
                if child != parent:
                    stack.append((child, node, False))

iterative_dfs(1)
print(min(dp[1]))




