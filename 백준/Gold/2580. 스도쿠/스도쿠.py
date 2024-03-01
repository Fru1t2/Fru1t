import sys

data = []
for _ in range(9):
    data.append(list(map(int, sys.stdin.readline().split())))

def checking(data, x, y):
    a = (x // 3) * 3
    b = (y // 3) * 3
    alist = [1,2,3,4,5,6,7,8,9]
    for i in range(9):
        if data[i][y] in alist:
            alist.remove(data[i][y])
    for j in range(9):
        if data[x][j] in alist:
            alist.remove(data[x][j])
    for i in range(3):
        for j in range(3):
            if data[a+i][b+j] in alist:
                alist.remove(data[a+i][b+j])
    return alist

def solving(data, x=0, y=0):
    if x == 9:
        for a in data:
            print(' '.join(map(str, a)))
        exit(0)
    if data[x][y] == 0:
        for i in checking(data, x, y):
            data[x][y] = i
            if y == 8:
                solving(data, x + 1, 0)
            else:
                solving(data, x, y + 1)
            data[x][y] = 0
    else:
        if y == 8:
            solving(data, x + 1, 0)
        else:
            solving(data, x, y + 1)

solving(data)