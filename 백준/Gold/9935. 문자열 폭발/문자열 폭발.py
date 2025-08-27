import sys

base = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()
m = len(bomb)
last = bomb[-1]

stack = []
for ch in base:
    stack.append(ch)
    if ch == last and len(stack) >= m:
        ok = True
        for k in range(m):
            if stack[-1 - k] != bomb[-1 - k]:
                ok = False
                break
        if ok:
            del stack[-m:]

print(''.join(stack) if stack else 'FRULA')
