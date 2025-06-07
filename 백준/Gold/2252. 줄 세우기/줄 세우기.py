import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
in_degree_list= [0 for _ in range(N+1)]
edge_list = {}

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    if edge_list.get(start, None) is None:
        edge_list[start] = [end]
    else:
        edge_list[start].append(end)
    in_degree_list[end] += 1

queue = deque()
answer_list = []
for i in range(1, N+1):
    if in_degree_list[i] == 0:
        queue.append(i)
while queue:
    start_vertex = queue.popleft()
    answer_list.append(start_vertex)
    for end_vertex in edge_list.get(start_vertex, []):
        in_degree_list[end_vertex] -= 1
        if in_degree_list[end_vertex] == 0:
            queue.append(end_vertex)

for answer_vertex in answer_list:
    print(answer_vertex, end=" ")

