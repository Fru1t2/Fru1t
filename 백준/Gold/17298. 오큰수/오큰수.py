import sys

n = int(sys.stdin.readline())
alist = list(map(int, sys.stdin.readline().split()))
stack = []
ans = [-1] * n

for i in range(n):
    if stack:
        while stack:
            if stack[-1][1] < alist[i]:
                ans[stack[-1][0]] = alist[i]
                stack.pop()
            else:
                break
    stack.append((i, alist[i]))

print(*ans, sep=' ')