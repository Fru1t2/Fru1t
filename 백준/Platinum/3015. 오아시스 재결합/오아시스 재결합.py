import sys

N = int(sys.stdin.readline())
heights = [int(sys.stdin.readline()) for _ in range(N)]

stack = []
result = 0

for height in heights:
    while stack and stack[-1][0] < height:
        result += stack.pop()[1]

    if stack and stack[-1][0] == height:
        count = stack.pop()[1]
        result += count
        if stack:
            result += 1
        stack.append((height, count + 1))
    else:
        if stack:
            result += 1
        stack.append((height, 1))


print(result)
