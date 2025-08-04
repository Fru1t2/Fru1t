import sys
from collections import defaultdict

N = int(sys.stdin.readline())
graph = defaultdict(list)
human_num = list(map(int, sys.stdin.readline().split()))
human_num.insert(0, 0)
dp = [[0, human_num[i]] for i in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(node, parent):
    queue = [(node, parent, False)]
    while queue:
        current, parent, flag = queue.pop()
        if flag:
            for child in graph[current]:
                if child != parent:
                    dp[current][0] += max(dp[child][1], dp[child][0])
                    dp[current][1] += dp[child][0]
        else:
            queue.append((current, parent, True))
            for child in graph[current]:
                if child != parent:
                    queue.append((child, current, False))

bfs(1, -1)
print(max(dp[1]))