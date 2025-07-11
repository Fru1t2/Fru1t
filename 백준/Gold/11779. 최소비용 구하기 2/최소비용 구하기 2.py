import heapq
import sys

num_city = int(sys.stdin.readline())
num_bus = int(sys.stdin.readline())

graph = {i: [] for i in range(1, num_city + 1)}

for _ in range(num_bus):
    u, v, cost = map(int, sys.stdin.readline().split())
    graph[u].append((v, cost))

start_index, end_index = map(int, sys.stdin.readline().split())


def dijkstra(start, end):
    dist = [float('inf')] * (num_city + 1)
    dist[start] = 0
    pq = [(0, start)]

    trace = [-1] * (num_city + 1)

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > dist[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                trace[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    path = []
    current = end
    while current != -1:
        path.append(current)
        current = trace[current]

    path.reverse()
    return dist[end], path

distance, path = dijkstra(start_index, end_index)

if distance == float('inf'):
    print(0)
else:
    print(distance)
    print(len(path))
    print(" ".join(map(str, path)))
