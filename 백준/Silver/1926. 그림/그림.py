import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
check = [[0 for _ in range(M)] for _ in range(N)]
alist = []
for _ in range(N):
    alist.append(list(map(int, sys.stdin.readline().split())))

def solve(n: int, m: int) -> int:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    area = 0
    stack = deque([(n, m)])
    while stack:
        x, y = stack.popleft()
        if 0 <= x < N and 0 <= y < M and alist[x][y] == 1 and check[x][y] == 0:
            area += 1
            check[x][y] = 1
            for dx, dy in directions:
                stack.append((x + dx, y + dy))
    return area

answer = 0
num = 0
for i in range(N):
    for j in range(M):
        if alist[i][j] == 1 and check[i][j] == 0:
            num += 1
            answer = max(answer, solve(i, j))

print(num)
print(answer)

