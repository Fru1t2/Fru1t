import sys
sys.setrecursionlimit(10 ** 9)

m, n = map(int, sys.stdin.readline().split())
arr = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for i in range(m)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def is_range(x, y, now):
    return 0 <= x < m and 0 <= y < n and arr[x][y] < now


def solution(x, y):
    if x == m - 1 and y == n - 1:
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            ax, ay = x + dx[i], y + dy[i]
            if is_range(ax, ay, arr[x][y]):
                dp[x][y] += solution(ax, ay)

    return dp[x][y]


print(solution(0, 0))