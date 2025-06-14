import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, graph, n):
    dist = [INF] * (n + 1)
    dist[start] = 0
    hq = [(0, start)]
    while hq:
        cost, now = heapq.heappop(hq)
        if dist[now] < cost:
            continue
        for nxt, weight in graph[now]:
            if dist[nxt] > cost + weight:
                dist[nxt] = cost + weight
                heapq.heappush(hq, (dist[nxt], nxt))
    return dist

T = int(sys.stdin.readline())
for _ in range(T):
    n, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
        if (a == g and b == h) or (a == h and b == g):
            gh_weight = d

    targets = [int(input()) for _ in range(t)]

    dist_s = dijkstra(s, graph, n)
    dist_g = dijkstra(g, graph, n)
    dist_h = dijkstra(h, graph, n)

    answer = []
    for x in targets:
        path1 = dist_s[g] + gh_weight + dist_h[x]
        path2 = dist_s[h] + gh_weight + dist_g[x]
        if dist_s[x] == min(path1, path2):
            answer.append(x)

    answer.sort()
    print(*answer)
