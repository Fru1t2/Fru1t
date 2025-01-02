import sys

number = int(sys.stdin.readline())
alist = list(map(int, sys.stdin.readline().split()))
X = int(sys.stdin.readline())
answer = 0
check = [0] * (X+1)
for num in alist:
    if num >= X:
        continue
    if check[num]:
        answer += 1
    else:
        check[X-num] += 1

print(answer)