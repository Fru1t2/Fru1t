import sys

word = list(sys.stdin.readline().strip())
alist = [0] * 26
for alpha in word:
    alist[ord(alpha)-97] += 1

print(" ".join(map(str, alist)))