import sys
import copy

n = int(sys.stdin.readline())
alist = []
for _ in range(n):
    alist.append(list(map(int, sys.stdin.readline().split())))

def dp_triangle(alist):
    blist = copy.deepcopy(alist)
    for i in range(1, n):
        for j in range(len(alist[i])):
            if i == 1:
                blist[i][j] = alist[i][j] + alist[0][0]
            elif j == 0:
                blist[i][j] = alist[i][j] + blist[i-1][j]
            elif j == len(alist[i]) - 1:
                blist[i][j] = alist[i][j] + blist[i-1][j-1]
            else:
                blist[i][j] = max(blist[i - 1][j - 1], blist[i - 1][j]) + alist[i][j]



    return max(blist[-1])

print(dp_triangle(alist))
