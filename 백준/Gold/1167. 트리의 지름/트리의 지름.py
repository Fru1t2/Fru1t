from collections import deque
import sys

def bfs(start):
    visited = [False] * (N + 1)
    queue = deque([(start, 0)])
    visited[start] = True
    farthest_node = start
    max_cost = 0

    while queue:
        current_node, total_cost = queue.popleft()
        if total_cost > max_cost:
            max_cost = total_cost
            farthest_node = current_node
        for next_node, weight in adj[current_node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, total_cost + weight))
    return farthest_node, max_cost

N = int(sys.stdin.readline())
adj = [[] for _ in range(N + 1)]
for _ in range(N):
    data = list(map(int, sys.stdin.readline().split()))
    node = data[0]
    i = 1
    while data[i] != -1:
        neighbor = data[i]
        weight = data[i + 1]
        adj[node].append((neighbor, weight))
        i += 2

farthest_node, _ = bfs(1)
_, diameter = bfs(farthest_node)

print(diameter)
