import sys


def find(x):
    root = x
    while parent[root] != root:
        root = parent[root]

    while x != root:
        next_x = parent[x]
        parent[x] = root
        x = next_x
    return root


def union(num_a, num_b):
    head_num_a = find(num_a)
    head_num_b = find(num_b)

    if head_num_a == head_num_b:
        return False
    if head_num_a > head_num_b:
        parent[head_num_a] = head_num_b
    else:
        parent[head_num_b] = head_num_a
    return True

V, E = map(int, sys.stdin.readline().split())
parent = [i for i in range(V + 1)]
edges = []
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c, a, b))

edges.sort()
answer = 0
edge_cnt = 0

for cost, a, b in edges:
    if union(a, b):
        answer += cost
        edge_cnt += 1
        if edge_cnt == V - 1:
            break

print(answer)
