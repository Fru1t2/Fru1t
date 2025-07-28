import sys

def find(num : int):
    root = num
    while union_find_set[root] != root:
        root = union_find_set[root]

    while num != root:
        parent = union_find_set[num]
        union_find_set[num] = root
        num = parent
    return root

def union(num_a : int, num_b : int):
    head_num_a = find(num_a)
    head_num_b = find(num_b)
    if head_num_a == head_num_b:
        return
    if head_num_a > head_num_b:
        union_find_set[head_num_a] = head_num_b
    else:
        union_find_set[head_num_b] = head_num_a
    return

n, m = map(int, sys.stdin.readline().split())
union_find_set = [i for i in range(0, n + 1)]
for _ in range(m):
    action, a, b = map(int, sys.stdin.readline().split())
    if action == 0:
        union(a, b)
    elif action == 1:
        if find(a) != find(b):
            print("NO")
        else:
            print("YES")

