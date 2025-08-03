import sys
from collections import defaultdict

sys.setrecursionlimit(10**5)
graph = defaultdict(list)
N, R, Q = map(int, sys.stdin.readline().split())
for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [1 for _ in range(N + 1)]

def dfs(node, parent):
    for child in graph[node]:
        if child != parent:
            dfs(child, node)
            dp[node] += dp[child]
    return
dfs(R, 0)
for _ in range(Q):
    query = int(sys.stdin.readline())
    print(dp[query])


