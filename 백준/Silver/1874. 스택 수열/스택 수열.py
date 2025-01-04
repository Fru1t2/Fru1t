import sys

number = int(sys.stdin.readline())
stack = []
start = 1
output = []
is_possible = True

for _ in range(number):
    command = int(sys.stdin.readline())
    if command < start:
        if stack and stack[-1] == command:
            stack.pop()
            output.append("-")
        else:
            is_possible = False
            break
    else:
        while start <= command:
            stack.append(start)
            output.append("+")
            start += 1
        stack.pop()
        output.append("-")

if is_possible:
    print("\n".join(output))
else:
    print("NO")
