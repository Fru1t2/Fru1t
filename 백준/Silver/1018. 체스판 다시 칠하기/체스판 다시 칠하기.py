import sys

result = []
a, b = map(int, sys.stdin.readline().split())
mylist = ["" for _ in range(a)]
for i in range(a):
    mylist[i] = list(sys.stdin.readline().strip())

for i in range(a):
    for j in range(b):
        if mylist[i][j] == "W":
            mylist[i][j] = 1
        else:
            mylist[i][j] = 0

for i in range(a-7):
    for j in range(b-7):
        draw1 = 0
        draw2 = 0
        for c in range(i, i+8):
            for d in range(j, j+8):
                if  (c + d) % 2 == 0:
                    if mylist[c][d] != 0:
                        draw1 += 1
                    if mylist[c][d] != 1:
                        draw2 += 1
                else:
                    if mylist[c][d] != 1:
                        draw1 += 1
                    if mylist[c][d] != 0:
                        draw2 += 1
        result.append(draw1)
        result.append(draw2)

print(min(result))
