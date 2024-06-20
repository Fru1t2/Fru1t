import sys

N = int(sys.stdin.readline())
alist = list(map(int, sys.stdin.readline().split()))
alist.sort()
total_sum = 0
def what(M: int, blist: list[int]) -> int:
    rear = len(blist) - 1
    front = 0
    while front < rear:
        pair_sum = blist[front] + blist[rear]
        if pair_sum == M:
            return 1
        elif pair_sum < M:
            front += 1
        else:
            rear -= 1
    return 0

for i in range(N):
    blist = alist[:i] + alist[i + 1:]
    total_sum += what(alist[i], blist)
print(total_sum)