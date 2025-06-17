import sys

N, S = map(int, sys.stdin.readline().split())
alist = list(map(int, sys.stdin.readline().split()))

first, second = 0, 0
current_sum = 0
num = 0
answer = N + 1
is_true = False

while current_sum < S and second < N:
    current_sum += alist[second]
    second += 1
if current_sum >= S:
    is_true = True
    answer = min(answer, second - first)
    while current_sum >= S:
        is_true = True
        answer = min(answer, second - first)
        current_sum -= alist[first]
        first += 1

while second < N:
    current_sum += alist[second]
    second += 1
    while current_sum >= S:
        is_true = True
        answer = min(answer, second - first)
        current_sum -= alist[first]
        first += 1

print(answer if is_true else 0)


