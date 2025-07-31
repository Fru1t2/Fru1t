import sys

def find(x):
    current = x
    while union_find_list[x] != x:
        x = union_find_list[x]

    while current != x:
        parent = union_find_list[current]
        union_find_list[current] = x
        current = parent

    return x

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return False
    if x < y:
        union_find_list[y] = x
    else:
        union_find_list[x] = y
    return True

while True:
    m, n = map(int, sys.stdin.readline().split())
    if m == 0 and n == 0:
        break

    union_find_list = [i for i in range(n + 1)]
    path = []
    answer = 0
    total = 0

    for _ in range(n):
        x, y, z = map(int, sys.stdin.readline().split())
        path.append((z, x, y))
        total += z

    path.sort()
    for weight, node_a, node_b in path:
        if union(node_a, node_b):
            answer += weight

    print(total - answer)