import sys

test_case = 0

def dfs(node, parent):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if dfs(neighbor, node):
                return True
        elif neighbor != parent:
            return True
    return False

while True:
    test_case += 1
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    tree = 0
    graph = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    for _ in range(m):
        v, u = map(int, sys.stdin.readline().split())
        graph[v].append(u)
        graph[u].append(v)

    for i in range(1, n+1):
        if not visited[i]:
            if not dfs(i, -1):
                tree += 1

    if tree == 0:
        print(f"Case {test_case}: No trees.")
    elif tree == 1:
        print(f"Case {test_case}: There is one tree.")
    else:
        print(f"Case {test_case}: A forest of {tree} trees.")




