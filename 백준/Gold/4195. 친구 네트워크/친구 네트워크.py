import sys
from collections import defaultdict

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
        size[head_num_b] += size[head_num_a]
    else:
        union_find_set[head_num_b] = head_num_a
        size[head_num_a] += size[head_num_b]
    return

T = int(sys.stdin.readline())
for _ in range(T):
    F = int(sys.stdin.readline())
    union_find_set = [i for i in range(F * 2 + 1)]
    size = [1 for _ in range(2 * F + 1)]
    dict = defaultdict(int)
    num = 1
    for _ in range(F):
        name1, name2 = sys.stdin.readline().split()
        if name1 not in dict:
            dict[name1] = num
            num += 1
        if name2 not in dict:
            dict[name2] = num
            num += 1

        i, j = dict[name1], dict[name2]
        union(i, j)
        print(size[find(i)])


