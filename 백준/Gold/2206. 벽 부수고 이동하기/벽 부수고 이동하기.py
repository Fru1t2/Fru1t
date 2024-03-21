import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
data = []
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().strip())))

visited = [[[False]*2 for _ in range(M)] for _ in range(N)]

def bfs():
    q = deque()
    q.append((0, 0, 1, 0))
    visited[0][0][0] = True
    while q:
        x, y, count, wall = q.popleft()
        if x == N - 1 and y == M - 1:
            return count
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if data[nx][ny] == 0 and not visited[nx][ny][wall]:
                    q.append((nx, ny, count + 1, wall))
                    visited[nx][ny][wall] = True
                if data[nx][ny] == 1 and wall == 0:
                    q.append((nx, ny, count + 1, 1))
                    visited[nx][ny][1] = True
    return -1

print(bfs())
