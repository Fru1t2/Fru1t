import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
in_degree_list= [0 for _ in range(N+1)]
edge_list = {}
heap = []
answer_list = []

for _ in range(M):
    start_index, end_index = map(int, sys.stdin.readline().split())
    in_degree_list[end_index] += 1
    if edge_list.get(start_index, None) is None:
        edge_list[start_index] = [end_index]
    else:
        edge_list[start_index].append(end_index)
for i in range(1, N+1):
    if in_degree_list[i] == 0:
        heapq.heappush(heap, i)

while heap:
    node = heapq.heappop(heap)
    answer_list.append(node)
    for edge in edge_list.get(node, []):
        in_degree_list[edge] -= 1
        if in_degree_list[edge] == 0:
            heapq.heappush(heap, edge)
for answer in answer_list:
    print(answer, end=" ")