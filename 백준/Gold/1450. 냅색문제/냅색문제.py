import sys
from bisect import bisect_right
from itertools import combinations


N, C = map(int, sys.stdin.readline().split())
weight_list = list(map(int, sys.stdin.readline().split()))
first_half_list = weight_list[:N//2]
second_half_list = weight_list[N//2:]

left_sums = []
for i in range(len(first_half_list) + 1):
    for comb in combinations(first_half_list, i):
        left_sums.append(sum(comb))

right_sums = []
for i in range(len(second_half_list) + 1):
    for comb in combinations(second_half_list, i):
        right_sums.append(sum(comb))

left_sums.sort()
answer = 0
for num in right_sums:
    answer += bisect_right(left_sums, C - num)

print(answer)
