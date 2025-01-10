import sys

number = int(sys.stdin.readline())
stack = []
answer = []
alist = list(map(int, sys.stdin.readline().split()))
for i in range(len(alist)):
    while stack and stack[-1][0] < alist[i]:
        answer.append((alist[i],stack.pop()[1]))
    stack.append((alist[i], i))

for remainder in stack:
    answer.append((-1, remainder[1]))

answer.sort(key=lambda x : x[1])
result = " ".join(str(a) for a,b in answer)
print(result)
