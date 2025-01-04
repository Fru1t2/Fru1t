class Stack:
    def __init__(self):
        self.items = []
        self.size_ = 0  # 변수 이름을 size_로 변경

    def push(self, item):
        self.items.append(item)
        self.size_ += 1

    def pop(self):
        if self.size_ > 0:
            self.size_ -= 1
            return self.items.pop()
        else:
            return -1

    def get_size(self):  # 메서드 이름을 get_size로 변경
        return self.size_

    def empty(self):
        return 1 if self.size_ == 0 else 0

    def top(self):
        if self.size_ > 0:
            return self.items[-1]
        else:
            return -1

import sys
number = int(sys.stdin.readline())
stack = Stack()
for _ in range(number):
    command = sys.stdin.readline().split()

    if command[0] == "push":
        stack.push(int(command[1]))
    elif command[0] == "pop":
        print(stack.pop())
    elif command[0] == "size":
        print(stack.get_size())
    elif command[0] == "empty":
        print(stack.empty())
    elif command[0] == "top":
        print(stack.top())
    else:
        exit(-1)
