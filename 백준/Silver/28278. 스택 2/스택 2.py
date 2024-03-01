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
stack1 = stack()
for _ in range(a):
    b = list(sys.stdin.readline().split())

    if b[0] == "1":
        stack1.push(int(b[1]))
    elif b[0] == "2":
        if stack1.isEmpty():
            print("-1")
        else:
            print(stack1.pop())
    elif b[0] == "3":
        print(len(stack1.items))
    elif b[0] == "4":
        print("1" if stack1.isEmpty() else "0")
    else:
        if stack1.isEmpty():
            print("-1")
        else:
            print(stack1.peek())

