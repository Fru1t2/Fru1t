from itertools import permutations

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
seen = set()
for p in permutations(arr, m):
    if p not in seen:
        print(' '.join(map(str, p)))
        seen.add(p)
