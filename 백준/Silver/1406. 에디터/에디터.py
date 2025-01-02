class Editor:
    def __init__(self, initial_text):
        self.left = list(initial_text)
        self.right = []

    def move_left(self):
        if self.left:
            self.right.append(self.left.pop())

    def move_right(self):
        if self.right:
            self.left.append(self.right.pop())

    def delete(self):
        if self.left:
            self.left.pop()

    def insert(self, char):
        self.left.append(char)

    def get_result(self):
        return ''.join(self.left + self.right[::-1])

import sys
initial_text = sys.stdin.readline().strip()
editor = Editor(initial_text)

n = int(sys.stdin.readline().strip())
for _ in range(n):

    command = sys.stdin.readline().split()
    if command[0] == 'L':
        editor.move_left()
    elif command[0] == 'D':
        editor.move_right()
    elif command[0] == 'B':
        editor.delete()
    elif command[0] == 'P':
        editor.insert(command[1])

# 결과 출력
print(editor.get_result())
