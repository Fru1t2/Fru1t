import sys
import heapq

N = int(sys.stdin.readline())
for _  in range(N):
    impossible = False
    uncertain = False
    changed_rank = []
    t = int(sys.stdin.readline())
    rank = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    for _ in range(m):
        changed_rank.append(list(map(int, sys.stdin.readline().split())))

    graph = {i: [] for i in rank}
    in_degree = {i: 0 for i in rank}

    for i in range(t):
        for j in range(i + 1, t):
            higher = rank[i]
            lower = rank[j]
            graph[higher].append(lower)
            in_degree[lower] += 1

    for a, b in changed_rank:
        if b in graph[a]:
            graph[a].remove(b)
            in_degree[b] -= 1
            graph[b].append(a)
            in_degree[a] += 1
        else:
            graph[b].remove(a)
            in_degree[a] -= 1
            graph[a].append(b)
            in_degree[b] += 1

    heap = []
    for i in rank:
        if in_degree[i] == 0:
            heapq.heappush(heap, i)

    answer = []
    while heap:
        if len(heap) > 1:
            uncertain = True
        node = heapq.heappop(heap)
        answer.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                heapq.heappush(heap, neighbor)

    for degree in in_degree:
        if in_degree[degree] > 0:
            impossible = True
    if impossible:
        print("IMPOSSIBLE")
    elif uncertain:
        print("?")
    else:
        print(' '.join(map(str, answer)))
