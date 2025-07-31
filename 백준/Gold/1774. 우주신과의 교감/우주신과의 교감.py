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
    return math.dist(x, y)

N, M = map(int, sys.stdin.readline().split())
node = []
union_find_list = [i for i in range(N + 1)]

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    node.append((i+1, (x, y)))

weight = []
for i in range(N):
    for j in range(i):
        wei = distance(node[i][1], node[j][1])
        weight.append((wei, node[i][0], node[j][0]))
weight.sort()
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    union(x, y)

answer = 0
for wei in weight:
    if union(wei[1], wei[2]):
        answer += wei[0]

print(format(answer, ".2f"))