from itertools import permutations

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for p in permutations(arr, m):
    print(' '.join(map(str, p)))
