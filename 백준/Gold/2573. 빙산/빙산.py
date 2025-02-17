import sys
from collections import deque

# 입력 받기
N, M = map(int, sys.stdin.readline().split())
ice_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 4방향 이동
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(x, y, check):
    queue = deque([(x, y)])
    check[x][y] = False

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if ice_map[nx][ny] > 0 and check[nx][ny]:
                    check[nx][ny] = False
                    queue.append((nx, ny))
    return 1


def melt_ice():
    melt_list = []
    for i in range(N):
        for j in range(M):
            if ice_map[i][j] > 0:
                count = 0
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < N and 0 <= ny < M and ice_map[nx][ny] == 0:
                        count += 1
                melt_list.append((i, j, count))

    for x, y, melt in melt_list:
        ice_map[x][y] = max(0, ice_map[x][y] - melt)

year = 0

while True:
    check = [[True] * M for _ in range(N)]
    crack = 0

    for i in range(N):
        for j in range(M):
            if ice_map[i][j] > 0 and check[i][j]:
                crack += bfs(i, j, check)

    if crack >= 2:
        print(year)
        break

    if crack == 0:
        print(0)
        break

    melt_ice()
    year += 1
