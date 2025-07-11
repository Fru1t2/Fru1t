import sys
input = sys.stdin.readline

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = float('inf')

dp = [[INF]*(n+1) for _ in range(n+1)]
next_node = [[-1]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dp[i][i] = 0

for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    if dp[u][v] > w:
        dp[u][v] = w
        next_node[u][v] = v

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dp[i][j] > dp[i][k] + dp[k][j]:
                dp[i][j] = dp[i][k] + dp[k][j]
                next_node[i][j] = next_node[i][k]

for i in range(1, n+1):
    row = []
    for j in range(1, n+1):
        row.append(str(dp[i][j] if dp[i][j] != INF else 0))
    print(" ".join(row))

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j or dp[i][j] == INF:
            print(0)
            continue

        path = [i]
        cur = i
        dest = j
        while cur != dest:
            cur = next_node[cur][dest]
            path.append(cur)

        print(len(path), *path)
