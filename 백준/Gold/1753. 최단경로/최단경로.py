import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
start_vertex = int(sys.stdin.readline())

graph = [[] for _ in range(V + 1)]
distance = [float('inf') for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

def dijkstra(start_vertex):
    hq = []
    distance[start_vertex] = 0
    heapq.heappush(hq, (distance[start_vertex], start_vertex))
    while hq:
        d, v = heapq.heappop(hq)
        if distance[v] < d:
            continue

        for v, w in graph[v]:
            cost = d + w
            if cost  < distance[v]:
                distance[v] = cost
                heapq.heappush(hq, (distance[v], v))
                
if __name__ == '__main__':
    dijkstra(start_vertex)
    for i in range(1, V + 1):
        print(distance[i] if distance[i] != float('inf') else "INF")

