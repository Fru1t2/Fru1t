import sys

N = int(sys.stdin.readline())

def checking(col):
    for i in range(col):
        if alist[col] == alist[i]:
            return False
        elif abs(alist[col] - alist[i]) == abs(col - i):
            return False
    return True


def find(col):
    global output
    if col == N:
        output += 1
    else:
        for i in range(N):
            alist[col] = i
            if checking(col) == True:
                find(col + 1)

output = 0
alist = [0]*N
find(0)
print(output)