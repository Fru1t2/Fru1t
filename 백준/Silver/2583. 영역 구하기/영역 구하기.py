import sys
from collections import deque

N,M,K = map(int, sys.stdin.readline().split())
check = [[0] * M for _ in range(N)]
rectangles = []
for _ in range(K):
    data = list(map(int, sys.stdin.readline().split()))
    rectangles.append((data[0], data[1], data[2], data[3]))

for x1, y1, x2, y2 in rectangles:
    for i in range(y1, y2):
        for j in range(x1, x2):
            check[i][j] = 1
answer = 0
areas = []
def finding(x: int, y: int) -> int:
    queue = deque([(x,y)])
    area = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        a, b = queue.popleft()
        if check[a][b]:
            continue
        check[a][b] = 1
        area += 1
        for dx, dy in directions:
            nx, ny = a + dx, b + dy
            if 0 <= nx < len(check) and 0 <= ny < len(check[0]) and not check[nx][ny]:
                queue.append((nx, ny))
    return area

for i in range(N):
    for j in range(M):
        if check[i][j] == 0:
            answer += 1
            areas.append(finding(i, j))

print(answer)
print(" ".join(map(str, sorted(areas))))

