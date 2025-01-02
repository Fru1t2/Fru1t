class Editor:
    def __init__(self):
        self.left = list()  
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

n = int(sys.stdin.readline().strip()) 
results = []

for _ in range(n):
    commands = sys.stdin.readline().strip()  
    editor = Editor() 
    for command in commands:
        if command == "<": 
            editor.move_left()
        elif command == ">": 
            editor.move_right()
        elif command == "-": 
            editor.delete()
        else: 
            editor.insert(command)
    results.append(editor.get_result())


print("\n".join(results))
