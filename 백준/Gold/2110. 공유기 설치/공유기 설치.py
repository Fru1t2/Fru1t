import sys

N, C = map(int, sys.stdin.readline().split())
alist = [int(sys.stdin.readline()) for _ in range(N)]
alist.sort()

start = 1
end = alist[-1] - alist[0]

while (start <= end):
    mid = (start+end)//2
    old = alist[0]
    count = 1

    for i in range(1, len(alist)):
        if alist[i] >= old+mid:
            count += 1
            old = alist[i]

    if count >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
