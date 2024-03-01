import sys

class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return not self.items

a = int(sys.stdin.readline())
for _ in range(a):
    stack1 = stack()
    data = list(sys.stdin.readline().strip())
    for i in range(len(data)):
        if stack1.isEmpty():
            if data[i] == ")":
                stack1.push(data[i])
                print("NO")
                break
            stack1.push(data[i])
        else:
            if stack1.peek() != data[i]:
                stack1.pop()
            else:
                stack1.push(data[i])
    if not stack1.isEmpty() and stack1.items[0] == ")":
        continue

    if stack1.isEmpty():
        print("YES")
    else:
        print("NO")
