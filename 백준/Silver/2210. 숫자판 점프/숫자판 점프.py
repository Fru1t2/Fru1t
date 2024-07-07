from collections import deque
import sys
def bfs(start_x, start_y, graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(start_x, start_y, str(graph[start_x][start_y]))])
    results = set()

    while queue:
        x, y, path = queue.popleft()

        if len(path) == 6:
            results.add(path)
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 그리드 내에 있는지 확인
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                queue.append((nx, ny, path + str(graph[nx][ny])))

    return results

data = []

for i in range(5):
    data.append(list(map(int, sys.stdin.readline().split())))

unique_numbers = set()

for i in range(5):
    for j in range(5):
        unique_numbers.update(bfs(i, j, data))

# 총 6자리 숫자의 개수 출력
print(len(unique_numbers))
