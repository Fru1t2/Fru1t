import sys

number = int(sys.stdin.readline())
stack = []
for _ in range(number):
    command = int(sys.stdin.readline())
    if command == 0:
        stack.pop()
    else:
        stack.append(command)

print(sum(stack))