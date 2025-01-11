import sys

case = list(sys.stdin.readline().strip())
stack = []
temp = 1
answer = 0

for i, word in enumerate(case):
    if word == "(":
        stack.append(word)
        temp *= 2
    elif word == "[":
        stack.append(word)
        temp *= 3
    elif word == ")":
        if not stack or stack[-1] != "(":
            print(0)
            sys.exit(0)
        if case[i - 1] == "(":
            answer += temp
        stack.pop()
        temp //= 2
    elif word == "]":
        if not stack or stack[-1] != "[":
            print(0)
            sys.exit(0)
        if case[i - 1] == "[":
            answer += temp
        stack.pop()
        temp //= 3  

if stack:
    print(0)
else:
    print(answer)
