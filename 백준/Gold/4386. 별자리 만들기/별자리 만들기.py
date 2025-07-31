import sys
import math

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

def distance(x, y):
    return round(math.dist(x, y), 2)

n = int(sys.stdin.readline())
node_num = 0
node = []
weight = []
for _ in range(n):
    node_num += 1
    x, y = map(float, sys.stdin.readline().split())
    node.append((node_num, (x, y)))

for i in range(n):
    for j in range(i):
        value = distance(node[i][1], node[j][1])
        weight.append((value, node[i][0], node[j][0]))

weight.sort()
answer = 0
union_find_list = [i for i in range(n + 1)]
for wei in weight:
    if union(wei[1], wei[2]):
        answer += wei[0]

print(answer)
