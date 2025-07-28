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

N = int(sys.stdin.readline())
union_find_set = [i for i in range(N + 1)]
M = int(sys.stdin.readline())
for i in range(1, N + 1):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(1, N + 1):
        if row[j - 1] == 1:
            union(i, j)


plan = list(map(int, sys.stdin.readline().split()))
first_root = find(plan[0])
is_connected = all(find(city) == first_root for city in plan)
if is_connected:
    print("YES")
else:
    print("NO")

