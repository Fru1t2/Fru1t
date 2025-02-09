import sys
from collections import deque


def bfs(start, case, visited, finished):
    queue = deque([start])
    cycle = []

    while queue:
        node = queue.popleft()

        if visited[node]:
            return len(cycle)

        visited[node] = True
        cycle.append(node)

        next_node = case[node]

        if visited[next_node]:
            if next_node in cycle:
                idx = cycle.index(next_node)
                return idx
            return len(cycle)
        queue.append(next_node)

    return len(cycle)


def solve():
    T = int(sys.stdin.readline())
    index = 1
    result = []

    for _ in range(T):
        N = int(sys.stdin.readline())
        data = list(map(int, sys.stdin.readline().split()))
        case = list(map(lambda x: int(x) - 1, data))
        visited = [False] * N
        finished = [False] * N
        answer = 0

        for i in range(N):
            if not visited[i]:
                answer += bfs(i, case, visited, finished)

        result.append(str(answer))
    print("\n".join(result))


if __name__ == "__main__":
    solve()
