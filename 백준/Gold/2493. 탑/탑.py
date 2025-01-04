import sys

number = int(sys.stdin.readline())
stack = []
answer = [0] * number
tower = list(map(int, sys.stdin.readline().split()))
for i in range(number):
    if not stack:
        stack.append((tower[i], i+1))
        continue

    while stack:
        if stack[-1][0] < tower[i]:
            stack.pop()

        if stack:
            if stack[-1][0] > tower[i]:
                answer[i] = stack[-1][1]
                stack.append((tower[i], i+1))
                break
        else:
            stack.append((tower[i], i+1))
            break

print(" ".join(map(str,answer)))