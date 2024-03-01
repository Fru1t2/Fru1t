import sys

a = int(sys.stdin.readline())

storage = []
alist = [True] * 1000000
alist[0] = alist[1] = False
for i in range(2,1000000):
    if alist[i] is not False:
        storage.append(i)
        for j in range(2*i,1000000,i):
            alist[j] = False
    else:
        continue
for _ in range(a):
    b = int(sys.stdin.readline())
    output = 0
    for i in range(2, b//2+1):
        if alist[i] and alist[b-i]:
            output += 1
    print(output)