import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
check = [[0 for _ in range(M)] for _ in range(N)]
alist = []
answer = []
for _ in range(N):
    alist.append(list(map(int, sys.stdin.readline().strip())))
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
stack = deque([(0, 0, 1)])
while stack:
    x, y ,minimum = stack.popleft()
    if x == N-1 and y == M-1:
        answer.append(minimum)
    if 0 <= x < N and 0 <= y < M:
        if alist[x][y] == 1 and check[x][y] == 0:
            minimum += 1
            check[x][y] = 1
            for dx, dy in directions:
                stack.append((x + dx, y + dy, minimum))

print(min(answer))
