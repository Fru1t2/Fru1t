import sys
from collections import defaultdict

n = int(sys.stdin.readline())
graph = defaultdict(list)
weight = list(map(int, sys.stdin.readline().split()))
dp = [[0, weight[i]] for i in range(n)]
dp.insert(0, [0, 0])

for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(node, parent):
    queue = [(node, parent, False)]
    while queue:
        node, parent, isit = queue.pop()
        if isit:
            for child in graph[node]:
                if child != parent:
                    dp[node][0] += max(dp[child][0], dp[child][1])
                    dp[node][1] += dp[child][0]
        else:
            queue.append((node, parent, True))
            for child in graph[node]:
                if child != parent:
                    queue.append((child, node, False))

def traceback(node, parent, is_parent_selected):
    if is_parent_selected:
        for child in graph[node]:
            if child != parent:
                traceback(child, node, False)
    else:
        if dp[node][1] > dp[node][0]:
            selected.append(node)
            for child in graph[node]:
                if child != parent:
                    traceback(child, node, True)
        else:
            for child in graph[node]:
                if child != parent:
                    traceback(child, node, False)


bfs(1, -1)
print(max(dp[1]))
selected = []
traceback(1, -1, False)
print(*sorted(selected))
