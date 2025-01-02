import sys

answer = [0] * 10
number = 1
for _ in range(3):
    number *= int(sys.stdin.readline())

for word in str(number):
    answer[int(word)] += 1

print("\n".join(map(str, answer)))

