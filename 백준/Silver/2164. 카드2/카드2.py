import sys
import queue

number = int(sys.stdin.readline())
queue = queue.Queue()

for i in range(1, number+1):
    queue.put(i)

while queue.qsize() > 1:
    queue.get()
    a = queue.get()
    queue.put(a)

print(queue.get())