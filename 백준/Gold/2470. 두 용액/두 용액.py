import sys

N = int(sys.stdin.readline())
value_list = list(map(int, sys.stdin.readline().split()))
value_list.sort()

start, end = 0, N - 1
num_difference = float('inf')
answer = (0, 0)

while start < end:
    total = value_list[start] + value_list[end]
    if abs(total) < num_difference:
        num_difference = abs(total)
        answer = (value_list[start], value_list[end])

    if total < 0:
        start += 1
    else:
        end -= 1

print(answer[0], answer[1])
