import sys

a = int(sys.stdin.readline())
alist = []
for _ in range(a):
    alist.append(int(sys.stdin.readline()))
alist.sort()
print(int(round(sum(alist) / len(alist) , 0)))
print(alist[(len(alist) // 2)])

bdic = dict()
for i in alist:
    if i in bdic:
        bdic[i] += 1
    else:
        bdic[i] = 1

maxbdic = max(bdic.values())
max_keys = [key for key, value in bdic.items() if value == maxbdic]
if len(max_keys) == 1:
    print(max_keys[0])
else:
    max_keys.sort()
    print(max_keys[1])

print(alist[-1] - alist[0])