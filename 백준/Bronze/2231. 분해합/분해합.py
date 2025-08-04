import sys
n = int(sys.stdin.readline())
isit = False
for i in range(n):
    num = list(str(i).strip())
    total = sum(int(x) for x in num)
    if total + i == n:
        print(i)
        isit = True
        break

if isit:
    pass
else:
    print(0)