import sys

number = int(sys.stdin.readline())
stack = []
answer = 0
for i in range(number):
    building = int(sys.stdin.readline())

    while stack and stack[-1][0] <= building:
        answer += i - stack[-1][1] - 1
        stack.pop()
    stack.append((building, i))

for i in range(0, len(stack)-1):
    answer += stack[-1][1] - stack[i][1]

print(answer)