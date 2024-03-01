import sys

a = int(sys.stdin.readline())
output = 0
while True:
    if (a % 5) != 0:
        a -= 3
        output += 1
    else:
        output += (a // 5)
        break

if a < 0:
    print("-1")
else:
    print(output)