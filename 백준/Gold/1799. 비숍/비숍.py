import copy
import sys
def checking(alist, x, y):
    for j, k in alist:
        if abs(x - j) == abs(y - k):
            return False
    return True

def colordel(data, color):
    data_copy = copy.deepcopy(data)
    for i in range(len(data_copy)):
        for j in range(len(data_copy)):
            if color == "White":
                if (i+j) % 2 == 0:
                    data_copy[i][j] = 0
            else:
                if (i+j) % 2 == 1:
                    data_copy[i][j] = 0
    return data_copy
def backtracking(data, x, y, alist):
    global output
    if x == len(data):  #끝날때
        output.append(len(alist))
        return

    if y == len(data):
        backtracking(data, x+1, 0, alist)
        return

    if data[x][y] == 1 and checking(alist, x, y):
        alist.append([x,y])
        backtracking(data, x, y+1, alist)
        alist.pop()
        backtracking(data, x, y+1, alist)
    else:
        backtracking(data, x, y+1, alist)

data = []
output = []
alist = []
result = 0
a = int(sys.stdin.readline())
for _ in range(a):
    data.append(list(map(int, sys.stdin.readline().split())))
data1 = colordel(data, "White")
data2 = colordel(data, "Black")
backtracking(data1, 0, 0, alist)
result += max(output)
output = []
alist = []
backtracking(data2, 0, 0, alist)
result += max(output)
print(result)