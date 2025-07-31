import sys
from collections import deque

def find(x):
    current = x
    while union_find_list[x] != x:
        x = union_find_list[x]

    while current != x:
        parent = union_find_list[current]
        union_find_list[current] = x
        current = parent

    return x

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return False
    if x < y:
        union_find_list[y] = x
    else:
        union_find_list[x] = y
    return True

def bfs(x, y, island_number):
    queue = deque()
    queue.append((x, y))
    street_map[x][y] = island_number

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx = cx + dx
            ny = cy + dy
            if 0 <= nx < N and 0 <= ny < M:
                if street_map[nx][ny] == 1:
                    street_map[nx][ny] = island_number
                    queue.append((nx, ny))


N, M = map(int, sys.stdin.readline().split())
street_map = []
for _ in range(N):
    street_map.append(list(map(int, sys.stdin.readline().split())))

island_number = 2
for i in range(N):
    for j in range(M):
        if street_map[i][j] == 1:
            bfs(i, j, island_number)
            island_number += 1

edges = []

for i in range(N):
    for j in range(M):
        if street_map[i][j] >= 2:
            current_island = street_map[i][j]
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = i + dx, j + dy
                distance = 0
                while 0 <= nx < N and 0 <= ny < M:
                    if street_map[nx][ny] == 0:
                        distance += 1
                        nx += dx
                        ny += dy
                    elif street_map[nx][ny] == current_island:
                        break
                    else:
                        if distance >= 2:
                            other_island = street_map[nx][ny]
                            edges.append((distance, current_island, other_island))
                        break

edges.sort()
union_find_list = [i for i in range(island_number)]
answer = 0
edge_count = 0

for edge in edges:
    if union(edge[1], edge[2]):
        answer += edge[0]
        edge_count += 1

if edge_count == island_number - 3:
    print(answer)
else:
    print(-1)
