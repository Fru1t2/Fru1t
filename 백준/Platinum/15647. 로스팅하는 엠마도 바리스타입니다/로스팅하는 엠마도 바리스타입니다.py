import sys
from collections import defaultdict, deque

n = int(sys.stdin.readline())
graph = defaultdict(list)
dp = [0 for _ in range(n + 1)]
subtree_size = [0 for _ in range(n + 1)]
for _ in range(n - 1):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def bfs1(root):
    stack = [(root, -1, False)]

    while stack:
        node, parent, is_post = stack.pop()

        if is_post:
            subtree_size[node] = 1
            for v, w in graph[node]:
                if v == parent:
                    continue
                subtree_size[node] += subtree_size[v]
                dp[node] += dp[v] + subtree_size[v] * w
        else:
            stack.append((node, parent, True))
            for v, w in graph[node]:
                if v == parent:
                    continue
                stack.append((v, node, False))


from collections import deque

def bfs2():
    queue = deque([1])
    visited = [False] * (n + 1)
    visited[1] = True

    while queue:
        u = queue.popleft()
        for v, w in graph[u]:
            if visited[v]:
                continue
            dp[v] = dp[u] - subtree_size[v] * w + (n - subtree_size[v]) * w
            visited[v] = True
            queue.append(v)


bfs1(1)
bfs2()
dp.pop(0)
print(*dp, sep='\n')

